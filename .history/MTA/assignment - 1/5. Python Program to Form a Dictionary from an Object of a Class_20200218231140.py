class person():
    nationality = "indian"

    def __init__(self,name,college):            #constructor
        self.name = name
        self.college = college
        print("my name is",self.name,"& my college is",self.college)
        
    def __init__(self,age,rollno):
        print("my age is",age,"& my college is",rollno)
        
    
    obj1 = person("arihant","bpibs")
    obj1 = person(22,12312)