import sys
import json
import os
import requests
import random
from time import sleep

APIGW_IP = "192.168.122.48:30010"

apis = ["students", "schools", "external"]

'''
#----------------------------------------------------------------
apis = ["https://cat-fact.herokuapp.com/facts",
        "https://api.thecatapi.com/v1/breeds",
        "https://api.thecatapi.com/v1/images/search",
        "https://api.thecatapi.com/v1/categories",
        "https://api.thecatapi.com/v1/votes",
        "https://api.thecatapi.com/v1/images"
        ]
'''

def call_random_api():
    API = random.choice(apis)
    URI = "http://" + APIGW_IP +"/" + API
    print("calling uri", URI)
    resp = requests.get(URI)
    if resp.status_code != 200:
        print("something wrong in API...exiting")
        return {"result": "error"}
    return resp.json()



def main():
    while (True):
        call_random_api()
        sleep(0.1)


if __name__ == '__main__':
    main()
