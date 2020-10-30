import asyncio
from hfc.fabric import Client

loop = asyncio.get_event_loop()

cli = Client(net_profile="test-network.json")

print(cli.organizations)  # orgs in the network
print(cli.peers)  # peers in the network
print(cli.orderers)  # orderers in the network
print(cli.CAs)  # ca nodes in the network

org1_admin = cli.get_user(org_name='org1.example.com', name='Admin')
orderer_admin = cli.get_user(org_name='orderer.example.com', name='Admin')

#cli.new_channel('mychannel')

responses = loop.run_until_complete(cli.channel_join(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com',
                      'peer1.org1.example.com',
                      'peer0.org2.example.com',
                      'peer1.org2.example.com'],
               orderer='orderer.example.com'
               ))
print(responses)