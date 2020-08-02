# Script to generate site manifests


### Rationale

Whenever deploying a new site one needs to manually create below files which is a repetitive task.

	1. $NEW_SITE/site-definition.yaml
	2. $NEW_SITE/baremetal/nodes.yaml
	4. $NEW_SITE/network/common-addresses.yaml
	6. $NEW_SITE/pki/pki-catalog.yaml
	7. $NEW_SITE/profiles/region.yaml
	8. $NEW_SITE/network/physical/networks.yaml
	9. $NEW_SITE/software/config/common-software-config.yaml

### What To Do!

1. Run the script main.py and enter required parameters as per your site

                python3 main.py

        Example for entering parameters:

                root@stack:/home/stack/script_final# python3 main.py
                Enter site name: site12a
                Enter ilo cidr range in format a.b.c.d/x: 32.33.34.0/26
                Enter start ip for ilo range: 32.33.34.1
                Enter end ip for ilo range: 32.33.34.62
                Enter pxe cidr range in format a.b.c.d/x: 10.11.12.128/25
                Enter management cidr range in format a.b.c.d/x: 32.33.35.0/26
                Enter storage cidr range in format a.b.c.d/x: 10.11.13.128/25
                Enter calico cidr range in format a.b.c.d/x: 10.11.14.128/25
                Enter overlay cidr range in format a.b.c.d/x: 10.11.15.0/25
                Enter routable cidr range in format a.b.c.d/x: 32.33.36.0/28
                Enter calico ingress cidr range in format a.b.c.d/x: 32.33.37.128/29
                Enter genesis hostname e.g. sitea01o001 :
                Enter hostname for second controller node e.g. site101o002:
                Enter hostname for third controller node e.g. sitea01o003:
                Enter hostname for fourth controller node e.g. sitea01o004:
                Enter ldap mechid to be used by the site e.g test123@test.com:
                Enter tag/branch name for global repo :
                Enter secrets repo name e.g secrets-repo :
                Enter corridor detail e.g 'prod' : 
                Enter location details in the format City, State, Country e.g LosAngeles,CA,US:
                Enter physical location id for the site e.g. TESTSITE01 :
                Enter id for sysadmin e.g.admin :

2. A folder for your site name will be created in /tmp directory with required files

                root@stack:/tmp# cd site12a/
                root@stack:/tmp/site12a# ls -l
                total 28
                drwxr-xr-x 2 root root 4096 Mar 11 16:01 baremetal
                drwxr-xr-x 3 root root 4096 Mar 11 16:01 network
                drwxr-xr-x 2 root root 4096 Mar 11 16:01 pki
                drwxr-xr-x 2 root root 4096 Mar 11 16:01 profiles
                -rw-r--r-- 1 root root  483 Mar 11 16:01 site-definition.yaml
                drwxr-xr-x 4 root root 4096 Mar 11 16:01 software
                root@stack:/tmp/site12a#
                

Note(One Time Setup): 
1. This script will require python3.6 or higher version of python. If using lower version of python install python3-yaml module,
2. Please install ruamel.yaml package on your local
                apt install python3-pip				
                sudo -H pip3 install ruamel.yaml
