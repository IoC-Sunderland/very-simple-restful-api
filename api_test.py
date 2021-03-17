"""Testing the very simple RESTful API
"""

import requests
import time
from http_status_codes import http_codes

BASE_URL = "https://new-restful-api.herokuapp.com/"
TIME_DELAY = 3 # Used to aid readability of responses as script runs

def response_code_message_handler(response):
    if response.status_code not in http_codes:
        print(f"No info found for status code: {response.status_code}!")
        time.sleep(TIME_DELAY)
    else:
        print(response.json(),
              f"\n{response.status_code}: {http_codes[response.status_code]}")
        time.sleep(TIME_DELAY)


# GET Request to RouteOne - 200: Success
response = requests.get(BASE_URL)
response_code_message_handler(response)

# POST Request to RouteOne - 200: Success
response = requests.post(BASE_URL)
response_code_message_handler(response)

# PUT Request to RouteTwo with data - 200: Success
response = requests.put(BASE_URL + "/routetwo/jim",
                        {"name": "jim", "age": 90, "fav_food": 'crackers'})
response_code_message_handler(response)

# GET Request to RouteTwo for name that exists - 200: Success
response = requests.get(BASE_URL + "/routetwo/jim")
response_code_message_handler(response)


# GET Request to RouteTwo for name that does not exist - 404: Error
response = requests.get(BASE_URL + "/routetwo/joe")
response_code_message_handler(response)

# DELETE Request to RouteTwo to delete name if it exists - 200: Success
response = requests.delete(BASE_URL + "/routetwo/jim")
response_code_message_handler(response)

# Try some more requests here:
