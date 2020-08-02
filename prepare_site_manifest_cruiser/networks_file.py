#!/usr/bin/env python3
import sys
#import yaml
from ruamel.yaml import YAML
#import ruamel.yaml
import ipaddress
def networks(site_name,oob_cidr,oob_start,oob_end,pxe_cidr,oam_cidr,storage_cidr,calico_cidr,overlay_cidr,routable_cidr):

#def networks(site_name,oob_cidr):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.explicit_end = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    stream = open("/tmp/" + site_name + "/network/physical" + "/networks.yaml", "r")
    data = list(yaml.load_all(stream))
#    print(data)

    oob_ips = list(ipaddress.ip_network(oob_cidr))
    pxe_ips = list(ipaddress.ip_network(pxe_cidr))
    oam_ips = list(ipaddress.ip_network(oam_cidr))
    storage_ips = list(ipaddress.ip_network(storage_cidr))
    calico_ips = list(ipaddress.ip_network(calico_cidr))
    overlay_ips = list(ipaddress.ip_network(overlay_cidr))
    routable_ips = list(ipaddress.ip_network(routable_cidr))

    data[0]['data']['cidr'] = oob_cidr
    data[0]['data']['routes'][0]['gateway'] = str(oob_ips[1])
    data[0]['data']['ranges'][0]['start'] = oob_start
    data[0]['data']['ranges'][0]['end'] = oob_end

    data[1]['data']['cidr'] = pxe_cidr
    data[1]['data']['routes'][0]['gateway'] = str(pxe_ips[1])
    data[1]['data']['ranges'][0]['start'] = str(pxe_ips[1])
    data[1]['data']['ranges'][0]['end'] = str(pxe_ips[10])
    data[1]['data']['ranges'][1]['start'] = str(pxe_ips[11])
    data[1]['data']['ranges'][1]['end'] = str(pxe_ips[63])
    data[1]['data']['ranges'][2]['start'] = str(pxe_ips[64])
    data[1]['data']['ranges'][2]['end'] = str(pxe_ips[126])

    data[2]['data']['cidr'] = oam_cidr
    data[2]['data']['routes'][0]['gateway'] = str(oam_ips[1])
    data[2]['data']['ranges'][0]['start'] = str(oam_ips[1])
    data[2]['data']['ranges'][0]['end'] = str(oam_ips[10])
    data[2]['data']['ranges'][1]['start'] = str(oam_ips[11])
    data[2]['data']['ranges'][1]['end'] = str(oam_ips[-2])

    data[3]['data']['cidr'] = storage_cidr
    data[3]['data']['ranges'][0]['start'] = str(storage_ips[1])
    data[3]['data']['ranges'][0]['end'] = str(storage_ips[10])
    data[3]['data']['ranges'][1]['start'] = str(storage_ips[11])
    data[3]['data']['ranges'][1]['end'] = str(storage_ips[-2])

    data[4]['data']['cidr'] = calico_cidr
    data[4]['data']['ranges'][0]['start'] = str(calico_ips[1])
    data[4]['data']['ranges'][0]['end'] = str(calico_ips[10])
    data[4]['data']['ranges'][1]['start'] = str(calico_ips[11])
    data[4]['data']['ranges'][1]['end'] = str(calico_ips[-2])

    data[5]['data']['cidr'] = overlay_cidr
    data[5]['data']['routes'][0]['gateway'] = str(overlay_ips[1])
    data[5]['data']['ranges'][0]['start'] = str(overlay_ips[1])
    data[5]['data']['ranges'][0]['end'] = str(overlay_ips[10])
    data[5]['data']['ranges'][1]['start'] = str(overlay_ips[11])
    data[5]['data']['ranges'][1]['end'] = str(overlay_ips[-2])

    data[6]['data']['cidr'] = routable_cidr
    data[6]['data']['routes'][0]['gateway'] = str(routable_ips[1])
    data[6]['data']['ranges'][0]['start'] = str(routable_ips[2])
    data[6]['data']['ranges'][0]['end'] = str(routable_ips[-2])

    with open("/tmp/" + site_name + "/network/physical" + "/networks.yaml", "w") as f:
        yaml.dump_all(data, f)
