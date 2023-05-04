from RPG import RPG

player=['none' for i in range(10)]
player[0]='=='
player[1]=RPG(1,'咪咪',50,1000,50,'睡覺')
player[2]=RPG(2,'李三',100,1,10000,'嘲諷')
player[3]=RPG(3,'楊翔順',300,20,1000,'撞擊')
print(f'共有{RPG.getCount()}個英雄')
while True:
    user=int(input('''
                   1.查看英雄
                   2.編輯英雄
                   3.新增英雄
                   4.exit
                   '''))
    if user==1:
        user=int(input('輸入英雄代號'))
        player[user].introduce()
    elif user==2:
        heroid=int(input('輸入英雄代號'))
        user=int(input('''
                       1:改名
                       2:改攻擊
                       3:改防禦
                       4:改血量
                       5:改技能
                       6:exit
                       '''))
        if user==1:
            player[heroid].name=input('新名子')
            print(f'名子已更改:{player[heroid].name}')
        elif user==2:
            player[heroid].attack=input('新攻擊')
            print(f'攻擊已更改:{player[heroid].attack}')
        elif user==3:
            player[heroid].defense=input('新防禦')
            print(f'防禦已更改:{player[heroid].defense}')
        elif user==4:
            player[heroid].blood=input('新血量')
            print(f'血量已更改:{player[heroid].blood}')
        elif user==5:
            player[heroid].skill=input('新技能')
            print(f'技能已更改:{player[heroid].skill}')
        else:break
    elif user==3:
        for i in range(10):
            if player[i]=='none':
                print(f'編號:{i}')
                player[i]=RPG(i,input('名子:'),input('攻擊:'),input('防禦:'),input('血量:'),input('技能:'))
                print(f'共有{RPG.getCount()}個英雄')
                break
    else:break