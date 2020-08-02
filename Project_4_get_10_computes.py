# Purpose of this script is to print the ansible playbook command limiting it to 10 computes per line
# Firstly the script will take ansible inventory file as input and extract the computes nodes from inventory
# Secondly it will print the command with limit of 10 computes per line 
# e.g. if there are 56 computes, the command will be printed 6 times
# the top 5 commands will have 10 computes per line each and the last command will have 6 computes 

#!/usr/bin/env python3
import argparse
import re

### Input to the script would be ansible inventory file containing computes,control and other nodes ###

parser = argparse.ArgumentParser(description='get 10 computes at a time')
parser.add_argument('filename', help='the file should be a list of computes')

args = parser.parse_args()

f=open(args.filename)
all_nodes = f.readlines()
f.close()

### Extract only the computes from the inventory file and store in lines variable ###

lines = []
for node in all_nodes:
    if re.match("(.)(.)(.)(.)r(.)(.)c(.)(.)(.)",node):
        lines.append(node)

### goal is to extract and print 10 computes per line so remainder if any will be stored in variable named remainder ###

lines.sort()
remainder = (len(lines)%10)

### strip for any empty spaces ###

for i, item in enumerate(lines):
    lines[i] = item.rstrip()

### print the command with 10 computes in each line ###

nodes = []
for counter, value in enumerate(lines,1):
        nodes.append(value)
        if (counter%10) == 0:
                print('ansible playbook -i inventory/ -e "mechid_file=/tmp/mechid_file.txt" playbooks/deploy_hotfix_xyz.yaml --limit ' + ':'.join(nodes),end="\n\n")
                nodes = []
                continue

### print the remainder of the computes if any ###

if remainder != 0:
        print('ansible playbook -i inventory/ -e "mechid_file=/tmp/mechid_file.txt" playbooks/deploy_hotfix_xyz.yaml --limit ' + ':'.join(nodes),end="\n")

