def Ecryption(data):
    EcryptionData=''
    for i in data:
        EcryptionData+=chr(ord(i)+10)
    return EcryptionData

def Decryption(data):
    DecryptionData=''
    for i in data:
        DecryptionData+=chr(ord(i)-10)
    return DecryptionData

datalist=[]
while True:
    user=input("""
               1=加密
               2=解密 datalist
               0=離開並查看
               """)
    if user =='1':
        a=Ecryption(input('g=輸入data'))
        print(a)
        datalist.append(a)
    elif user=='2':
        for i in datalist:
            print(Decryption(i))
    elif user=='0':break
print(datalist)
        
