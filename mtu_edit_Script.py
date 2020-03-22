# The purpose of this script is to automatically edit mtu values in a yaml file
# yaml file will be the input to this script

#!/usr/bin/env python3
import argparse
import re
import yaml

def main():
    parser = argparse.ArgumentParser("MTU update script")
    parser.add_argument('--site-file', type=open, help='path to opsimple_site.yaml', required=True)
    parser.add_argument('--site-type', help='enter medium or large', choices=['medium', 'large'], required=True)
    args = parser.parse_args()

    # Initialization
    split_re = re.compile('(\n#{10,}\n# [ A-Za-z0-9)(.,]+\n#{10,})')
    site_blocks = {}

    # Parse site yaml
    site_content = args.site_file.read()
    site_content_splitted = split_re.split(site_content)
    for index, block in enumerate(site_content_splitted):
        value = yaml.load(block)
        if value != None:
            site_blocks[list(value)[0]] = {"index": index, "value": value}

    ### *** Edit mtu for mtu_override *** ###
    aic_plugin_config = [entry for entry in site_blocks['FuelPluginConfig']['value']['FuelPluginConfig'] if entry['fuel_plugin'] == 'aic-fuel-plugin'][0]['content']['yaml_additional_config']
    aic_plugin_config['mtu_override']['br-mgmt'] = 9100
    aic_plugin_config['mtu_override']['br-storage'] = 9000
    aic_plugin_config['mtu_override']['br-mesh'] = 9150

    ### *** Edit mtu for bond1 *** ###
    for i in range(len(site_blocks['Interface']['value']['Interface'])):
        if site_blocks['Interface']['value']['Interface'][i]['name'] == 'bond1':
            site_blocks['Interface']['value']['Interface'][i]['interface_properties']['mtu'] = 9100

    ### *** Edit mtu for bond0 *** ###
    for i in range(len(site_blocks['Interface']['value']['Interface'])):
        if site_blocks['Interface']['value']['Interface'][i]['name'] == 'bond0':
            site_blocks['Interface']['value']['Interface'][i]['interface_properties']['mtu'] = 9214

    ### *** Edit mtu for eth1 *** ###
    for i in range(len(site_blocks['Interface']['value']['Interface'])):
        if site_blocks['Interface']['value']['Interface'][i]['name'] == 'eth1':
            site_blocks['Interface']['value']['Interface'][i]['interface_properties']['mtu'] = 9150

    ### *** Edit mtu for eth0 if site is medium *** ###
    if args.site_type == 'medium':
        for i in range(len(site_blocks['Interface']['value']['Interface'])):
            if site_blocks['Interface']['value']['Interface'][i]['name'] == 'eth0':
                site_blocks['Interface']['value']['Interface'][i]['interface_properties']['mtu'] = 9150

    ### *** Edit mtu for sriov interfaces if site is medium *** ###
    if args.site_type == 'medium':
        for i in range(len(site_blocks['Interface']['value']['Interface'])):
            if site_blocks['Interface']['value']['Interface'][i]['interface_properties'].keys() == {'mtu','sriov'}:
                site_blocks['Interface']['value']['Interface'][i]['interface_properties']['mtu'] = 9214

    ### *** Set ignore flag to false for all computes *** ###
    for i in range(len(site_blocks['OpenStackServer']['value']['OpenStackServer'])):
        if site_blocks['OpenStackServer']['value']['OpenStackServer'][i]['server_type'] == 'compute':
            site_blocks['OpenStackServer']['value']['OpenStackServer'][i]['ignore'] = False

    ### *** Assemble site yaml *** ###
    for key, value in site_blocks.items():
        site_content_splitted[value['index']] = yaml.dump(value['value'], default_flow_style=False, default_style='')
    print("\n\n".join(site_content_splitted))

if __name__ == '__main__':
        main()
