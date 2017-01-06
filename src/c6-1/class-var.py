class Cat:
    nakigoe = "nya-"
    def naku(self):
        # 次の行を、print(Cat.nakigoe)より変更
        print(self.nakigoe)

mike = Cat()
mike.naku()

nora = Cat()
nora.naku()

mike.nakigoe = "myu-"

nora.naku()
mike.naku()