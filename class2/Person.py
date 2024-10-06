class Person():

    def __init__(self,eyeColor, hairColor):
        self.eyeColor = eyeColor
        self.hairColor = hairColor

    @classmethod
    def American(cls):
        return cls("blue","brown")

    @classmethod
    def Taiwanese(cls):
        return cls("black","black")
    
American = Person.American()
Taiwanese = Person.Taiwanese()

American.introduce()
Taiwanese.introduce()