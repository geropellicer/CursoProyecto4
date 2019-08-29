import requests

def client():

    token_h = "Token 36cf5f60ead8db49e50bf047933c0afe6ed7c0f6"
    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/perfiles/",
                                headers=headers)

    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()