def gen1to3():
  yield 1;
  yield 2;
  yield 3;

i = gen1to3()
print(next(i))
print(next(i))
print(next(i))
print(next(i))