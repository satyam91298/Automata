class Student:
    def details(self,name,marks) :
        self.name=name
        print("Name:",name)
        for i in range(len(marks)) :
            print("Subject",i,"=",marks[i])
name=input("Enter Name\n")
st=[]
for i in range(3) :
    stt=int(input("Enter marks"))
    st.append(stt)
s=Student()
s.details(name,st)
r=Student()
name1=input("Enter name\n")
l=[]
for i in range(3) :
    stt=int(input("Enter marks"))
    l.append(stt)
    r.details(name,l)
