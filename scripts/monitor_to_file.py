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

"""
This module is for cron jobs. It stores data in a data.txt file for retrieval
from conky using:

    ${execpi 5 cat ~/.conky/scripts/data.txt}

To activate a cron job for this, issue the command crontab -e and edit your
cron jobs. Recommended configuration is to execute every 5 minutes, like
this:

    */5 * * * * python ~/.conky/scripts/monitor_to_file.py

"""

import os
import json
import time
import stat
import datetime
import argparse
from monitor import get_monitoring_data, JSON_DATA_DIR
from service_defs import service_definitions

def create_json_file(service_definition, data, verbose = False):
    json_data_file = os.path.join(JSON_DATA_DIR, service_definition + '.json')
    interval = data.get('interval')
    if file_age_in_seconds > interval:
        data_dict = {}
        monitoring_data = get_monitoring_data(service_definition, formatted = False)
        data_dict['service_name'] = monitoring_data[0]
        data_dict['status_color'] = monitoring_data[1]
        data_dict['status_message'] = monitoring_data[2]
        f = open(json_data_file, 'w')
        f.write(json.dumps(data_dict))
        f.close()
        if verbose:
            print('%s: Getting status for %s... %s' % 
                (
                    datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                    data.get('name'), 
                    monitoring_data[2]
                )
            )

def file_age_in_seconds(pathname):
    return time.time() - os.stat(pathname)[stat.ST_MTIME]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Retrieves data for json conky post-processing')
    parser.add_argument('-v', '--verbose', action='store_true', help = 'Toggles verbose')
    args = parser.parse_args()
    for service_definition, data in sorted(service_definitions.items()):
        create_json_file(service_definition, data, args.verbose)