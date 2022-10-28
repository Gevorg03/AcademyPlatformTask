"""QA JSON file"""

import requests
import json

URL = "https://jsonplaceholder.typicode.com/posts"

with open('../json/src.json', encoding="utf-8") as json_file:
    user_data = json.load(json_file)

response = requests.get(URL)
json_response = json.loads(response.text)


def valid():
    """this function is responsible for checking whether such a key exists and,
    if so, whether it matches the standards entered by the user"""

    for data in json_response:
        for key, val in user_data.items():
            if key in data.keys():
                if 'id' in key.lower():
                    if not data[key] <= val[0]:
                        print(f"There is a {key}, that value is bigger than the "
                              f"entered value")
                        return
                    if val[1] != "int":
                        print(f"The {key} must be int")
                        return
                else:
                    if not len(data[key]) <= val[0]:
                        print(f"There is a {key}, that length is bigger than the "
                              f"entered value")
                        return
                    if val[1] != "string":
                        print(f"The {key} must be string")
                        return
            else:
                print(f"There is no {key}")
                return
    print("Passed")


valid()
