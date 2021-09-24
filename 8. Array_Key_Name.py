#8. Parse the following JSON to get all the values of a key ‘name’ within an array
import json
sample = [
    {
        "id":1,
        "name":"name1",
        "color":[
            "red",
            "green"
        ]
    },
    {
        "id":2,
        "name":"name2",
        "color":[
            "pink",
            "yellow"
        ]
    }
]

data = json.dumps(sample)
for rec in sample:
    print(rec['name'])

