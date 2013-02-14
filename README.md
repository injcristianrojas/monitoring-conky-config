# Conky configuration for monitoring purposes

## Intro

As part of my everyday work, I must monitor different systems and software mainly
using Nagios. But Nagios is pretty uncomfortable most of the time, and, let's face it,
[nobody really checks those Nagios e-mails](http://devopsreactions.tumblr.com/post/39118334785/carefully-examining-nagios-emails).

So I saw in [Conky](http://conky.sourceforge.net/) an opportunity to monitor things a
little better, on-screen. I took some freely available conky scripts, and I tried them
on my Ubuntu GNOME Shell Remix machine. Hope this works for you too.

## Quick Start

First, clone the repo in your home directory under the `.conky` directory. If you have
that directory already, back it up.

    git clone git@github.com:injcristianrojas/monitoring-conky-config.git ~/.conky

In order to use Conky, you must have a ~/.conkyrc file. To make things a little easier,
create a symbolic link:

    ln -s .conky/conkyrc ~/.conkyrc

You're almost ready. Now make a copy of the example service definitions file called
`service_defs.py` and you will have three examples up and running:

    cd .conky/scripts
    cp service_defs_example.py service_defs.py

Run `conky` and you're good to go.

## A little deeper

The last lines of the conkyrc file call a python module, which monitors service
commands:

    ${execpi 10 python ~/.conky/scripts/monitor.py mon1}
    ${execpi 10 python ~/.conky/scripts/monitor.py mon2}
    ${execpi 10 python ~/.conky/scripts/monitor.py mon3}

You can define the services to bo monitored and their check types in the
`service_definitions` dictionary on the `service_defs.py` file. Each service
definition must be created as follows:

    'MON_ID': {
    	'command': 'COMMAND_TO_BE_EXECUTED',
    	'name': 'NAME_TO_APPEAR',
    	'type': 'CHECK_TYPE'
    }

The parameters are the following:

* `MON_ID`: Service ID. Must match the one indicated as the argument of the
`monitor.py` call in `conkyrc` (`mon1`, `mon2`, `mon3`...).
* `COMMAND_TO_BE_EXECUTED`: Command to be executed by the service.
* `NAME_TO_APPEAR`: Name that will appear in the conky display for this service.
* `CHECK_TYPE`: Depending on `COMMAND_TO_BE_EXECUTED`'s exit code it can display status
information depending on one of the following types:
  * `TYPE_UP_DOWN`: If the service command has an exit code of 0, displays `UP`.
  Otherwise, it displays `DOWN`.
  * `TYPE_NAGIOS`: This type of display is based on the Nagios style of status
  definitions. It displays `OK` if the command has an exit code of 0, `WARNING`
  if it is 1, and `CRITICAL` if it is 2.


## Caveats

* The **Wireless Networking Stats** section in the conkyrc file is based on my
laptop's configuration. Change them from `eth1` to whatever your main
networking interface is in your machine.

## License

This work is licensed under the Apache License, version 2.0:


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