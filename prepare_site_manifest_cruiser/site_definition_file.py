#!/usr/bin/env python3
import sys
#import yaml
from ruamel.yaml import YAML
import ipaddress

def site_definition(site_name,global_repo_tag,secrets_repo_name):

#############load existing file with fixed format########

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.explicit_end = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    stream = open("/tmp/" + site_name + "/site-definition.yaml", "r")
    data = list(yaml.load_all(stream))
#    print(data)

    data[0]['metadata']['name'] = site_name
    data[0]['data']['repositories']['global']['revision'] = global_repo_tag
    data[0]['data']['repositories']['secrets']['url'] = 'ssh://REPO_USERNAME@codecloud.web.att.com:7999/ST_CCPSECURE/' + secrets_repo_name

################dump yaml file##############

    with open("/tmp/" + site_name + "/site-definition.yaml", "w") as f:
        yaml.dump_all(data, f)
