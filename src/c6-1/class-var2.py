class Cat:
    nakigoe = "nya-"
    def naku(self):
        print(Cat.nakigoe)

mike = Cat()
mike.naku()

nora = Cat()
nora.naku()

Cat.nakigoe = "myu-"

nora.naku()
mike.naku()