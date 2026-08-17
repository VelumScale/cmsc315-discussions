"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""



from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Employee: # Employee class
    position = "General Staff"  # Class variable

    def __init__(self, name, department):
        self.name = name
        self.department = department

    # displays object info 
    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}, Position: {self.position}")






# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.


class Executive(Employee): #child class 
    clearence_level = "High"  # New class variable

    def __init__(self, name, department, salary, c_bounes):
        super().__init__(name, department)
        self.salary = salary 
        self.curruption_bounes = c_bounes #joke veriable 
        self.nepobaby = [] # Mutable attrebute

    # show public info
    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}, Position: {self.position}, Salary: {self.salary}, Clearence Level: {self.clearence_level}")

    # shows secret info
    def display_secret_info(self):
        print(f"Curruption Bounes: {self.curruption_bounes} Nepo babies:")
        for i in self.nepobaby:
            print(i.name)

    # adds a nep baby 
    def add_nepobaby(self,object):
        self.nepobaby.append(object)

    # Deletes a nepobaby 
    def del_nepobaby(self,object):
        print("Remove nepobaby:")
        #ask for user input
        nepo_baby_name = str(input())

        for i in self.nepobaby:

            if i.name == nepo_baby_name:
                self.nepobaby.remove(i)
        
                


    


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.


def demonstrate_namespaces():

    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    # Declareing two objects of the child class
    exec_bob = Executive("Bob", "Finance", 120000, 5000)
    exec_alice = Executive("Alice", "HR", 110000, 3000)

    #Access class variable through the class itself
    Executive.clearence_level = "Medium" 

    #Access the same class veriable throught the object 
    exec_bob.clearence_level = "low"

    # adding an attibute to bob
    exec_bob.city = "New York" #disples where bob is located

    # Display each object's namespace using __dict__
    print(exec_bob.__dict__)
    print(exec_alice.__dict__)
    print()

    # Display class namespace
    print(Executive.__dict__)
    print()


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    ## Create an object that contains a mutable data
    exec_tom = Executive("tom","IT", 150000, 4000)
    henry = Employee("Henry","IT")
    gary = Employee("Henry","IT")

    #adding henry and gary to toms nepobaby list
    exec_tom.add_nepobaby(henry)
    exec_tom.add_nepobaby(gary)

    #Create a shallow copy 
    nepo_list_shallow = copy(exec_tom.nepobaby)

    # Create a deep copy
    nepo_list_deep = deepcopy(exec_tom.nepobaby)

    # modifyng the original data
    exec_tom.nepobaby[0].department = "HR"

    #Display the original object, shallow copy, and deep copy.
    #this is the orginal object that containts the mutible data 
    print(f"this is the original object list: {exec_tom.nepobaby} \n")

    #A shallow copy is a new object, that refrences the nested data thaat is shared with the origial object 
    print(f"this is a shallow copy of said list: {nepo_list_shallow} \n")

    #A deep copy is a new object that doesn't refrence the original. this means the nested data is also copyed and not shared 
    print(f"this is a deep copy of said list: {nepo_list_deep}")


    
# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")

    # creating a employe object the parent class
    tony = Employee("Tony","HR")   


    #calling methods from the parent class (employee)
    print(tony.display_info())
    print()



    print("\nTODO: Create and test your child object")

    #creating an exsecutive object from the child class
    tonys_boss_henry = Executive("Henry","HR", 150000, 5000)

    #calling methods from the child class (exsecutive)
    tonys_boss_henry.display_info()
    tonys_boss_henry.display_secret_info()
    print()



    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()