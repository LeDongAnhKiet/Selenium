import csv

with open('test.csv', 'w', newline='') as f:
    field = ['user', 'password']
    w = csv.DictWriter(f, fieldnames=field)
    w.writeheader()
    w.writerow({'user': 'boi', 'password': '1234'})

with open('test.csv', 'r', newline='') as f:
    r = csv.DictReader(f)
    for row in r:
        user = row['user']
        password = row['password']

print(user + ' ' + password)
