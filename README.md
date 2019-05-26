
# apt-monitor

apt-monitor provides a web interface to easily view which Aptitude-based systems
need package upgrades. It uses the [asyncssh][asyncssh] library to establish
an SSH connection to a list of systems, and the [Flask][flask] framework for
the web interface.


## Usage

apt-monitor should be provided with a list of systems to monitor, as well as an
SSH key associated with each system. It can be configured to poll each system
after a particular interval has elapsed.


### Configuration

apt-monitor looks for `apt-monitor.ini` in the project root (the same folder as
the `src` directory) by default. Here's an example:

```
[apt-monitor]
interval=60

[DEFAULTS]
IdentityFile=~/.ssh/id_rsa
User=zack

[system1]

[system2]
IdentityFile=~/.ssh/id_rsa_other
```

### Running

The project can be run from the project root with
```
$ FLASK_APP=src/web.py flask run
```

It can be stopped with Ctrl-C.


## Considerations

- apt-monitor queries each system at a regular interval, and stores the list of
  packages that need upgraded in memory. If you are using apt-monitor for a
  particularly large number of systems, this could become a problem.
- This web interface **should not** be made publicly accesible. An attacker
  could use it to determine that a vulnerable package is running on your
  system.



[asyncssh]: https://asyncssh.readthedocs.io/en/latest/
[flask]: http://flask.pocoo.org/
