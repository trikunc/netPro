import json

data_router = open("ip.txt", "r").read()

data = data_router.split("\n")

data_fix = []
for i in range (len(data)):
    router = data[i].split(";")
    data_fix.append({
    'IP':router[0],
    'USER':router[1],
    'PASS':router[2]
})

# print(data_fix)
print(json.dumps(data_fix, indent=3))