#!/usr/bin/env python3
import os
import shutil
import networks_file
import nodes_file
import pki_catalog_file
import common_addresses_file
import region_file
import site_definition_file
import common_software_config_file

def main():
    site_name = input("Enter site name e.g. site12a : ")
    ilo_cidr = input("Enter ilo cidr range in format a.b.c.d/x: ")
    ilo_start = input("Enter start ip for ilo range: ")
    ilo_end = input("Enter end ip for ilo range: ")
    pxe_cidr = input("Enter pxe cidr range in format a.b.c.d/x: ")
    management_cidr = input("Enter management cidr range in format a.b.c.d/x: ")
    storage_cidr = input("Enter storage cidr range in format a.b.c.d/x: ")
    calico_cidr = input("Enter calico cidr range in format a.b.c.d/x: ")
    overlay_cidr = input("Enter overlay cidr range in format a.b.c.d/x: ")
    routable_cidr = input("Enter routable cidr range in format a.b.c.d/x: ")
    calico_ingress_cidr = input("Enter calico ingress cidr range in format a.b.c.d/x: ")
    genesis_hostname = input("Enter genesis hostname e.g. site101o001 : ")
    master_2_hostname = input("Enter hostname for second controller node e.g. site101o002 : ")
    master_3_hostname = input("Enter hostname for third controller node e.g. site101o003 : ")
    master_4_hostname = input("Enter hostname for fourth controller node e.g. site101o004 : ")
    ldap_mechid = input("Enter ldap mechid to be used by the site e.g test123@test.com: ")
    global_repo_tag = input("Enter tag/branch name for global repo: ")
    secrets_repo_name = input("Enter secrets repo name: ")
    corridor = input("Enter corridor detail e.g 'prod' : ")
    location = input("Enter location details in the format City, State, Country e.g LosAngeles,CA,US : ")
    location_id = input("Enter physical location id for the site e.g. TESTSITE01 : ")
    location_add = input("Enter location address and zip in the format street address, zip code : ")
    sysadmin = input("Enter attid for sysadmin e.g. admin: ")

    try:
        os.mkdir("/tmp/" + site_name)
        os.mkdir("/tmp/" + site_name + "/baremetal")
        os.mkdir("/tmp/" + site_name + "/deployment")
        os.mkdir("/tmp/" + site_name + "/network")
        os.mkdir("/tmp/" + site_name + "/network" + "/physical")
        os.mkdir("/tmp/" + site_name + "/pki")
        os.mkdir("/tmp/" + site_name + "/profiles")
        os.mkdir("/tmp/" + site_name + "/software")
        os.mkdir("/tmp/" + site_name + "/software" + "/charts")
        os.mkdir("/tmp/" + site_name + "/software" + "/charts" + "/kubernetes")
        os.mkdir("/tmp/" + site_name + "/software" + "/charts" + "/kubernetes" + "/container-networking")
        os.mkdir("/tmp/" + site_name + "/software" + "/config")
    except OSError:
        print ("Creation of the directory failed... Directory already exists in /tmp")


    shutil.copy('files/nodes.yaml','/tmp/' + site_name + "/baremetal")
    shutil.copy('files/networks.yaml','/tmp/' + site_name + "/network/physical")
    shutil.copy('files/common-addresses.yaml','/tmp/' + site_name + "/network")
    shutil.copy('files/pki-catalog.yaml','/tmp/' + site_name + "/pki")
    shutil.copy('files/region.yaml','/tmp/' + site_name + "/profiles")
    shutil.copy('files/site-definition.yaml','/tmp/' + site_name)
    shutil.copy('files/common-software-config.yaml','/tmp/' + site_name + "/software/config")

    networks_file.networks(site_name,ilo_cidr,ilo_start,ilo_end,pxe_cidr,management_cidr,storage_cidr,calico_cidr,overlay_cidr,routable_cidr)

    nodes_file.nodes(site_name,ilo_cidr,ilo_start,ilo_end,pxe_cidr,management_cidr,storage_cidr,calico_cidr,overlay_cidr,genesis_hostname,master_2_hostname,master_3_hostname,master_4_hostname)

    pki_catalog_file.pki(site_name,management_cidr,calico_cidr,genesis_hostname,master_2_hostname,master_3_hostname,master_4_hostname)

    common_addresses_file.common_addresses(site_name,ilo_start,pxe_cidr,storage_cidr,calico_cidr,routable_cidr,calico_ingress_cidr,genesis_hostname,master_2_hostname,master_3_hostname,master_4_hostname,ldap_mechid)

    region_file.region(site_name)

    site_definition_file.site_definition(site_name,global_repo_tag,secrets_repo_name)

    common_software_config_file.common_software_config(site_name,corridor,location,location_id,sysadmin,location_add)

if __name__ == '__main__':
        main()
