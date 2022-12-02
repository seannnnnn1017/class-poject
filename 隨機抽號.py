def RD(x,y):
    import random
    a=random.randint(x,y+1)
    list1.append(a)
    print(a)
list1=[]
while True:
    user=input("""
               1=隨機抽數
               2=查看
               0=離開並查看
               """)
    if user =='1':RD(int(input('頭')),int(input('尾')))
    elif user=='2':print(list1)
    elif user=='0':break