class Student:
    def get(self,rlno,name,totalmark):
        self.rlno=rlno
        self.name=name
        self.totalmark=totalmark
    def disp(self):
        print(f"roll no:{self.rlno}")
        print(f"name:{self.name}")
        print(f"total mark:{self.totalmark}")
stud1=Student()
stud1.get(101,"alice",65)
stud1.disp()
