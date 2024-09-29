class Person():

    def __init__(self,name,age,favoriteFood):
        self.name = name
        self.age = age
        self.favoriteFood = favoriteFood

    def introduce(self):
        print("我是"+self.name+"，我今年"+str(self.age)+"歲，最喜歡吃"+self.favoriteFood+"。")

    def shout(self, content):
        print("我大喊:「"+ content +"」")

Amy = Person("Amy",15,"apple")
Amy.introduce()
Amy.shout("我討厭看牙醫")