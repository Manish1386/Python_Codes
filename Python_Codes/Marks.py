class Students:
    def __init__(self, name):
        self.name=name
        self.marks=[]

    def enterMarks(self):
        for i in range(3):
            m=int(input("Enter marks of %s in subject %d: " %(self.name, i+1)))
            self.marks.append(m)

    def display(self):
        print(self.name," got ", self.marks)

s1=Students("Anisha")
s1.enterMarks()

s2=Students("Jignesh")
s2.enterMarks()

s1.display()
s2.display()