# Write your awesome code here
import json
import re

data_structure = {
        "bus_id": (int, False),
        "stop_id": (int, False),
        "stop_name": (str, False),
        "next_stop": (int, False),
        "stop_type": (str, True),
        "a_time": (str, False)
    }

err_dict = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0
    }

json_in = json.loads(input())

for row in json_in:
    for key in row:
        if key == "stop_name" and not bool(re.match(r'[A-Z][\w ]* (Road|Avenue|Boulevard|Street)$', row[key])):
            err_dict[key] += 1
        if key == "stop_type" and not bool(re.match(r'[SFO]?$', row[key])):
            err_dict[key] += 1
        if key == "a_time" and not bool(re.match(r'([01]\d|2[0-3]):[0-5]\d$', row[key])):
            err_dict[key] += 1

errors_n = 0
for value in err_dict.values():
    errors_n += value

print(f'Format validation: {errors_n} errors')
for key, value in err_dict.items():
    if key in ["stop_name", "stop_type", "a_time"]:
        print(f'{key}: {value}')

'''
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]
'''