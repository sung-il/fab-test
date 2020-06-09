import asyncio

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from hfc.fabric import Client



#print(hfc.VERSION)

#with open('first-test.yaml') as stream:
#    conf = yaml.load(stream, Loader=Loader)

#strs = conf['test']
#print(strs)
#print(strs['name'])


loop = asyncio.get_event_loop()
cli = Client(net_profile="first-network.json")
org1_admin = cli.get_user('Org1MSP', 'Admin')

# response = loop.run_until_complete(cli.query_installed_chaincodes(
#                requestor=org1_admin,
#                peers=['peer0.org1.example.com'],
#                decode=True
#                ))



response = loop.run_until_complete(cli.query_channels(
               requestor=org1_admin,
               peers=['peer0.org1.example.com'],
               decode=True
               ))

print(response)