import asyncio
import time

from hfc.fabric import Client

#print(hfc.VERSION)

#with open('first-test.yaml') as stream:
#    conf = yaml.load(stream, Loader=Loader)

#strs = conf['test']
#print(strs)
#print(strs['name'])


loop = asyncio.get_event_loop()

cli = Client(net_profile="test-network.json")
org1_admin = cli.get_user('org1.example.com', 'Admin')

# check installed chaincode
# response = loop.run_until_complete(cli.query_installed_chaincodes(
#                requestor=org1_admin,
#                peers=['peer0.org1.example.com'],
#                decode=True
#                ))

# Channel check
# response = loop.run_until_complete(cli.query_channels(
#                requestor=org1_admin,
#                peers=['peer0.org1.example.com'],
#                decode=True
#                ))

# Query a chaincode
# args = ['24']
# response = loop.run_until_complete(cli.chaincode_query(
#                requestor=org1_admin,
#                channel_name='mychannel',
#                peers=['peer0.org1.example.com'],
#                args=args,
#                cc_name='mysmallbank'
#                ))

# Invoke Transaction
# Create account
args = ['55', 'y', '100', '100']
start = time.time()
response = loop.run_until_complete(cli.chaincode_invoke(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               fcn='create_account',
               cc_name='mysmallbank',
               wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
               ))
print(time.time()-start)
print("create_account")

# Deposit checking
args = ['100', '55']
start = time.time()
response = loop.run_until_complete(cli.chaincode_invoke(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               fcn='deposit_checking',
               cc_name='mysmallbank',
               wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
               ))
print(time.time()-start)
print("deposit_checking")

# Send payment
args = ['100', '55', '24']
start = time.time()
response = loop.run_until_complete(cli.chaincode_invoke(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               fcn='send_payment',
               cc_name='mysmallbank',
               wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
               ))
print(time.time()-start)
print("send_payment")

# Query
args = ['24']
start = time.time()
response = loop.run_until_complete(cli.chaincode_query(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               cc_name='mysmallbank'
               ))
print(time.time()-start)
print("realQuery"+response)

# invoke-query
# Send payment
args = ['24']
start = time.time()
response = loop.run_until_complete(cli.chaincode_invoke(
               requestor=org1_admin,
               channel_name='mychannel',
               peers=['peer0.org1.example.com'],
               args=args,
               fcn='query',
               cc_name='mysmallbank',
               wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
               ))
print(time.time()-start)
print("invoke-query")