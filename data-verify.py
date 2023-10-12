import requests
import logging
from requests.structures import CaseInsensitiveDict

url = "http://18.192.48.168:5000/cubes"
team = "/team33"
teamurl =url+team

def checkAvailability():
    logging.info('I told you so')
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Content-Length"] = "1"

    resp = requests.post(url, headers=headers)

    print(resp.status_code)

def checkData():
    logging.info('I told you so')
    headers = CaseInsensitiveDict()
    headers["Auth"] = "testToken"
    headers["Content-Type"] = "application/json"

    data = """
    {
    "time": "2023-10-10 17:10:05", 
    "config": {
        "1": "red", 
        "2": "blue", 
        "3": "red", 
        "4": "yellow", 
        "5": "",
        "6": "",
        "7": "yellow", 
        "8": "red"
        } 
    }"""
    resp = requests.post(teamurl, headers=headers, data=data)

    print(resp.status_code)

checkData()
checkAvailability()