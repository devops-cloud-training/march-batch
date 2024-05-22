# what is object ?
# what is object oriented programming
# what is class ?

# class - blueprint of an object which will defined in a generic way
# object - an instance of a class with its own behaviour and attributes

# class Vehicle:
#     # attributes
#     vehicle_name = ""
#     wheels = 0
#     max_speed = 0

#     # behaviours 

#     def pressBrakes(self):
#         print("Pressed brake")

#     def soundHorn(self):
#         print("pom! pom! pom!")
    
#     def start_engine(self):
#         print("Engine started")

# car = Vehicle()
# car.vehicle_name = "volkswagen taigun"
# car.wheels = 4
# car.max_speed = 150

# print("Car: ",car.vehicle_name)
# print("no of wheels: ", car.wheels)
# print("Max speed: ", car.max_speed)
# car.start_engine()
# car.soundHorn()
# car.pressBrakes()


# bus = Vehicle()
# bus.vehicle_name = "ashok layland"
# bus.wheels = 6
# bus.max_speed = 100

# print("Car: ",bus.vehicle_name)
# print("no of wheels: ", bus.wheels)
# print("Max speed: ", bus.max_speed)
# bus.start_engine()
# bus.soundHorn()
# bus.pressBrakes()


# class Birds:
#     name ="some species"
#     age = 2

#     def __init__(self, bird_name, bird_age=10):
#         self.name = bird_name
#         self.age = bird_age
#         print("The object is created and the values are set")

#     def fly(self):
#         print(f"I'm a bird and my name is {self.name}, and I can fly")

# bird1 = Birds("Parrot",2)

# # print(bird1.name)
# # print(bird1.age)
# bird1.fly()

# bird2 = Birds("Peacock")

# print(bird1.name)
# print(bird1.age)
# bird2.fly()

# inheritance, polymorphism

class Person():
    name = ""
    age =""
    gender = ""
    govd_id = ""

    def __init__(self, person_name, person_age, person_gender, person_id):
        self.name = person_name
        self.age = person_age
        self.gender = person_gender
        self.govd_id = person_id
    
    def display_your_id(self):
        print("My name is: ",self.name)
        print("My age is ",self.age)
        print("I'm a ", self.gender)
        print("My govt id is ",self.govd_id)

class Employee(Person):

    salary = 0
    designation = ""

    def __init__(self, emp_name, emp_age, emp_gender, emp_govtid, emp_salary, emp_designation):
        self.salary = emp_salary
        self.designation = emp_designation
        Person.__init__(self, emp_name, emp_age, emp_gender, emp_govtid)

    def display_your_id(self):
        super().display_your_id()
        #Person.disploy_your_id()
        # print("My name is: ",self.name)
        # print("My age is ",self.age)
        # print("I'm a ", self.gender)
        # print("My govt id is ",self.govd_id)
        print("My salary is",self.salary)
        print("My designation is,",self.designation)

employee1 = Employee("sathish",16,"male",12345,900000000,"Architect")
employee1.display_your_id()

employee2 = Employee("visualpath",30,"male",9876,100000,"Engineer")
employee2.display_your_id()