class CompanyDataBean:
    ''' This is a bean class of a company, this holds company name, price, month & year'''
    def __init__(self,name,value=0,month=None,year=0):
        self.name=name
        self.value=int(value)
        self.month=month
        self.year=int(year)
    def __gt__(self,value):
        ''' The greater than(>) operator is overloaded here'''
        return (int(value) > self.value) 
    def __str__(self):
        ''' The string representation of this class object'''
        return "Company Name : %8s ShareValue : %5s  Month/Year : %2s/%3d" % (self.name, self.value, self.month,self.year)
