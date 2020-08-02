# I was given some 200 .txt files with information about unwanted files in each sites ops and fuel nodes
# txt files containing multiple blocks of information as below:
#
# --------------------------------------------------------
# root@abcxyzafuel01.abc1b.infra.aaa.ttt.net:# cd /root
# root@abcxyzafuel01.abc1b.infra.aaa.ttt.net:/root# date;find . -name \*.yaml -print |xargs ls -lhta |grep -v fuel
# Mon Dec 10 09:50:38 UTC 2019
# -rw-r--r--. 1 root root  148 Sep 18 15:27 ./mechid/puppet.yaml
# -rw-r--r--. 1 root root  635 Sep 18 15:27 ./mechid/keep_mechid.yaml
# abc123@abcxyzaopsc01:~$ date;sudo grep --include=\*.{yaml,yml} -rnwl './' -e "# Template block" |xargs ls -ltr
# Mon Dec 10 09:55:55 UTC 2019
#-r--r--r-- 1 root root 67543 Jul 3 33:10 ./kkkk/rrrr/file_abc.yaml
#-rw-r----- 1 root root 97853 Feb 28 28:10 ./latest.yaml
#
# ---------------------------------------------------------
# Task was to find unwanted files in each node for a site and delete the files
# Below script will take single .txt file as input and give the output which can be given to shell command to delete
#
# -------------------------------------------------------------
# abcxyzaopsc01 ./files/code.yaml
# abcxyzaopsc01 ./latest.yaml
# abcxyzaopsc01 ./backup.yaml
# abcxyzaopsc01 kkk_rsa
# abcxyzaopsc01 kkk_rsa.pub
# abcxyzafuel01 ./present.yaml
# abcxyzafuel01 ./ttt/bkp.yaml
# -------------------------------------------------------------


#!/usr/bin/env python3
import argparse
def main():
        parser = argparse.ArgumentParser("extraction script")
        parser.add_argument('--file', type=open, help='path to .txt file', required=True)
        args = parser.parse_args()
        lines = args.file.readlines()
        ops_lines=[]
        fuel_lines=[]
        flag=-1
        for line in lines:
                if line.find('opsc01:') != -1:
                        opsname= line.partition(' ')[0].partition('@')[2].partition(':')[0]
                        flag=1
                elif line.find('fuel01') != -1:
                        fuelname= line.partition(' ')[0].partition('@')[2].partition(':')[0]
                        flag=0
                elif flag==1:
                        if line.find(' 1 ') != -1:
                                ops_lines.append(opsname +' '+line.rpartition(' ')[2].rstrip())
                elif flag==0:
                        if line.find(' 1 ') != -1:
                                fuel_lines.append(fuelname +' '+line.rpartition(' ')[2].rstrip())
        for i in ops_lines:
                print(i)
        for j in fuel_lines:
                print(j)
if __name__ == '__main__':
        main()
