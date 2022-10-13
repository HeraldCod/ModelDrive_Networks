import requests
import json

url = "https://10.10.10.152:8080/rpc/get-interface-information"

headers = {
    'Accept': "application/json",
    'Content-Type':"application/xml"
}

# Pushing the API call response to response variable as python dictionary using json library

response = requests.get(url, headers=headers, auth=('herald', '@@@@@@@@@@')).json()

print(json.dumps(response, indent=2, sort_keys=True))

