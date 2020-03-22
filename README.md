# automation_scripts
I created a bunch of python scripts for automating my manual day-to-day activities. The scripts are commented to explain the purpose and logic of the code

### 1. get_10_computes.py

#### Purpose of this script is to print the ansible playbook command limiting it to 10 computes per line
The script will take ansible inventory file as input and extract the compute nodes from inventory
Secondly it will print the command with limit of 10 computes per line
e.g. if there are 56 computes, the command will be printed 6 times
The top 5 commands will have 10 computes per line each and the last command will have 6 computes

### 2. extraction_script.py

#### Purpose of this script is to extract files to be deleted from each node in a format that can be given as input to shell commands

Usage: python3 extraction_script.py --file abc.txt

### 3. mtu_edit_script.py

#### Purpose of this script is to edit mtu values in a yaml file with the use of script in order to prevent mistakes and save time

Usage: python3 mtu_edit_Script.py --site-file=abc.yaml --site-type=large
