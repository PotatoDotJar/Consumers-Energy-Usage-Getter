import sys
import requests
import pandas as pd

apiKey = "<WIP: Need to get key automatically>"

headers = {
    'Authorization': apiKey
}

def getCSVLink(promiseID):
    req = requests.get(
        "https://engage-api.simpleenergy.io/promix/" + promiseID,
        headers=headers)
    if(req.status_code == 200):
        data = req.json()

        if(data["code"] == "PROMISE_FOUND"):
            return data["promise_url"]
        else:
            return None        
    else:
        print("Error: Failed to get link for promise ID")
        quit(1)

def getFileData():
    req = requests.get(
        "https://engage-api.simpleenergy.io/gridxmw/usage/download?commodity={commodity}&date={date}&format=csv".format(date="2022-03-20", commodity="electric"),
        headers=headers)

    if(req.status_code == 200):
        data = req.json()

        fileLink = getCSVLink(data["promise_id"])
        return pd.read_csv(fileLink)
    else:
        print("Error: Failed to get promise ID")
        quit(1)

data = getFileData()
print(data)