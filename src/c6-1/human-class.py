# <<<クラスを使った場合>>>
class Human:
  ''' 人間を表すクラス '''

  def search1(self, place):
    ''' 周りを見る処理 '''
    pass

  def take1(self, food):
    ''' 物をつかむ処理 '''
    self.food_taken1 = food

  def open_mouth1(self):
    ''' 口を開ける処理 '''
    pass

  def eat1(self):
    ''' 食物を食べる処理 '''
    print(self.food_taken1+"を食べました")

hito1 = Human()
hito1.take1("Banana")
hito1.eat1()
# -> Bananaを食べました

# <<<クラスを使わなかった場合>>>
def search2(place):
  ''' 周りを見る処理 '''
  pass

def take2(food):
  ''' 物をつかむ処理 '''
  food_taken2 = food

def open_mouth2():
  ''' 口を開ける処理 '''
  pass

def eat2():
  ''' 食物を食べる処理 '''
  print(food_taken2+"を食べました")

take2("Banana")
eat2()
# -> NameError: name 'food_taken2' is not definedというエラーが出る。