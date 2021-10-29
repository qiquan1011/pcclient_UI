from pageLocator.acq_main_locator import Acq_Main_Locator
import shutil
from pywinauto import mouse
import time
import os
from common.log import Logger
import traceback,sys
from common.baseCom import base_Com
class Acq_Main_Object():
    def __init__(self,path,yaml_page_path,yaml_input_path,name,name_path):
        self.acq=Acq_Main_Locator(path,yaml_page_path,yaml_input_path,name,name_path)
        self.Base_Com=base_Com()
        self.randonName=self.Base_Com.random_name()
        self.rangeAge=self.Base_Com.get_num()
        #self.Image_handle=self.Base_Com.get_scrren_save(self.acq)
    def acq_check(self,Image_path):
        #病人姓名
        try:
            patient_name=self.acq.Patientname()
            patient_name.type_keys(self.randonName)
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)

        #病人年龄
        try:
            patient_age=self.acq.Age()
            patient_age.type_keys(self.rangeAge)
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)
        #保存并采集
        try:
            save_And_check=self.acq.Save_And_Check()
            save_And_check.click()
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)
        time.sleep(5) #等待采集程序启动
        #复制采集的文件
        if os.path.exists(r"D:\DCMDATA\check_data.dat"):
            os.remove(r"D:\DCMDATA\check_data.dat")
        shutil.copy2(r"D:\Dat采集文件\check_data.dat", r"D:\DCMDATA")
        time.sleep(10)#等待文件上传
        #更多按钮
        try:
            apply_btu=self.acq.Apply()
            apply_btu.click()
        #模拟鼠标点击申请诊断
            mouse.move(coords=(1800,951))
            mouse.click(button="left",coords=(1800,951))
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)
        #申请诊断确认按钮
        try:
            Btu_ok=self.acq.Ok_Btu()
            Btu_ok.click()
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)
        time.sleep(1)
        try:
            if os.path.exists(Image_path):
                os.remove(Image_path)
            image=self.acq.get_scrren()
            image.save(Image_path)
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)
        time.sleep(3)
        #返回主页面操作
        try:
            re_btu=self.acq.Return_Btu()
            re_btu.click()
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)

        try:
            checked=self.acq.Checked()
            checked.click()
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)

        try:
            diagnosed=self.acq.Diagnosed()
            diagnosed_text=diagnosed.window_text()
            print(diagnosed_text)
            return diagnosed_text
        except Exception as e:
            message = traceback.format_exc()
            Logger("error").get_logger().debug(message)
        

if __name__=="__main__":
    path = r"D:\pythonProject\pcclient_UI\testData\pageData\acqMain_Page_Data.yaml"
    yaml_page_path = r"D:\pythonProject\pcclient_UI\testData\pageData\loginData.yaml"
    yaml_input_path = r"D:\pythonProject\pcclient_UI\testData\inputData\login_input_data"
    name = "Aquarium.Ecg.Client.Shell.exe"
    name_path = r"D:/NLEMR/RestingECG"
    Acq_Main_Object(path,yaml_page_path,yaml_input_path,name,name_path).acq_check()

