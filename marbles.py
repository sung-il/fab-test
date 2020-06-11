import asyncio
import time

from hfc.fabric import Client


loop = asyncio.get_event_loop()

cli = Client(net_profile="test-network.json")
org1_admin = cli.get_user('org1.example.com', 'Admin')

name="TE"
color="sky"
size="35"
owner="TE"

# initMarbles
# for i in range(10,51):
#     args = [name+str(i), color, size, owner+str(i)]
#     response = loop.run_until_complete(cli.chaincode_invoke(
#                 requestor=org1_admin,
#                 channel_name='mychannel',
#                 peers=['peer0.org1.example.com'],
#                 args=args,
#                 fcn='initMarble',
#                 cc_name='mymarbles',
#                 wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#                 ))
#     time.sleep(2)
#     print(i)
#     print(response)

# readMarble
# args = [name]
# response = loop.run_until_complete(cli.chaincode_invoke(
#             requestor=org1_admin,
#             channel_name='mychannel',
#             peers=['peer0.org1.example.com'],
#             args=args,
#             fcn='readMarble',
#             cc_name='mymarbles',
#             wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#             ))
# print(response)

# for i in range(10000):
#     args = [name+str(i), color, size, owner+str(i)]
#     response = loop.run_until_complete(cli.chaincode_invoke(
#             requestor=org1_admin,
#             channel_name='mychannel',
#             peers=['peer0.org1.example.com'],
#             args=args,
#             fcn='initMarble',
#             cc_name='mymarbles',
#             wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
            # ))
    # print("initMarble")
    # print(response)

# for i in range(1):
#     args = ["doc02"]
#     response = loop.run_until_complete(cli.chaincode_invoke(
#             requestor=org1_admin,
#             channel_name='mychannel',
#             peers=['peer0.org1.example.com'],
#             args=args,
#             fcn='readMarble',
#             cc_name='mymarbles',
#             wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#             ))
#     print("readMarble")
#     print(response)

# for i in range(1):
#     args = ["0"]
#     response = loop.run_until_complete(cli.chaincode_invoke(
#             requestor=org1_admin,
#             channel_name='mychannel',
#             peers=['peer0.org1.example.com'],
#             args=args,
#             fcn='getHistoryForMarble',
#             cc_name='mymarbles',
#             wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#             ))
#     print("getHistoryForMarble")
#     print(response)



# Test
# for i in range(10):
#     args = ["RT1", "RT99"]
#     response = loop.run_until_complete(cli.chaincode_invoke(
#             requestor=org1_admin,
#             channel_name='mychannel',
#             peers=['peer0.org1.example.com'],
#             args=args,
#             fcn='getMarblesByRange',
#             cc_name='mymarbles',
#             wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#             ))
    #print("getMarblesByRange")
    #print(response)

# for i in range(20):
#     args = ["RT0", "RT99"]
#     response = loop.run_until_complete(cli.chaincode_invoke(
#             requestor=org1_admin,
#             channel_name='mychannel',
#             peers=['peer0.org1.example.com'],
#             args=args,
#             fcn='getMarblesByRange',
#             cc_name='mymarbles',
#             wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
#             ))
    # print(response)