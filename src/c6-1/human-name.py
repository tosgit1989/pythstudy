class HumanName:
  ''' 人を表すクラス '''
  def setName(self, name):
    ''' 名前を設定するメソッド '''
    self.name = name

  def getName(self):
    ''' 名前を取得するメソッド '''
    return self.name

taro = HumanName()
taro.setName("Taro")
print(taro.getName())

jiro = HumanName()
jiro.setName("Jiro")
print(jiro.getName())
print(jiro.name)