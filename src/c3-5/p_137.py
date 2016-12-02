nums = [1, 2, 3, 11, 12, 13, 21, 22, 23]
print(list(filter(lambda x : (x % 2) == 0, nums)))
print(list(filter(lambda x : (x % 2) == 1, nums)))
print(list(filter(lambda x : x > 13, nums)))
print(list(filter(lambda x : x < 8, nums)))