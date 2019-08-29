import requests

def client():
    credentials_registro = {"username": "gero2",
                    "email": "gerogero@gero.gero",
                    "password1": "asdasdasd2",
                    "password2": "asdasdasd2",}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                                data=credentials_registro)

    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()