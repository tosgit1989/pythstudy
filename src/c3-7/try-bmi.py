from math import floor
while True:
  try:
    weight = float(input("体重は？"))
    height = float(input("身長は？"))
    bmi = weight / ((height / 100) * (height / 100))
    break;
  except:
    print("入力ミスがあります。再度入力してください。")

result = ""
if bmi < 18.5: result = "痩せ型"
elif bmi < 25: result = "標準体重"
else:
  fat_lv = floor((bmi / 5) - 4)
  result = "".join(["肥満", str(fat_lv), "度"])

print("BMI: ", bmi)
print("判定: ", result)