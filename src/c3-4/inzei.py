def calc_royality(price, sales, per):
  rate = per / 100
  ro = int(price * sales * rate)
  return ro

i = input("定価は？")
price = int(i)

i = input("発行部数は？")
sales = int(i)

i = input("印税率(パーセント)は？")
per = float(i)

v = calc_royality(price, sales, per)
print("印税は、", v, "円です")