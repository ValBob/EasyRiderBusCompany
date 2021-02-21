# Write your awesome code here
import json


json_in = json.loads(input())

print('On demand stops test:')
stop_name_type = {}
wrong_stops = []
ok = True  # Flag for no wrong times detected

for row in json_in:
    if not stop_name_type.get(row['stop_name']):
        stop_name_type[row['stop_name']] = set(row['stop_type'])
    else:
        stop_name_type[row['stop_name']].add(row['stop_type'])
        if 'O' in stop_name_type[row['stop_name']] and len(stop_name_type[row['stop_name']]) > 1:
            wrong_stops.append(row['stop_name'])
            ok = False
if ok:
    print('OK')
else:
    print(f'Wrong stop type: {sorted(wrong_stops)}')
