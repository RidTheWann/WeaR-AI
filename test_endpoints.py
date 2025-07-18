import requests

base_url = "http://localhost:8000"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer my-secret-token"
}

def test_health():
    resp = requests.get(f"{base_url}/v1/health")
    print("/v1/health:", resp.status_code, resp.json())

def test_embeddings():
    data = {"input": ["Hello", "World"]}
    resp = requests.post(f"{base_url}/v1/embeddings", json=data, headers=headers)
    print("/v1/embeddings:", resp.status_code, resp.json())

def test_chat():
    data = {"messages": ["Hello"], "stream": False}
    resp = requests.post(f"{base_url}/v1/chat/completions", json=data, headers=headers)
    print("/v1/chat/completions:", resp.status_code, resp.json())

if __name__ == "__main__":
    test_health()
    test_embeddings()
    test_chat()
