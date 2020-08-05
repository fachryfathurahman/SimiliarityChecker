
from similiarity import *
import requests
import sys

url = "https://api.ofcode.dev/ilab/submission/"
TaskDetailID = str(sys.argv)
urlWithID = url + TaskDetailID

responseWithID = requests.get(urlWithID)
responseAll = requests.get(url)

allData = responseAll.json()
allData = allData['data']


listIdx = list()
size = len(allData)
for x in range(len(allData)):
    y = x+1
    if y == size:
        break
    elif allData[x]['TaskDetailID'] == allData[y]['TaskDetailID']:
        listIdx.append(x)

allData = [i for j, i in enumerate(allData) if j not in listIdx]

dataWithId = responseWithID.json()['data']
dataWithIdContent = dataWithId['Content']
dataWithIdContent = remove_comment(dataWithIdContent)


max_value = float()
last_percentage = []
for x in allData:
    if x['Content'] == '' or dataWithId['Content'] == '' or x['TaskDetailID'] == dataWithId['TaskDetailID']:
        continue
    tmp_x = remove_comment(x['Content'])
    resutlt = documentSimiliarity(dataWithIdContent, tmp_x)
    if resutlt[1] > max_value:
        max_value = resutlt[1]
        last_percentage = [x['TaskDetailID'], resutlt]

print(last_percentage)

