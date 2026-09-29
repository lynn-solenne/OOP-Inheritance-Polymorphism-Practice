#Hospital Staff Management- Hierarchical inheritance+super()+Polymorphism
class Staff:
    def __init__(self,name,staff_id):
        self.name=name
        self.staff_id=staff_id
    def work(self):
        print(f"{self.name} is working.")
class Doctor(Staff):
    def __init__(self,name,staff_id,specialization):
        super().__init__(name,staff_id)
        self.specialization=specialization
    def work(self):
        print(f"Dr. {self.name} is examining patients.")
class Nurse(Staff):
    def __init__(self,name,staff_id,ward):
        super().__init__(name,staff_id)
        self.ward=ward
    def work(self):
        print(f"Nurse {self.name} is caring for patients.")
class Receptionist(Staff):
    def __init__(self,name,staff_id,shift):
        super().__init__(name,staff_id)
        self.shift=shift
    def work(self):
        print(f"{self.name} is managing appointments.")
doctor=Doctor("Sara","Sf12345","Neurology")
nurse=Nurse("Ali","Sf45678","ICU")
receptionist=Receptionist("Mia","Sf12378","Morning")
staff_member=[doctor,nurse,receptionist]
for staff in staff_member:
    staff.work()

