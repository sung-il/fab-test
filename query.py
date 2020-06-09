import asyncio
from hfc.fabric import Client

loop = asyncio.get_event_loop()

cli = Client(net_profile="first-network.json")
org1_admin = cli.get_user('Org1MSP', 'Admin')

# Query a chaincode
<<<<<<< HEAD
args = ['query']
=======
args = ['a']
>>>>>>> abe828df8b16335f968db098f3b528813f682665
# The response should be true if succeed
response = loop.run_until_complete(cli.chaincode_query(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               cc_name='mycc'
               ))
print(response)