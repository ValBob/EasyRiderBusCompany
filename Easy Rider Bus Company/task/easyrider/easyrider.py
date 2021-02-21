# Write your awesome code here
import json


def right_sequence(former, later):
    t1 = [int(i) for i in former.split(':')]
    t2 = [int(i) for i in later.split(':')]
    if t2[0] > t1[0]:
        return True
    elif t2[0] == t1[0]:
        if t2[1] > t1[1]:
            return True
    return False


json_in = json.loads(input())

print('Arrival time test:')
same_bus = 0
time_before = ''
switch_flag = True  # To skip remained bus line stops if wrong time detected
ok = True  # Flag for no wrong times detected

for row in json_in:
    if row['bus_id'] == same_bus:
        if switch_flag:
            if not right_sequence(time_before, row['a_time']):
                print(f'bus_id line {row["bus_id"]}: wrong time on station {row["stop_name"]}')
                switch_flag = False
                ok = False
    else:
        switch_flag = True
    same_bus = row['bus_id']
    time_before = row['a_time']
if ok:
    print('OK')
