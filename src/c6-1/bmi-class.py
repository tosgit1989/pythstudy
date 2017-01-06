class BMI:
  def __init__(self, weight, height):
    ''' 初期化 '''
    self.weight = weight
    self.height = height
    self.calcBMI()

  def calcBMI(self):
    ''' BMIを計算する '''
    h = self.height / 100
    self.bmi = self.weight / (h ** 2)

  def printJudge(self):
    ''' 結果を表示する '''
    print("---")
    print("BMI=", self.bmi)
    b = self.bmi
    if (b < 18.5): print("痩せ型")
    elif (b < 25): print("標準")
    else: print("肥満", (b // 5) - 4, "度")

person1 = BMI(weight=65, height=170)
person1.printJudge()

person2 = BMI(76, 165)
person2.printJudge()

person3 = BMI(weight=50, height=180)
person3.printJudge()
