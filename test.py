import requests
from requests.structures import CaseInsensitiveDict
import json


url = 'http://127.0.0.1:8000/api/links'
headers = CaseInsensitiveDict()

headers["Content-Type"] = "application/json"
headers["Authorization"] = "Token 0f0d7f926cb8da8faeffbec60377509ec94ed920"

username = 'http://127.0.0.1:8000/api/'
password = 'bigwiz2021'

info = {
  
  "url": username,
  
  "info": password
}

data = json.dumps(info,indent=2)

resp = requests.post(url, headers=headers,data=data)
print(resp.json())