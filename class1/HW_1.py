class Dog():

    def __init__(self,name,type,toys):
        self.name = name
        self.type = type
        self.toys= toys

    def introduce(self):
        print("這是"+self.name+"，我最喜歡的品種-"+self.type+"，牠最喜歡玩的玩具是"+self.toys+"。")

    def bark(self, content):
        print("他常對我"+ content +"")

Gizmo = Dog("Gizmo","馬爾濟斯","繩子")
Gizmo.introduce()
Gizmo.bark("BARK!")