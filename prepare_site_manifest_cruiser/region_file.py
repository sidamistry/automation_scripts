#!/usr/bin/env python3
import sys
#import yaml
from ruamel.yaml import YAML
import ipaddress

def region(site_name):

#############load existing file with fixed format########

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.explicit_end = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    stream = open("/tmp/" + site_name + "/profiles/region.yaml", "r")
    data = list(yaml.load_all(stream))
#    print(data)

    data[0]['metadata']['name'] = site_name
    data[0]['metadata']['substitutions'][0]['src']['name'] = site_name + '_ssh_public_key'

################dump yaml file##############

    with open("/tmp/" + site_name + "/profiles/region.yaml", "w") as f:
        yaml.dump_all(data, f)
