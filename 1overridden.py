class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):  # Method is overridden
        return "Hello from Child"

obj = Child()
print(obj.greet())  # Output: Hello from Child

#came to know it is principles of object oriented programing 
#Inheritence / generalization 
