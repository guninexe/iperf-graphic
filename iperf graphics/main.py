import json
import matplotlib.pyplot as plt


def autolabel(rects, labels=None, height_factor=1.01):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if labels is not None:
            try:
                label = labels[i]
            except (TypeError, KeyError):
                label = ' '
        else:
            label = '%d' % int(height)
        ax.text(rect.get_x() + rect.get_width()/2., height_factor*height,
                '{}'.format(label),
                ha='center', va='bottom')



path = 'log.json'

byte = []
second  = []

with open(path, 'r') as f:
    data = json.loads(f.read())
    for i in data['intervals']:
        byte.append(i['streams'][0]['bytes'])
        second.append(i['streams'][0]['start'])


bt = []

for i in byte:
    am = i/1000
    bt.append(am)

print(second)
plt.bar(second, bt)
plt.xlabel('timeline'), plt.ylabel('kb/s')
ax = plt.gca()
autolabel(ax.patches, bt, height_factor=1.0)

plt.show()

with open(path, "w") as f:
    pass