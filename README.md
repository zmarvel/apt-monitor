
# apt-monitor

apt-monitor provides a web interface to easily view which Aptitude-based systems
need package upgrades. It uses the [asyncssh][asyncssh] library to establish
an SSH connection to a list of systems, and the [Flask][flask] framework for
the web interface.

## Usage

apt-monitor should be provided with a list of systems to monitor, as well as an
SSH key associated with each system. It can be configured to poll each system
after a particular interval has elapsed.

## Considerations

- apt-monitor queries each system at a regular interval, and stores the list of
  packages that need upgraded in memory. If you are using apt-monitor for a
  particularly large number of systems, this could become a problem.
- This web interface **should not** be made publicly accesible. An attacker
  could use it to determine that a vulnerable package is running on your
  system.



[asyncssh]: https://asyncssh.readthedocs.io/en/latest/
[flask]: http://flask.pocoo.org/
