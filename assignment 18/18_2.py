# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

# 1km=1000m
# 1m=100cm


class Distance:

    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm

    def __add__(self,other):

        m=self.cm + other.cm
        m= m // 100
        self.cm = m % 100
        m = self.m + other.m + m
        km= m // 1000
        self.m= m % 1000
        self.km=self.km + other.km + km 

        return self

    def __sub__(self,other):

        if self.km > other.km or self.m > other.m or self.cm > other.cm  :
           
            cm=self.cm - other.cm
            m= cm // 100
            self.cm = cm % 100
            m = self.m - other.m  + m
            km= m // 1000
            self.m= m % 1000
            self.km=(self.km - other.km) + km 

            return self
        else:
            cm=self.cm - other.cm
            m= cm // 100
            self.cm = cm % 100
            m = self.m - other.m  + m
            km= m // 1000
            self.m= m % 1000
            self.km=(self.km - other.km) + km 
            
            return self


    def __str__(self):
        
        return f'kiloeter :{self.km}\nMeter :{self.m}\nCentimeter :{self.cm}'


obj1=Distance(10,1000,100)

obj2=Distance(10,1000,20)

obj3=Distance(1,100,100)

print(obj1+obj2)