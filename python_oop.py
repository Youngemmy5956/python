string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class
    
    from abc import ABC,   
class ClassName(ABC):
    pass