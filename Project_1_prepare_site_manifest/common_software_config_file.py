#!/usr/bin/env python3
import sys
#import yaml
from ruamel.yaml import YAML
import ipaddress

def common_software_config(site_name,corridor,location,location_id,sysadmin,location_add):

#############load existing file with fixed format########

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.explicit_end = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    stream = open("/tmp/" + site_name + "/software/config/common-software-config.yaml", "r")
    data = list(yaml.load_all(stream))
#    print(data)
    
    data[0]['data']['osh']['region_name'] = site_name
    data[0]['data']['location']['location_corridor'] = corridor
    data[0]['data']['location']['location_name'] = location.split(',')[0]
    data[0]['data']['location']['location_state'] = location.split(',')[1]
    data[0]['data']['location']['location_country'] = location.split(',')[2]
    data[0]['data']['location']['location_physical_location_id'] = location_id

    data[0]['data']['location']['location_address'] = location_add.split(',')[0]
    data[0]['data']['location']['location_zip'] = location_add.split(',')[1]

    data[0]['data']['infrastructure']['sysadmin'] = sysadmin

################dump yaml file##############

    with open("/tmp/" + site_name + "/software/config/common-software-config.yaml", "w") as f:
        yaml.dump_all(data, f)
