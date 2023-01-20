import json
import matplotlib.pyplot as plt


path = 'log.json'

byte = []
with open(path, 'r') as f:
    data = json.loads(f.read())
    for i in data['intervals']:
        byte.append(i['streams'][0]['bytes'])

plt.plot(byte)
plt.show()

with open(path, "w") as f:
    pass