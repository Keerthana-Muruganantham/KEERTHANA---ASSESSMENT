#5. Two lists convert it into the dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res = {}
for key, value in zip(keys, values):
        res[key] = value
print(res)


