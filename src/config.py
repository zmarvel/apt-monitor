
from configparser import ConfigParser
from pathlib import Path


class Config():
    def __init__(self, path):
        self.path = Path(path).resolve()
        print('Attempting to open config {}'.format(path))
        if not self.path.exists():
            raise FileNotFoundError(path)
        self.config = ConfigParser()
        self.config.read(self.path)

    def get_host(self, hostname):
        return self.config[hostname]

    def get_hosts(self):
        return list(filter(lambda h: h != 'DEFAULTS' and h != 'apt-monitor', self.config.sections()))

    def __getitem__(self, key):
        return self.config[key]
