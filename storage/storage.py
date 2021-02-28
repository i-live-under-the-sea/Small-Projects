import json

def write(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

def store(name ,data):
    path = 'store'
    w = {}
    w[name] = data
    write(path, name, w)



def getstorage(name):
    if(name[-4:] == "json"):
        with open("./store/"+name) as f:
            data = json.load(f)
        print(data['name'])
        return data['name']
    else:
        with open("./store/"+name + ".json") as f:
            data = json.load(f)
        return data[name]
        

