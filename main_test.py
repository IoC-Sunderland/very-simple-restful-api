import requests
from http_status_codes import http_codes

BASE_URL = "http://127.0.0.1:5000"


def response_code_message_handler(response):
    if response.status_code not in http_codes:
        print(f"No info found for status code: {response.status_code}!")
    else:
        print(response.json(),
              f"\n{response.status_code}: {http_codes[response.status_code]}")


# GET Request to RouteOne
response = requests.get(BASE_URL)
response_code_message_handler(response)

# POST Request to RouteOne
response = requests.post(BASE_URL)
response_code_message_handler(response)

# GET Request to RouteTwo with args
response = requests.get(BASE_URL + "/routetwo/sue")
response_code_message_handler(response)

# PUT Request to RouteTwo with data - 400 Bad Request
response = requests.put(BASE_URL + "/routetwo/jim",
                        {"name": "jim", "age": 90, "fav_food": 'crackers'})
response_code_message_handler(response)

# Pause for input
input()

# GET Request to RouteTwo for name that exists
response = requests.get(BASE_URL + "/routetwo/jim")
response_code_message_handler(response)


# GET Request to RouteTwo for name that does not exist
response = requests.get(BASE_URL + "/routetwo/joe")
response_code_message_handler(response)

# DELETE Request to RouteTwo to delete name if it exists
response = requests.delete(BASE_URL + "/routetwo/jim")
response_code_message_handler(response)
