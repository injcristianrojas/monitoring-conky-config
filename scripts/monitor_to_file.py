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

from monitor import get_monitoring_data, JSON_DATA_FILE
from service_defs import service_definitions
import json

"""
This module is for cron jobs. It stores data in a data.txt file for retrieval
from conky using:

    ${execpi 5 cat ~/.conky/scripts/data.txt}

To activate a cron job for this, issue the command crontab -e and edit your
cron jobs. Recommended configuration is to execute every 5 minutes, like
this:

    */5 * * * * python ~/.conky/scripts/monitor_to_file.py

"""

if __name__ == '__main__':
    f = open(JSON_DATA_FILE, 'w')
    data_dict = {}
    for service_definition, data in sorted(service_definitions.items()):
        print('Getting status for %s' % data.get('name'))
        data_dict[service_definition] = {}
        monitoring_data = get_monitoring_data(service_definition, formatted = False)
        data_dict[service_definition]['service_name'] = monitoring_data[0]
        data_dict[service_definition]['status_string'] = monitoring_data[1]
        #f.write(get_monitoring_data(service_definition) + '\n')
    f.write(json.dumps(data_dict))
    f.close()