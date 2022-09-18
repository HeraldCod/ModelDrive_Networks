import requests

from pprint import pprint

import sys

router = {"ip":"172.26.198.63",
          "port":"443",
          "user":"developer",
          "pass":"C1sco12345"}

if __name__=='__main__':
    
    headers = {"Content-Type": "application/yang-data+json", "Accept": "application/yang-data+json"}

    u = "https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet1"

    u = u.format(router["ip"], router["port"])

    print(u)

    r = requests.get(u,headers = headers,
                 auth=(router["user"], router["pass"]),
                 verify=False)

    print(r.text)

    payload = "{\"hostname\": \"Router_cat\"}"

    response = requests.request("PUT",u, auth=(USER, PASS),
                            data=payload, headers=headers, verify=False)

    print(response.text)

    del_url = "https://172.26.198.63/restconf/data/Cisco-IOS-XE-native:native/interface/TenGigabitEthernet=1%2F0%2F10/ip/address/primary"

    delete_response = requests.request("DELETE",del_url, auth=(USER, PASS),
                             headers=headers, verify=False)

    print(response.text)


    

