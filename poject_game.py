import time
import random
class RPG:
    def __init__(self,number,name,attack,defense,blood,skill,skilltime,acurracy,critical) -> None:
        self.number=number
        self.name=name
        self.attack=attack
        self.defense=defense
        self.blood=blood
        self.skill=skill
        self.skilltime=skilltime
        self.acurracy=acurracy
        self.critical=critical
    def introduce(self):
        print(f"""
              =======================
              {self.name}  NO.{self.number}
              =======================
              攻擊:{self.attack}
              防禦:{self.defense}
              血量:{self.blood}
              =======================
              技能:{self.skill}
              技能時間:{self.skilltime}
              =======================
              """)
def skill(skill_name,playnum):
    global p1blood
    global p2blood
    global p1time
    global p2time
    global damage
    if playnum == 1:
        if skill_name == "睡覺":
            print('使用 睡覺',"+5")
            p1blood += 5
            p1time =5
        elif skill_name =="撞擊":
            print('使用 撞擊',"傷害上升100%")
            damage*=2
            p1time =3
    elif playnum == 2:
        if skill_name == "睡覺":
            print('使用 睡覺',"血量+5")
            p2blood += 5
            p2time =5
        elif skill_name =="撞擊":
            print('使用 撞擊',"傷害上升100%")
            damage*=2
            p2time =3
            

        

    


def PVP(play1:RPG,play2:RPG):

    global p1blood
    global p2blood
    global p1time
    global p2time
    global damage
    
    count=1
    
    p1blood=play1.blood
    p2blood=play2.blood
    damage=0
    p1time=0
    p2time=0
    playnumber1=1
    playnumber2=2
    print(f"""
              =======================                         
              {play1.name}  NO.{play1.number}                 
              =======================                         
              攻擊:{play1.attack}                             
              防禦:{play1.defense}                     
              血量:{play1.blood}                              
              =======================                         
              技能:{play1.skill}                              
              技能時間:{play1.skilltime}                      
              =======================     
                        VS
              =======================                         
              {play2.name}  NO.{play2.number}                 
              =======================                         
              攻擊:{play2.attack}                             
              防禦:{play2.defense}                     
              血量:{play2.blood}                              
              =======================                         
              技能:{play2.skill}                              
              技能時間:{play2.skilltime}                      
              =======================                        
          """)
    while p1blood >0 or p2blood >0:
        damage=0
        chance=random.randint(1,101)

        if chance<=play1.acurracy: #命中率
            damage=(play1.attack)*10/((play2.defense))
            chance=random.randint(1,101)
            if chance <= play1.critical:damage*=2 #爆擊率
        if p1time==0: #技能
            skill(play1.skill,playnumber1)
        p2blood-=damage
        print(f'==============================================第{count}回合==============================================')
        count+=1
        print(f"""  {play1.name}的回合
              {play1.name}對{play2.name}造成{damage}傷害
              =======================                         
              {play1.name}  NO.{play1.number}                 
              =======================                         
              攻擊:{play1.attack}                             
              防禦:{play1.defense}                     
              血量:{p1blood}    
              技能冷卻:{p1time}      
              ======================= 
                     V    S
              =======================                         
              {play2.name}  NO.{play2.number}                 
              =======================                         
              攻擊:{play2.attack}                             
              防禦:{play2.defense}                     
              血量:{p2blood}      
              技能冷卻:{p2time}     
              =======================
                                      
              """)
        a=input("")
        if p1blood <=0 or p2blood <=0:
            break
        damage=0
        chance=random.randint(1,101)
        
        if chance<=play2.acurracy: #命中率
            damage=(play2.attack)*10/((play1.defense)) 
            chance=random.randint(1,101)
            if chance <= play2.critical:damage*=2 #爆擊
        if p2time==0:  #技能
            skill(play2.skill,playnumber2)
        p1blood-=damage
        
        print(f"""  {play2.name}的回合
              {play2.name}對{play1.name}造成{damage}傷害
              =======================                         
              {play1.name}  NO.{play1.number}                 
              =======================                         
              攻擊:{play1.attack}                             
              防禦:{play1.defense}                     
              血量:{p1blood} 
              技能冷卻:{p1time}     
              ======================= 
                     V    S
              =======================                         
              {play2.name}  NO.{play2.number}                 
              =======================                         
              攻擊:{play2.attack}                             
              防禦:{play2.defense}                     
              血量:{p2blood}   
              技能冷卻:{p2time}        
              =======================
              """)
        a=input("")
        if p1blood <=0 or p2blood <=0:
            break
        if p1time>0:p1time-=1
        if p2time>0:p2time-=1
    if p1blood<=0:
        print(f'{play2.name}WIN')
    else:
        print(f'{play1.name}WIN')
player=['none' for i in range(10)]
player[1]=RPG(1,'咪咪',50,1000,50,'睡覺',2,100,20)
player[2]=RPG(2,'李三',100,1,10000,'嘲諷',3,75,50)
player[3]=RPG(3,'楊翔順',300,20,1000,'撞擊',4,40,60)
PVP(player[1],player[3])