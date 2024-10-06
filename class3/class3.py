# ==================================================封裝Encapsulation==============================================================
class Student:
    def __init__(self, name):
        self.__name = name
        self.__score = {"Math": 0, "Physics": 0, "Chemistry": 0}
    # 私有方法
    def __add_subject(self, subject):
        self.__score[subject] = 0
    # 公有方法
    def set_score(self, subject, score):
        if subject not in self.__score:
            self.__add_subject(subject)
        self.__score[subject] = 0

    def get_subject(self):
        for key in self.__score:
            print(key, " : ", self.__score[key])

yeet = Student("yee")
yeet.set_score("Chinese", 100)
yeet.get_subject()

# ==================================================封裝Encapsulation==============================================================

# ==================================================繼承Inheritance================================================================

class Person:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.__ID = ID
    def speak(self, sentence):
        return self.name + "says" + sentence
    
class Athlete(Person):

    def __init__(self, name, age, ID, height    ):
        super().__init__(name, age, ID)
        self.height = height

    def speak(self, sentence):
        print("Athelete", super().speak(sentence))
        
    def workout(self):
        return "%s goes to the gym to exercise." % (self.name)

# ==================================================繼承Inheritance================================================================