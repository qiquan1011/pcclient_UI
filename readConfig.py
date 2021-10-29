import os
import configparser
class read_config():
    def __init__(self):
        #获取权柄
        self.curret_path=os.path.abspath(__file__)
        self.father_path=os.path.abspath(os.path.dirname(self.curret_path))
        self.config_path=os.path.join(self.father_path,"config.ini")
        self.cf=configparser.ConfigParser()
        self.cf.read(self.config_path)

    def get_Email(self,name):
        '''
        读取，并返回Email信息
        :param name:
        :return:
        '''
        get_value=self.cf.get("Email",name)
        return get_value

if __name__=="__main__":
    read_config().get_Email("sendmail")