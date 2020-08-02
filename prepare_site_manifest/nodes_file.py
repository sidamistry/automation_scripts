#!/usr/bin/env python3
import sys
import yaml
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import SingleQuotedScalarString as sq
import ipaddress

def nodes(site_name,ilo_cidr,ilo_start,ilo_end,pxe_cidr,management_cidr,storage_cidr,calico_cidr,overlay_cidr,genesis_hostname,master_2_hostname,master_3_hostname,master_4_hostname):
#def nodes(site_name):

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.explicit_end = True
    yaml.indent(mapping=2, sequence=4, offset=2)

    stream = open("/tmp/" + site_name + "/baremetal" + "/nodes.yaml", "r")
    data = list(yaml.load_all(stream))
#    print(data)

    ilo_ips = list(ipaddress.ip_network(ilo_cidr))
    pxe_ips = list(ipaddress.ip_network(pxe_cidr))
    management_ips = list(ipaddress.ip_network(management_cidr))
    storage_ips = list(ipaddress.ip_network(storage_cidr))
    calico_ips = list(ipaddress.ip_network(calico_cidr))
    overlay_ips = list(ipaddress.ip_network(overlay_cidr))
    
    for i in range(10):
        data.append({'schema': sq('drydock/BaremetalNode/v1'), 'metadata': {'schema': sq('metadata/Document/v1'), 'name':  (genesis_hostname[:-4] + 'c' + format(i+1, "03")), 'layeringDefinition': {'abstract': False, 'layer': 'site'}, 'storagePolicy': 'cleartext'}, 'data': {'ilo': {'account': sq('tier4')}, 'host_profile': 'nc-p1-adv', 'addressing': [{'network': 'ilo', 'address': str(ipaddress.ip_address(ilo_start)+i+1)}, {'network': 'management', 'address': str(management_ips[i+12])}, {'network': 'pxe', 'address': str(pxe_ips[i+12])}, {'network': 'storage', 'address': str(storage_ips[i+12])}, {'network': 'calico', 'address': str(calico_ips[i+12])}, {'network': 'overlay', 'address': str(overlay_ips[i+12])}], 'metadata': {'rack': ('rack' + genesis_hostname[-6:-4]), 'tags':[sq('workers')]}}})

    data.append({'schema': sq('drydock/BaremetalNode/v1'), 'metadata': {'schema': sq('metadata/Document/v1'), 'name': master_2_hostname, 'layeringDefinition': {'abstract': False, 'layer': 'site'}, 'storagePolicy': 'cleartext'}, 'data': {'ilo': {'account': sq('tier4')}, 'host_profile': 'nc-cp-primary-adv', 'addressing': [{'network': 'ilo', 'address': str(ipaddress.ip_address(ilo_start)+11)}, {'network': 'management', 'address': str(management_ips[22])}, {'network': 'pxe', 'address': str(pxe_ips[22])}, {'network': 'storage', 'address': str(storage_ips[22])}, {'network': 'calico', 'address': str(calico_ips[22])}, {'network': 'overlay', 'address': str(overlay_ips[22])}],'metadata': {'rack': ('rack' + master_2_hostname[-6:-4]), 'tags': [sq('masters')]}}})

    for i in range(10):
        data.append({'schema': sq('drydock/BaremetalNode/v1'), 'metadata': {'schema': sq('metadata/Document/v1'), 'name':  (master_2_hostname[:-4] + 'c' + format(i+1, "03")), 'layeringDefinition': {'abstract': False, 'layer': 'site'}, 'storagePolicy': 'cleartext'}, 'data': {'ilo': {'account': sq('tier4')}, 'host_profile': 'nc-p1-adv', 'addressing': [{'network': 'ilo', 'address': str(ipaddress.ip_address(ilo_start)+i+12)}, {'network': 'management', 'address': str(management_ips[i+23])}, {'network': 'pxe', 'address': str(pxe_ips[i+23])}, {'network': 'storage', 'address': str(storage_ips[i+23])}, {'network': 'calico', 'address': str(calico_ips[i+23])}, {'network': 'overlay', 'address': str(overlay_ips[i+23])}], 'metadata': {'rack': ('rack' + master_2_hostname[-6:-4]), 'tags': [sq('workers')]}}})

    data.append({'schema': sq('drydock/BaremetalNode/v1'), 'metadata': {'schema': sq('metadata/Document/v1'), 'name': master_3_hostname, 'layeringDefinition': {'abstract': False, 'layer': 'site'}, 'storagePolicy': 'cleartext'}, 'data': {'ilo': {'account': sq('tier4')}, 'host_profile': 'nc-cp-primary-adv', 'addressing': [{'network': 'ilo', 'address': str(ipaddress.ip_address(ilo_start)+22)}, {'network': 'management', 'address': str(management_ips[33])}, {'network': 'pxe', 'address': str(pxe_ips[33])}, {'network': 'storage', 'address': str(storage_ips[33])}, {'network': 'calico', 'address': str(calico_ips[33])}, {'network': 'overlay', 'address': str(overlay_ips[33])}], 'metadata': {'rack': ('rack' + master_3_hostname[-6:-4]),'tags': [sq('masters')]}}})

    for i in range(10):
        data.append({'schema': sq('drydock/BaremetalNode/v1'), 'metadata': {'schema': sq('metadata/Document/v1'), 'name':  (master_3_hostname[:-4] + 'c' + format(i+1, "03")), 'layeringDefinition': {'abstract': False, 'layer': 'site'}, 'storagePolicy': 'cleartext' }, 'data': {'ilo': {'account': sq('tier4')}, 'host_profile': 'nc-p1-adv', 'addressing': [{'network': 'ilo', 'address': str(ipaddress.ip_address(ilo_start)+i+23)}, {'network': 'management', 'address': str(management_ips[i+34])}, {'network': 'pxe', 'address': str(pxe_ips[i+34])}, {'network': 'storage', 'address': str(storage_ips[i+34])}, {'network': 'calico', 'address': str(calico_ips[i+34])}, {'network': 'overlay', 'address': str(overlay_ips[i+34])}],'metadata': {'rack': ('rack' + master_3_hostname[-6:-4]), 'tags': [sq('workers')]}}})

    data.append({'schema': sq('drydock/BaremetalNode/v1'), 'metadata': {'schema': sq('metadata/Document/v1'), 'name': master_4_hostname, 'layeringDefinition': {'abstract': False, 'layer': 'site'}, 'storagePolicy': 'cleartext'}, 'data': {'ilo': {'account': sq('tier4')}, 'host_profile': 'nc-cp-secondary-adv', 'addressing': [{'network': 'ilo', 'address': str(ipaddress.ip_address(ilo_start)+33)}, {'network': 'management', 'address': str(management_ips[44])}, {'network': 'pxe', 'address': str(pxe_ips[44])}, {'network': 'storage', 'address': str(storage_ips[44])}, {'network': 'calico', 'address': str(calico_ips[44])}, {'network': 'overlay', 'address': str(overlay_ips[44])}], 'metadata': {'rack': ('rack' + master_4_hostname[-6:-4]), 'tags': [sq('masters')]}}})

    for i in range(10):
        data.append({'schema': sq('drydock/BaremetalNode/v1'), 'metadata': {'schema': sq('metadata/Document/v1'), 'name':  (master_4_hostname[:-4] + 'c' + format(i+1, "03")), 'layeringDefinition': {'abstract': False, 'layer': 'site'}, 'storagePolicy': 'cleartext'}, 'data': {'ilo': {'account': sq('tier4')}, 'host_profile': 'nc-p1-adv', 'addressing': [{'network': 'ilo', 'address': str(ipaddress.ip_address(ilo_start)+i+34)}, {'network': 'management', 'address': str(management_ips[i+45])}, {'network': 'pxe', 'address': str(pxe_ips[i+45])}, {'network': 'storage', 'address': str(storage_ips[i+45])}, {'network': 'calico', 'address': str(calico_ips[i+45])}, {'network': 'overlay', 'address': str(overlay_ips[i+45])}], 'metadata': {'rack': ('rack' + master_4_hostname[-6:-4]), 'tags': [sq('workers')]}}})

    with open("/tmp/" + site_name + "/baremetal" + "/nodes.yaml", "w") as f:
        yaml.dump_all(data, f)
