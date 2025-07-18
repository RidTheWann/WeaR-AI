import requests

url = "http://localhost:8000/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer my-secret-token"
}
data = {
    "messages": ["Hello"],
    "stream": False
}
response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
