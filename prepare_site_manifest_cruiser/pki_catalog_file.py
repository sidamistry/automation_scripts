#!/usr/bin/env python3
import sys
#import yaml
from ruamel.yaml import YAML
import ipaddress

def pki(site_name,oam_cidr,calico_cidr,genesis_hostname,master_2_hostname,master_3_hostname,master_4_hostname):

#############load existing file with fixed format########

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.explicit_end = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    stream = open("/tmp/" + site_name + "/pki/pki-catalog.yaml", "r")
    data = list(yaml.load_all(stream))
#    print(data)

#############Initialize ip's of required cidr's###########

    oam_ips = list(ipaddress.ip_network(oam_cidr))
    calico_ips = list(ipaddress.ip_network(calico_cidr))

    data[0]['data']['certificate_authorities']['kubernetes']['certificates'] = []
################rack1##############

    data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({'document_name': 'kubelet-' + genesis_hostname, 'common_name': 'system:node:' + genesis_hostname, 'hosts': [genesis_hostname, str(oam_ips[11]), str(calico_ips[11])], 'groups': ['system:nodes']})

    for i in range(10):
        data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({ 'document_name': 'kubelet-' + (genesis_hostname[:-4] + 'c' + format(i+1, "03")), 'common_name': 'system:node:' + (genesis_hostname[:-4] + 'c' + format(i+1, "03")), 'hosts': [(genesis_hostname[:-4] + 'c' + format(i+1, "03")), str(oam_ips[i+12]), str(calico_ips[i+12])], 'groups': ['system:nodes']})

################rack2##############

    data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({'document_name': 'kubelet-' + master_2_hostname, 'common_name': 'system:node:' + master_2_hostname, 'hosts': [master_2_hostname, str(oam_ips[22]), str(calico_ips[22])], 'groups': ['system:nodes']})

    for i in range(10):
        data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({'document_name': 'kubelet-' + (master_2_hostname[:-4] + 'c' + format(i+1, "03")), 'common_name': 'system:node:' + (master_2_hostname[:-4] + 'c' + format(i+1, "03")), 'hosts': [(master_2_hostname[:-4] + 'c' + format(i+1, "03")), str(oam_ips[i+23]), str(calico_ips[i+23])], 'groups': ['system:nodes']})

################rack3##############

    data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({'document_name': 'kubelet-' + master_3_hostname, 'common_name': 'system:node:' + master_3_hostname, 'hosts': [master_3_hostname, str(oam_ips[33]), str(calico_ips[33])], 'groups': ['system:nodes']})

    for i in range(10):
        data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({'document_name': 'kubelet-' + (master_3_hostname[:-4] + 'c' + format(i+1, "03")), 'common_name': 'system:node:' + (master_3_hostname[:-4] + 'c' + format(i+1, "03")), 'hosts': [(master_3_hostname[:-4] + 'c' + format(i+1, "03")), str(oam_ips[i+34]), str(calico_ips[i+34])], 'groups': ['system:nodes']})

################rack4##############

    data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({'document_name': 'kubelet-' + master_4_hostname, 'common_name': 'system:node:' + master_4_hostname, 'hosts': [master_4_hostname, str(oam_ips[44]), str(calico_ips[44])], 'groups': ['system:nodes']})

    for i in range(10):
        data[0]['data']['certificate_authorities']['kubernetes']['certificates'].append({'document_name': 'kubelet-' + (master_4_hostname[:-4] + 'c' + format(i+1, "03")), 'common_name': 'system:node:' + (master_4_hostname[:-4] + 'c' + format(i+1, "03")), 'hosts': [(master_4_hostname[:-4] + 'c' + format(i+1, "03")), str(oam_ips[i+45]), str(calico_ips[i+45])], 'groups': ['system:nodes']})

################dump yaml file##############

    with open("/tmp/" + site_name + "/pki/pki-catalog.yaml", "w") as f:
        yaml.dump_all(data, f)
