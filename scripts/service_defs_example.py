TYPE_NAGIOS = 0
TYPE_UP_DOWN = 1

service_definitions = {
  'mon1': {
    'command': 'ls -la',
    'name': 'Check ls',
    'type': TYPE_UP_DOWN
  },
  'mon2': {
    'command': 'python -c "import sys;from random import randint;sys.exit(randint(0,2))"',
    'name': 'Random Nagios exit code',
    'type': TYPE_NAGIOS
  },
  'mon3': {
    'command': 'python -c "import sys;from random import randint;sys.exit(randint(0,2))"',
    'name': 'Random UP/DOWN exit code',
    'type': TYPE_UP_DOWN
  },
}