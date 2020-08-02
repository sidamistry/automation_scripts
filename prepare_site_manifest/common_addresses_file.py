#!/usr/bin/env python3
import sys
#import yaml
from ruamel.yaml import YAML
import ipaddress

def common_addresses(site_name,oob_start,pxe_cidr,storage_cidr,calico_cidr,routable_cidr,calico_ingress_cidr,genesis_hostname,master_2_hostname,master_3_hostname,master_4_hostname,ldap_mechid):

#############load existing file with fixed format########

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.explicit_end = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    stream = open("/tmp/" + site_name + "/network/common-addresses.yaml", "r")
    data = list(yaml.load_all(stream))
#    print(data)

#############Initialize ip's of required cidr's###########

    pxe_ips = list(ipaddress.ip_network(pxe_cidr))
    storage_ips = list(ipaddress.ip_network(storage_cidr))
    calico_ips = list(ipaddress.ip_network(calico_cidr))
    routable_ips = list(ipaddress.ip_network(routable_cidr))
    calico_ingress_ips = list(ipaddress.ip_network(calico_ingress_cidr))

#############Fill up common-addresses.yaml with values###########

    data[0]['data']['calico']['bgp']['ipv4']['public_service_cidr'] = calico_ingress_cidr
    data[0]['data']['calico']['bgp']['ipv4']['ingress_vip'] = str(calico_ingress_ips[1]) + '/32'
    data[0]['data']['calico']['bgp']['ipv4']['maas_vip'] = str(calico_ingress_ips[2]) + '/32'
    data[0]['data']['calico']['bgp']['ipv4']['peers'][0] = str(calico_ips[2])
    data[0]['data']['calico']['bgp']['ipv4']['peers'][1] = str(calico_ips[3])
    data[0]['data']['calico']['ip_rule']['gateway'] = str(calico_ips[1])

    data[0]['data']['dns']['node_domain'] = site_name + '.cci.att.com'
    data[0]['data']['dns']['ingress_domain'] = site_name + '.cci.att.com'

    data[0]['data']['genesis']['hostname'] = genesis_hostname
    data[0]['data']['genesis']['ip'] = str(calico_ips[11])
    data[0]['data']['genesis']['oob'] = oob_start

    data[0]['data']['bootstrap']['ip'] = str(pxe_ips[11])

    data[0]['data']['masters'][0]['hostname'] = master_2_hostname
    data[0]['data']['masters'][1]['hostname'] = master_3_hostname
    data[0]['data']['masters'][2]['hostname'] = master_4_hostname

    data[0]['data']['ldap']['username'] = ldap_mechid

    data[0]['data']['storage']['ceph']['public_cidr'] = storage_cidr
    data[0]['data']['storage']['ceph']['cluster_cidr'] = storage_cidr


################dump yaml file##############

    with open("/tmp/" + site_name + "/network/common-addresses.yaml", "w") as f:
        yaml.dump_all(data, f)
