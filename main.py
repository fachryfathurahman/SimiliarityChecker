
from similiarity import *
import requests

url = "https://api.ofcode.dev/ilab/submission/"
TaskDetailID = "63193"
urlWithID = url + TaskDetailID

responseWithID = requests.get(urlWithID)
responseAll = requests.get(url)

allData = responseAll.json()
dataWithId = responseWithID.json()['data']
dataWithIdContent = dataWithId['Content']
dataWithIdContent = remove_comment(dataWithIdContent)


max_value = float()
last_percentage = []
for x in allData['data']:
    if x['Content'] == '' or dataWithId['Content'] == '' or x['TaskDetailID'] == dataWithId['TaskDetailID']:
        continue
    tmp_x = remove_comment(x['Content'])
    resutlt = documentSimiliarity(dataWithIdContent, tmp_x)
    if resutlt[1] > max_value:
        max_value = resutlt[1]
        last_percentage = [x['TaskDetailID'], resutlt]

print(last_percentage)

# directory = "D:\praktikumsem4\machine learning\similiaritychecker\\testing"
# test_path = "D:\praktikumsem4\machine learning\similiaritychecker\\testing\\257_1.txt"
# files_path = [os.path.abspath(os.path.join(directory, p)) for p in os.listdir(directory)]
# max_value = float()
# path_max = "not found"
# list_final = []
# for files in files_path:
#     percentage = documentSimiliarity(test_path, files)
#     split_test_path = test_path.split("_")[0]
#     split_files = files.split("_")[0]
#     print(files, percentage)
#     if test_path == files:
#         continue
#     if split_test_path == split_files:
#         continue
#     if percentage[1] >= max_value:
#         path_max = files
#         max_value = percentage[1]
#         list_final = [path_max, percentage]
#
# print(list_final)
