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
import json
from service_defs import service_definitions, TYPE_NAGIOS, TYPE_UP_DOWN

JSON_DATA_DIR = os.path.join(os.path.expanduser('~'), '.conky/scripts/bucket')

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
    return (
        service,
        statuses.get(exit_code, {}).get('color', 'orange'),
        statuses.get(exit_code, {}).get('message', 'UNKNOWN')
    )

def get_up_down_status(service, exit_code):
    color = 'red'
    message = 'DOWN'
    if exit_code == 0:
        color = 'green'
        message = 'UP'
    return (service, color, message)

def format_data(service_data):
    return '%s ${alignr} ${color %s}%s${color}' % service_data

def get_monitoring_data(service_definition, formatted = True):
    if service_definition in service_definitions:
        service_definition = service_definitions.get(service_definition)
        exit_code = subprocess.call(service_definition.get('command'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        if service_definition.get('type') == TYPE_NAGIOS:
            data = get_nagios_status(service_definition.get('name'), exit_code)
        else:
            data = get_up_down_status(service_definition.get('name'), exit_code)
    else:
        data = (service_definition, 'orange', 'NOT FOUND')
    return format_data(data) if formatted else data

def get_json_data(service_definition):
    json_data_file = os.path.join(JSON_DATA_DIR, service_definition + '.json')
    json_fd = open(json_data_file, 'r')
    try:
        json_data = json.loads(json_fd.readline())
    except ValueError:
        return '%s${alignr} ${color grey}RETRIEVING${color}' % service_definitions.get(service_definition).get('name')
    finally:
        json_fd.close()
    return '%s ${alignr} ${color %s}%s${color}' % (json_data.get('service_name'), json_data.get('status_color'), json_data.get('status_message'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Retrieves data for conky processing')
    parser.add_argument('service', type = str, help = 'service source')
    parser.add_argument('-j', '--json', action='store_true', help = 'Retrieves it from scheduled json file (faster)')
    args = parser.parse_args()
    print get_json_data(args.service) if args.json else get_monitoring_data(args.service)