class person():
    country = "India"

    def __init__(self,name,college,age,rollno):                                 #constructor
        self.name = name                                                        #name, college (on RHS) r object(instance) variables
        self.college = college
        print("my name is",self.name,"& my college is",self.college)     #self.'name', self.'college' r cls variables with no predfined value
        print("my age is",age,"& my rollno. is",rollno)                         #age, rollno r object(instance) variables
        
    def fn1(self,msg):
        print(msg,"\nI'm from",self.country)                             #self.'country' is an object(instance) variable with predfined value
        
    def fn2(self):
        x=input("\nenter ur name:\t")
        y=input("enter ur college name:\t")
        print("ur name is",x,"& ur college is",y)
        
        z=input("\nenter ur country name:\t")
        if z!=self.country:
            
            outsiders[x]=z
        print(outsiders)
        
        with open('list.json','w') as f:                  #creates json file on hdd(same folder) if not exist already and open it internally
        json.dump(outsiders,f)
        
        
obj1 = person("rocky","mit",22,12312)
obj1.fn1("hello everyone!")
obj1.fn2()