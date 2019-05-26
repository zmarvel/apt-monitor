
import threading
from time import sleep
import asyncssh
import asyncio
from pathlib import Path

# 5 minutes
DEFAULT_INTERVAL = 5*60


class Monitor(threading.Thread):
    def __init__(self, config):
        super().__init__()
        self.config = config
        # apt-monitor settings
        app_config = config['apt-monitor']
        if 'interval' in app_config:
            self.interval = float(app_config['interval'])
        else:
            self.interval = DEFAULT_INTERVAL
        # seconds
        self.sleep_slice = 5
        self.app_config = app_config

        # default SSH client settings
        self.defaults = config['DEFAULTS']

        self._done = False
        self._status = {}

    def run(self):
        while not self._done:
            asyncio.run(self._run())
            slept = 0
            while slept < self.interval and not self._done:
                sleep(self.sleep_slice)
                slept += self.sleep_slice

    def join(self):
        self._done = True
        super().join()

    async def _run(self):
        tasks = []
        for host in self.config.get_hosts():
            if host not in ['DEFAULTS', 'apt-monitor']:
                tasks.append(self.check_host(host))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for (host, stdout, stderr) in results:
            self._status[host] = list(
                filter(lambda line: line != '', stdout))
            print('HOST {} => {}'.format(host, stderr))

    async def check_host(self, host):
        if 'IdentityFile' in self.config[host]:
            client_keys = [Path(self.config[host]['IdentityFile']).
                           expanduser()
                           .resolve()]
        else:
            client_keys = [Path(self.defaults['IdentityFile']).
                           expanduser().
                           resolve()]

        if 'User' in self.config[host]:
            username = self.config[host]
        else:
            username = self.defaults['User']

        async with asyncssh.connect(host, username=username,
                                    client_keys=client_keys) as conn:
            cmd = '/usr/bin/apt list --upgradable'
            print('Running {} on {}'.format(cmd, host))
            upgradable_list = conn.run(cmd)
            completed = await upgradable_list
            if completed.exit_status == 0:
                return (host, completed.stdout.splitlines(),
                        completed.stderr.splitlines())
            else:
                raise ConnectionError(host)

    def get_status(self, host=None):
        if host is not None:
            return self._status[host]
        else:
            return self._status
