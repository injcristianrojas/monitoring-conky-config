# Conky configuration for monitoring purposes

## Intro

As part of my everyday work, I must monitor different systems and software mainly
using Nagios. But Nagios is pretty uncomfortable most of the time, and, let's face it,
[nobody really checks those Nagios e-mails](http://devopsreactions.tumblr.com/post/39118334785/carefully-examining-nagios-emails).

So I saw in Conky an opportunity to monitor things a little better, on-screen. I took
some freely available conky scripts, and I tried them on my Ubuntu GNOME Shell Remix
machine. Hope this works for you too.

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

Execute conky and you're good to go.
