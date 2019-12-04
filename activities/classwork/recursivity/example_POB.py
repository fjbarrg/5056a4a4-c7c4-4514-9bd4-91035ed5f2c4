import json


class SchoolMember:
    ROLE = ""

    def __init__(self,name,age,role=""):
        self.name = name
        self.age = age
        self.role = role if role else self.ROLE

    def get_info(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

    def get_role(self):
        if not self.ROLE:
            raise NotImplementedError{"Cannot get role from abstract model"}
        else:
            print(self.ROLE)

    @staticmethod
    def from_dict(dictionary):
        role = dictionary.get("role")
        if role == Student.ROLE:
            return Student(**dictionary)
        elif role== Professor.ROLE:
            return Professor(**dictionary)
        else:
            raise ValueError("Invalid role.")

    def to_dict(selfself):
        return{
            "name": self.name,
            "age": self.age
            "role": self.role
        }

class Student(SchoolMember):
    ROLE = "Student"


class Professor(SchoolMember):
    ROLE = "Professor"



school_member = SchoolMember(name = "A", age= 22)
    # Acceder a las variables
school_member..get_info()
school_member.name


student_a = Student(name= "student a", age=23)
student_a.get_role()

school_member_dictionary= {
    "name": "A",
    "age": 21,
    "role": "Professor"
}

a= SchoolMember.from_dict(school_member_dictionary)
a.age
a.name
