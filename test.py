import asyncio

<<<<<<< HEAD
# import yaml
# try:
#     from yaml import CLoader as Loader, CDumper as Dumper
# except ImportError:
#     from yaml import Loader, Dumper
=======
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
>>>>>>> abe828df8b16335f968db098f3b528813f682665

from hfc.fabric import Client



#print(hfc.VERSION)

#with open('first-test.yaml') as stream:
#    conf = yaml.load(stream, Loader=Loader)

#strs = conf['test']
#print(strs)
#print(strs['name'])


loop = asyncio.get_event_loop()
<<<<<<< HEAD
cli = Client(net_profile="first-network.json")
org1_admin = cli.get_user('Org1MSP', 'Admin')

response = loop.run_until_complete(cli.query_installed_chaincodes(
               requestor=org1_admin,
               
               peers=['peer0.org1.example.com'],
               decode=True
               ))
=======
cli = Client(net_profile="test-network.json")
org1_admin = cli.get_user('org1.example.com', 'Admin')

# response = loop.run_until_complete(cli.query_installed_chaincodes(
#                requestor=org1_admin,
#                peers=['peer0.org1.example.com'],
#                decode=True
#                ))
>>>>>>> abe828df8b16335f968db098f3b528813f682665



# response = loop.run_until_complete(cli.query_channels(
#                requestor=org1_admin,
#                peers=['peer0.org1.example.com'],
#                decode=True
#                ))

<<<<<<< HEAD
# print(response)
=======
# print(response)



# Query a chaincode
args = ['a']
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_query(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               cc_name='mycc'
               ))
print(response)
>>>>>>> abe828df8b16335f968db098f3b528813f682665
