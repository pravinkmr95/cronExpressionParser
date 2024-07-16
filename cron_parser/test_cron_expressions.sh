#!/bin/bash

check_command_status() {
    if [ $? -ne 0 ]; then
        echo "Command failed: $1"
        exit 1
    fi
}

python3 main.py "20-31/2 15-23/2 1,15,25 3-12/3 1-5/2 /usr/bin/find"
check_command_status

python3 main.py "20-31/2 15-23/2 1,15,25 1-12/3 1-5/2 /usr/bin/find"
check_command_status


python3 main.py "20-31/2 15-23/2 1,15,25 1-13/3 1-5/2 /usr/bin/find"
check_command_status

python3 main.py "20-31/2 15-23/2 1,15,25 1-1/3 1-5/2 /usr/bin/find"
check_command_status


python3 main.py "20-31/2 15-23/2 1,15,25 */3 1-5/2 /usr/bin/find"
check_command_status


python3 main.py "20-31/2 15-23/2 1,15,25 * 1-5/2 /usr/bin/find"
check_command_status

python3 main.py "20-31/2 15-24/2 1,15-25 * 1-5/2 /usr/bin/find"
check_command_status

python3 main.py "20-31/2 15-23/2 1,15-25 * 1-5/2 /usr/bin/find"
check_command_status


python3 main.py "20-31/2 0 1,15-25 * 1-5/2 /usr/bin/find"
check_command_status "cd .."


python3 main.py "*/5 0 1,15 * 1-5 /usr/bin/find"
check_command_status

python3 main.py "20-25/5 0 1,15 * 1-5 /usr/bin/find"
check_command_status

python3 main.py "*/15 0 1,15 * 1-5 /usr/bin/find"
check_command_status

python3 main.py "*/15 25 1,15 * 1-5 /usr/bin/find"
check_command_status

python3 main.py "*/15 1,15 * 1-5 /usr/bin/find"
check_command_status

python3 main.py "0-59/10 0 * * * /path/to/command"
check_command_status

python3 main.py "*/5 * * * * /path/to/command"
check_command_status

python3 main.py "*/15 9-17 * * 1-5 /path/to/command"
check_command_status

python3 main.py "0 */2 * * * /path/to/command"
check_command_status

python3 main.py "30 */3 * * 1 /path/to/command"
check_command_status

python3 main.py "*/30 * 1-7 * 1 /path/to/command"
check_command_status

echo "Executed successfully."