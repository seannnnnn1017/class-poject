class RPG:
    objcount=0
    def __init__(self,number,name,attack,defense,blood,skill) -> None:
        self.__number=number
        self.__name=name
        self.__attack=attack
        self.__defense=defense
        self.__blood=blood
        self.skill=skill
        RPG.objcountadd()
    @staticmethod
    def objcountadd():
        RPG.objcount+=1
    @staticmethod
    def getCount():
        return RPG.objcount
    
    
    @property
    def name():
        return 'none'
    @name.setter
    def name(self,new):
        self.__name=new
    @name.getter
    def name(self):
        return self.__name
    
    @property
    def attack():
        return 'none'
    @attack.setter
    def attack(self,new):
        self.__attack=new
    @attack.getter
    def attack(self):
        return self.__attack

    @property
    def defense():
        return 'none'
    @defense.setter
    def defense(self,new):
        self.__defense=new
    @defense.getter
    def defense(self):
        return self.__defense
    
    @property
    def blood():
        return 'none'
    @blood.setter
    def blood(self,new):
        self.__blood=new
    @blood.getter
    def blood(self):
        return self.__blood
    
    @property
    def skill():
        return 'none'
    @skill.setter
    def skill(self,new):
        self.__skill=new
    @skill.getter
    def skill(self):
        return self.__skill
    
    def introduce(self):
        print(f"""
              =======================
              {self.__name}  NO.{self.__number}
              =======================
              攻擊:{self.__attack}
              防禦:{self.__defense}
              血量:{self.__blood}
              =======================
              技能:{self.skill}
              =======================
              """)
    
        
