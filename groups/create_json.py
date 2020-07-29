import json

def loadTxtFile():
    data = {}
    fd = open('participants.txt', 'r')
    for l in fd:
        c = l[:-1].split()
        name = c[:-1]
        group = int(c[-1:][0])
        key = " ".join(name)
        if key not in data.keys():
            data[key] = [group]
        else:
            data[key].append(group)
    fd.close()
    return data

def createJson(data):
    l = len(data)
    fd = open('groups.json', 'w')
    fd.write('[\n')
    c = 1
    for k in data.keys():
        fd.write('  {\n')
        fd.write('    name: "' + k + '",\n')
        fd.write('    groups: ' + str(data[k]) + '\n')
        
        if c == l:
            fd.write('  }\n')
        else:
            fd.write('  },\n')
        c = c + 1
    fd.write(']')
    fd.close()
    

if __name__ == '__main__':
    data = loadTxtFile()
    print(data)
    createJson(data)
