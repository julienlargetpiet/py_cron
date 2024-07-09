# py_crontab

Implementation of the crontab programm in Python

## Description

`python3 py_cron.py bash_script_to_execute cron_info`

`cron_info` is defined by the following:

seconds.minutes.hours.days.months.years.week_day

- seconds, supports list like for example 1/2 which will be all the odd seconds (step of 2) or 34-46 which will be all the seconds between 34 and 46

- minutes same but for minutes

- hours same but for hours
  
- days same but for days

- months same but for months

- years same but for years

- week_day is different from the crontab standard as the **0 corresponds to Monday** and **6 to the Sunday**

## Usage

It is one python script for one cron task. So if you want to have another cron task, just dupplicates the python script `py_cron.py` and run it too.

You can run the python script(s) as a `systemd` service, one for each cron task, apart from if you want to execute multiple programms at the same time because you can do that launching multiple programms via a shell script that will be executed by the py_cron script.

A py_cron service should look something like this:

location: `/etc/systemd/system/py_cron_task.service`

########

[Unit]
Description=description of the task

[service]
Type=Simple
User=username
WorkingDirectory=/path_to_your directory_of_the_py_cron_script
ExecStart=/path_to_your directory_of_the_py_cron_script/script.py
Restart=always

[Install]
WantedBy=multi-user.target

########

## Example

I have a shell script that i want to execute called test.sh in my directory.
I want to be executed the first 15 seconds of each odd minutes (of all hours of all days of all months of the year 2024 any week day of course)

I simply run `python3 py_cron.py $(pwd)/test.sh 1-15.1/2.*.*.*.2024.*`



