class Dog:
    def __init__(self, name, age):
        #print("Constructor ran")
        self.name = name
        self.age = age
test = Dog("Leila", 9)
test1 = Dog("Polo", 5)
print(test.name,test.age)
print(test1.name,test1.age)