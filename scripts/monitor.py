#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Copyright 2013 Cristián Rojas

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

import os
import subprocess
import argparse
from service_defs import service_definitions, TYPE_NAGIOS, TYPE_UP_DOWN

def get_nagios_status(service, exit_code):
    statuses = {
        0: {
            'color': 'green',
            'message': 'OK'
        },
            1: {
            'color': 'yellow',
            'message': 'WARNING'
        },
            2: {
            'color': 'red',
            'message': 'CRITICAL'
        },
    }
    return '%s ${alignr} ${color %s}%s${color}' % (service, statuses[exit_code]['color'], statuses[exit_code]['message'])

def get_up_down_status(service, exit_code):
    color = 'red'
    message = 'DOWN'
    if exit_code is 0:
        color = 'green'
        message = 'UP'
    return '%s ${alignr} ${color %s}%s${color}' % (service, color, message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Sends SSH commands over multiple tunnels')
    parser.add_argument('service', type = str, help = 'service source')
    args = parser.parse_args()
    if args.service in service_definitions:
        service_definition = service_definitions[args.service]
        exit_code = subprocess.call(service_definition['command'], shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        if service_definition['type'] == TYPE_NAGIOS:
            print get_nagios_status(service_definition['name'], exit_code)
        else:
            print get_up_down_status(service_definition['name'], exit_code)
    else:
        print "${color red}Service with key %s NOT FOUND${color}" % args.service