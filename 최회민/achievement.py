import configparser
from datetime import datetime
class Achievement():
    def __init__(self):
        self.cf= configparser.ConfigParser()
        self.cf.read('achievement.ini')
        
        self.singleWin=self.cf['singleWin']
        self.storyAWin=self.cf['storyAWin']
        self.storyBWin=self.cf['storyBWin']
        self.storyCWin=self.cf['storyCWin']
        self.storyDWin=self.cf['storyDWin']
        self.in10Turn=self.cf['in10Turn']
        self.notUseSkill=self.cf['notUseSkill']
    def setSingleWin(self):
        self.singleWin=True
        self.cf.set('singleWin','achieve', "True")
        today=self.getToday()
        self.cf.set('singleWin','time', today)        
        with open('achievement.ini','w') as change:
            self.cf.write(change)
        self.singleWin=self.cf['singleWin']
            
    def setStoryAWin(self):
        self.cf.set('storyAWin','achieve', "True")
        today=self.getToday()
        self.cf.set('storyAWin','time', today)        
        with open('achievement.ini','w') as change:
            self.cf.write(change)       
        self.storyAWin=self.cf['storyAWin']
             
    def setStoryBWin(self):
        self.cf.set('storyBWin','achieve', "True")
        today=self.getToday()
        self.cf.set('storyBWin','time', today)
        with open('achievement.ini','w') as change:
            self.cf.write(change)      
        self.storyBWin=self.cf['storyBWin']
              
    def setStoryCWin(self):
        self.cf.set('storyCWin','achieve', "True")
        today=self.getToday()
        self.cf.set('storyCWin','time', today)
        with open('achievement.ini','w') as change:
            self.cf.write(change)     
        self.storyCWin=self.cf['storyCWin']
              
    def setStoryDWin(self):
        self.cf.set('storyDWin','achieve', "True")
        today=self.getToday()
        self.cf.set('storyDWin','time', today)
        with open('achievement.ini','w') as change:
            self.cf.write(change)    
        self.storyDWin=self.cf['storyDWin']
        
    def setIn10Turn(self):
        self.cf.set('in10Turn','achieve', "True")
        today=self.getToday()
        self.cf.set('in10Turn','time', today)
        with open('achievement.ini','w') as change:
            self.cf.write(change)    
        self.in10Turn=self.cf['in10Turn']
        
    def setNotUseSkill(self):
        self.cf.set('notUseSkill','achieve', "True")
        today=self.getToday()
        self.cf.set('notUseSkill','time', today)
        with open('achievement.ini','w') as change:
            self.cf.write(change)        
        self.notUseSkill=self.cf['notUseSkill']

    def getSingleWin(self):
        return self.singleWin
    
    def getStoryAWin(self):
        return self.storyAWin
    
    def getStoryBWin(self):
        return self.storyBWin

    def getStoryCWin(self):
        return self.storyCWin

    def getStoryDWin(self):
        return self.storyDWin
    
    def getIn10Turn(self):
        return self.in10Turn
    
    def getNotUseSkil(self):
        return self.notUseSkill
    
    def getToday(self):
        now = datetime.now()
        today = str(now.month) + '.' + str(now.day)
        return today
        
    