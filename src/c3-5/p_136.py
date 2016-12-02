nums = [1, 3, 5, 7, 9]
x2 = lambda x : x * 2

print(list(map(x2, nums)))

print(list(map(lambda x : x * 2, nums)))
print(list(map(lambda x : x * 3, nums)))
print(list(map(lambda x : x * 4, nums)))