class Student:
    def check_pass_fail(self,name,marks):
        if marks<33:
            return name,"Fail in the exam"
        else:
            return name,"Pass in the exam"

student1=Student()
fail_OR_pass=student1.check_pass_fail('Mehedi Hasan Nirob',75)
print(fail_OR_pass)
fail_OR_pass=student1.check_pass_fail('Nirob',12)
print(fail_OR_pass)