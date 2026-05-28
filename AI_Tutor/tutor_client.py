import requests
url="http://localhost:8000/tutor"

json_data = {
    "prompt": "You are a python teacher teach me python using example and code snippet. teach step by step by answering follow up questions",}


try:
    response = requests.post(url, json=json_data)
    print(f"status code: {response.status_code}")
    print(f"response: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")    