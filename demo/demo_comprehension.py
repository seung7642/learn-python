scores = [x + y for x in range(5) for y in range(5)]
print(scores)

scores = {x + y for x in range(5) for y in range(5)}
print(scores)

names = ('John', 'David', 'Linda')
ages = (20, 30, 40)
user_info = {k: v for k, v in zip(names, ages)}
print(user_info)
