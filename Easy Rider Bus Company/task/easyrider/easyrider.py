# Write your awesome code here
import json

json_in = json.loads(input())

routes = {}

for row in json_in:
    if not routes.get(row['bus_id']):
        routes[row['bus_id']] = [row['stop_type']]
    else:
        routes[row['bus_id']].append(row['stop_type'])

for bus_id in routes:
    if not ('S' in routes[bus_id] and 'F' in routes[bus_id]):
        print(f'There is no start or stop for the line: {bus_id}.')
        break
else:
    starts = set()
    finishes = set()
    stops = {}
    for row in json_in:
        if row['stop_type'] == 'S':
            starts.add(row['stop_name'])
        elif row['stop_type'] == 'F':
            finishes.add(row['stop_name'])

        if not stops.get(row['stop_name']):
            stops[row['stop_name']] = [row['bus_id']]
        else:
            stops[row['stop_name']].append(row['bus_id'])
    transfers = [k for k, v in stops.items() if len(v) > 1]
    print(f'Start stops: {len(starts)} {sorted([*starts])}')
    print(f'Transfer stops: {len(transfers)} {sorted(transfers)}')
    print(f'Finish stops: {len(finishes)} {sorted([*finishes])}')


