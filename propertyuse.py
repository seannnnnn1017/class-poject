class CStudent:
    
    def __init__(self,a):
        self.__a=a


    @property
    def a(self):
        return 
    @a.setter
    def seta(self,newa):
        self.__a=newa
    @a.getter
    def geta(self):
        return self.__a

OP=CStudent(('S109102345', '張三', 'IECS', 'zs100232@gmail.com', '2000-02-02'))
print(OP.geta)