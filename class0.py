class CStudent:
    
    def __init__(self):
        self.__a=('S109102345', '張三', 'IECS', 'zs100232@gmail.com', '2000-02-02')

    @property
    def a(self):
        return 'No Data'
    @a.setter
    def seta(self,newa):
        self.__a=newa
    @a.getter
    def geta(self):
        return self.__a

OP=CStudent()
print(OP.geta)