import logging
import os
import datetime
log_path=os.getcwd()
#print(log_path)
class Logger:
    def __init__(self,name):
        log_path=os.path.dirname(os.getcwd())
        resultPath=os.path.join(log_path,"result")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.datetime.now().strftime("%Y%m%d")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger=logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        fh=logging.FileHandler(os.path.join(logPath,"outlog.log"),encoding="utf-8")
        fh.setLevel(logging.DEBUG)

        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger

if __name__=="__main__":
    t = Logger("hmk").get_logger().debug("User %s is loging" % 'jeck')