import asyncio
import time

from hfc.fabric import Client


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

for customer_id in range(99, 110):
    args = [str(customer_id), customer_name, inital_checking_balance, inital_savings_balance]
    response = loop.run_until_complete(cli.chaincode_invoke(
                requestor=org1_admin,
                channel_name='mychannel',
                peers=['peer0.org1.example.com'],
                args=args,
                fcn='create_account',
                cc_name='mysmallbank',
                wait_for_event=True # for being sure chaincode invocation has been commited in the ledger, default is on tx event
                ))    
    print("peer0.org1")

for customer_id in range(110, 120):
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
    print("peer1.org1")