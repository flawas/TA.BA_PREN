import requests
from requests.structures import CaseInsensitiveDict

url = "http://18.192.48.168:5000/cubes/team33"

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
resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)