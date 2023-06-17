class Student:
    def check_pass_fail(self):
        if self.mark <33:
            return "Fail in the exam"
        else:
            return "Pass in the exam"

    def __init__(self,name,marks):
        self.name=name
        self.mark=marks

student1=Student("Nirob",75)
fail_or_pass=student1.check_pass_fail()
print(student1.name,fail_or_pass)

student1=Student("Mehedi",31)
fail_or_pass=student1.check_pass_fail()
print(student1.name,fail_or_pass)