import configparser

class Configset:
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read('settings.ini')
        
    def getDefault(self): # 기본 설정 불러올 때 사용
        return self.cf['DEFAULT']['WIN_WIDTH'], self.cf['DEFAULT']['WIN_HEIGHT'], self.cf['DEFAULT']['COLOR_BLIND_MODE']
    def getChange(self): # 저장된 설정 불러올 때 사용
        return self.cf['CHANGE']['WIN_WIDTH'], self.cf['CHANGE']['WIN_HEIGHT'], self.cf['CHANGE']['COLOR_BLIND_MODE']
    
    def setWidth(self,width):
        str_width=str(width)
        self.cf.set('CHANGE','WIN_WIDTH',str_width)
    def setHeight(self,height):
        str_height=str(height)
        self.cf.set('CHANGE','WIN_HEIGHT',str_height)   
    def setColorBindMode(self,check):
        str_check=str(check)
        self.cf.set('CHANGE','COLOR_BLIND_MODE',str_check)
    def save(self): # 설정 값 변경 후 파일에 저장
        with open('settings.ini','w') as configfile:
            self.cf.write(configfile)
    
    # 키 설정 관련 코드 추가 작성