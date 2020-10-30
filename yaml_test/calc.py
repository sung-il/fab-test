import yaml

COST_GETSTATE=10
COST_PUTSTATE=100
COST_MARSHAL=100
COST_UNMARSHAL=100
COST_RETURN=100

result = dict()
fi = dict()

with open('base-cost.yaml') as stream:
    conf = yaml.load(stream, Loader=yaml.Loader)

for func in conf["chaincode"]:
    # print(func)
    RESULT_GETSTATE=func["GetState"]*COST_GETSTATE
    RESULT_PUTSTATE=func["PutState"]*COST_PUTSTATE
    RESULT_MARSHAL=func["Marshal"]*COST_MARSHAL
    RESULT_UNMARSHAL=func["Unmarshal"]*COST_UNMARSHAL
    RESULT_RETURN=func["Return"]*COST_RETURN

    result[func['fn']]=RESULT_GETSTATE+RESULT_PUTSTATE+RESULT_MARSHAL+RESULT_UNMARSHAL+RESULT_RETURN

# print(result)
fi["chaincode"]=result
with open('cost.yaml', 'w') as f:
    yaml.dump(fi, f)