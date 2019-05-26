
from .config import Config
from .monitor import Monitor


DEFAULT_CONFIG_PATH = 'apt-monitor.ini'
_config = Config(DEFAULT_CONFIG_PATH)

_monitor = Monitor(_config)

_monitor.start()
