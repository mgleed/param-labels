with open("ParamLabels.csv") as f:
    csv = [line.rstrip('\n').split(',') for line in f.readlines() if not line.isspace()]

hashes = []
csvout = []
for i in csv:
    if not int(i[0], 16) in hashes:
        hashes.append(int(i[0], 16))
        csvout.append((f"{int(i[0], 16):#0{12}x}", i[1]))

csvout.sort(key=lambda i: i[1])

with open("ParamLabels.csv", 'w') as f:
    f.write('\n'.join([','.join(line) for line in csvout]))
