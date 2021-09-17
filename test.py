import requests
from requests.structures import CaseInsensitiveDict
import json


url = 'http://127.0.0.1:8000/lt/profile'
headers = CaseInsensitiveDict()

headers["Content-Type"] = "application/json"
headers["Authorization"] = "Token 0f0d7f926cb8da8faeffbec60377509ec94ed920"

username = 'toshiba'
password = 'bigwiz2021'

info = {
  
  "username": username,
  
  "password": password
}

data = json.dumps(info,indent=2)

resp = requests.get(url, headers=headers)
print(resp.json())