
class CStudent:
    objcount=0
    def __init__(self,id,name,department,Email,birthday):
       self.__id=id
       self.__name=name
       self.__department=department
       self.__Email=Email
       self.__birthday=birthday
       CStudent.objcountadd()
       CStudent
    @staticmethod
    def objcountadd():
        CStudent.objcount+=1
        print(f'Total {CStudent.objcount} student')
    @staticmethod
    def getobjcount():
        return CStudent.objcount
    @property
    def id(self):
        return 'None'
    @id.setter
    def setid(self,newid):
        self.__id=newid
    @id.getter
    def getid(self):
        return self.__id

    @property
    def name(self):
        return 'None'
    @name.setter
    def setname(self,newname):
        self.__name=newname
    @name.getter
    def getname(self):
        return self.__name         

    @property
    def department(self):
        return 'None'
    @department.setter
    def setdepartment(self,newdepartment):
        self.__department=newdepartment
    @department.getter
    def getdepartment(self):
        return self.__department   

    @property
    def Email(self):
        return 'None'
    @Email.setter
    def setEmail(self,newEmail):
        self.__Email=newEmail
    @Email.getter
    def getEmail(self):
        return self.__Email 

    @property
    def birthday(self):
        return 'None'
    @birthday.setter
    def setbirthday(self,newbirthday):
        self.__birthday=newbirthday
    @birthday.getter
    def getbirthday(self):
        return self.__birthday    

studentlist=[0 for i in range(5)] 
studentlist[0]=CStudent('S109102345','張三','IECS', 'zs100232@gmail.com', '2000-02-02')
studentlist[1]=CStudent('S109104533','李四','IECS', 'ktr002222@gmail.com', '2004-03-22')
studentlist[2]=CStudent('S109123346','王五','EE', 'zs1543232@gmail.com', '1999-04-22')
studentlist[3]=CStudent('S109102355','趙雲','CE', 'zkkse0252@gmail.com', '2001-05-10')
studentlist[4]=CStudent('S109102785','李白','AI', 'zsf23s3d@gmail.com', '2002-06-04')
while True:
    student=input("""
               ------------------------
               輸入學生代號(0,1,2,3,4)
               leave=離開
               ------------------------
               """)
    if student=='leave':break
    else:
        while True:
            user=input('''
                ------------------------
                    1=查看資料
                    2=進入修改介面
                    leave=離開
                ------------------------
                    ''')
            if user=='leave':break
            elif user=='1':print(
                studentlist[int(student)].getid,
                studentlist[int(student)].getname,
                studentlist[int(student)].getdepartment,
                studentlist[int(student)].getEmail,
                studentlist[int(student)].getbirthday,
                                )
            elif user=='2':
                seter=input('''
                ------------------------
                0=修改id
                1=修改name
                2=修改department
                3=修改Email
                4=修改birthday
                leave=離開
                ------------------------
                            ''')
                if seter=='leave':break
                if seter=='0':
                    new=input('新資料')
                    studentlist[int(student)].setid=new
                elif seter=='1':
                    new=input('新資料')
                    studentlist[int(student)].setname=new
                elif seter=='2':
                    new=input('新資料')
                    studentlist[int(student)].setdepartment=new
                elif seter=='3':
                    new=input('新資料')
                    studentlist[int(student)].setEmail=new
                elif seter=='4':
                    new=input('新資料')
                    studentlist[int(student)].setbirthday=new