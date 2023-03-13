import csv
import json


# Ex 1

def csv_to_json(csv1, json1):
    with open(csv1, 'r') as f1:
        result = csv.DictReader(f1)

        data = []
        for row in result:
            data.append(row)

    with open(json1, 'w') as f2:
        json.dump(data, f2, indent=4)


csv_to_json('from.csv', 'into.json')


# Ex 2

def json_2(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    half = len(data) // 2

    first = data[:half]
    second = data[half:]

    with open('1st.json', 'w') as f:
        json.dump(first, f, indent=4)

    with open('2nd.json', 'w') as f:
        json.dump(second, f, indent=4)


json_2('into.json')
