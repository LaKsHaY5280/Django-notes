import random
from .models import *
from faker import Faker
fake = Faker()

def seed_db(n=10)->None:
    try:
        for _ in range (1,n):

            name = fake.name()
            age = fake.random_int(min=18,max=25)
            email = fake.email()
            
            dep_objs = Department.objects.all()
            randi = random.randint(0,len(dep_objs)-1)
            department = dep_objs[randi]
            
            student_id = fake.random_int(min=100,max=999)
            stuid_obj = StudentID.objects.create(student_id=student_id)
            
            print(name,age,email,department,student_id)
            student = Student.objects.create(name=name,age=age,email=email,department=department,student_id=stuid_obj)
            student.save()
    except Exception as e:
        print(f"An error occurred: {e}")
