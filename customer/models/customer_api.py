import requests

api_url = "https://fttx.smarten.com.np/api/v1/pod/list"


def get_data():
    response = requests.get(url=api_url)
    data = response.json()
    return data

print(get_data())

