class Dog():

    def __init__(self,name,type,toys):
        self.name = name
        self.type = type
        self.toys= toys

    def introduce(self):
        print("這是"+self.name+"，我最喜歡的品種之一-"+self.type+"，牠最喜歡玩的玩具是"+self.toys+"。")

    def bark(self, content):
        print("他們常對我"+ content +"")


    @classmethod
    def Husky(cls):
        return cls("Jack","Husky","socks")

    @classmethod
    def GoldenRetriever(cls):
        return cls("Browny","Golden retriever","ball")
    

Husky = Dog.Husky()
Maltese = Dog.GoldenRetriever()

Husky.introduce()
Maltese.introduce()

Gizmo = Dog("Gizmo","Maltese","rope")
Gizmo.introduce()
Gizmo.bark("BARK!")