# Write your awesome code here
import json

json_in = json.loads(input())

routes = {}
for row in json_in:
    if not routes.get(row['bus_id']):
        routes[row['bus_id']] = [row['stop_id']]
    else:
        routes[row['bus_id']].append(row['stop_id'])


print('Line names and number of stops:')
for key, value in routes.items():
    print(f'bus_id: {key}, stops: {len(value)}')

