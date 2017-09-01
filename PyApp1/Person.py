#no interfaces 
#no private or protected 

class Person():
   def __init__(self, name, age):
    self.person_name = name
    self.person_age = age
   
   def __str__ (self):
       return "Name: "+ self.person_name + " Age: "+ str(self.person_age)


class Employee(Person):
    def __init__(self,id,person):
        self.id = id
        self.person_age = person.person_age
        self.person_name = person.person_name

    def __str__(self):
       return  str(Person(self.person_name,self.person_age)) + " Id:"+str(self.id)


person = Person("Kunal",32)
employee = Employee(105,person)
print(employee)


