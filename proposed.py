import yaml
import asyncio
import time

from hfc.fabric import Client

# with open('first-test.yaml') as stream:
#     conf = yaml.load(stream, Loader=yaml.Loader)

# # strs = conf['conf']
# # print(strs)
# # print(strs['peer'])
# # dic = strs['peer']
# # print(dic[0]['id'])

# conf_test = conf['conf']

# for peer in conf_test['peer']:
#     print(peer['id'])
#     print(peer['spec'])

# for msb in conf_test['mysmallbank']:
#     print(msb['fn'])
#     print(msb['ec'])

# print(conf_test['mysmallbank'][0]['fn'])


# ======

loop = asyncio.get_event_loop()
cli = Client(net_profile="test-network.json")
org1_admin = cli.get_user('org1.example.com', 'Admin')

customer_id='74'
customer_name='test'
inital_checking_balance='1000'
inital_savings_balance='1000'
amount='1000'
dest_customer_id='55'
source_customer_id=customer_id

args = [dest_customer_id]
response = loop.run_until_complete(cli.chaincode_invoke(
            requestor=org1_admin,
            channel_name='mychannel',
            peers=['peer1.org1.example.com'],
            args=args,
            fcn='query',
            cc_name='mycc',
            wait_for_event=False # for being sure chaincode invocation has been commited in the ledger, default is on tx event
            ))
print("peer1.org1.example.com, queryy")

for customer_id in range(3000, 4000):
    args = [str(customer_id), customer_name, inital_checking_balance, inital_savings_balance]
    response = loop.run_until_complete(cli.chaincode_invoke(
                requestor=org1_admin,
                channel_name='mychannel',
                peers=['peer1.org1.example.com'],
                args=args,
                fcn='create_account',
                cc_name='mysmallbank',
                wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
                ))    
print("create_account")

for customer_id in range(3000, 4000):
    args = [str(customer_id)]
    response = loop.run_until_complete(cli.chaincode_invoke(
                requestor=org1_admin,
                channel_name='mychannel',
                peers=['peer1.org1.example.com'],
                args=args,
                fcn='query',
                cc_name='mysmallbank',
                wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
                ))
print("invoke-query")

# Connection with peer0.org1.example.com
args = [dest_customer_id]
response = loop.run_until_complete(cli.chaincode_invoke(
            requestor=org1_admin,
            channel_name='mychannel',
            peers=['peer0.org1.example.com'],
            args=args,
            fcn='query',
            cc_name='mysmallbank',
            wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
            ))
print("peer0.org1.example.com, query")

for customer_id in range(3000, 4000):
    args = [amount, str(customer_id)]
    response = loop.run_until_complete(cli.chaincode_invoke(
                requestor=org1_admin,
                channel_name='mychannel',
                peers=['peer0.org1.example.com'],
                args=args,
                fcn='deposit_checking',
                cc_name='mysmallbank',
                wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
                ))
print("deposit_checking")

for customer_id in range(3000, 4000):
    args = [amount, dest_customer_id, str(customer_id)]
    response = loop.run_until_complete(cli.chaincode_invoke(
                requestor=org1_admin,
                channel_name='mychannel',
                peers=['peer0.org1.example.com'],
                args=args,
                fcn='send_payment',
                cc_name='mysmallbank',
                wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
                ))
print("send_payment")
