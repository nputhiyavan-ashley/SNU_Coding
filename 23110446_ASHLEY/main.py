#ASSUMED JSON INPUT GIVEN AS VALUE HERE IN THE VARIABLE 'json'

json={"user":{"name":"Ana"},"active":True}
keys=[]
result={}
temp=[]

for key in list(json.keys()).sort():
    if type(json[key]) is dict():
        innerkeys=list(json[key].keys())
        innerkeys.sort()
        for key in inner_key:
            