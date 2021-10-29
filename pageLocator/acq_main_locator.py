from common.get_Connect import Login
from common.baseCom import base_Com
class Acq_Main_Locator():
    def __init__(self,path,yaml_page_path,yaml_input_path,name,name_path):

        self.acqHandle=Login(yaml_page_path,yaml_input_path).get_acq_connect(name,name_path)

        self.BaseCom=base_Com
        self.yamlData=self.BaseCom().open_yaml(path)
    def Patientname(self):
        #定位姓名输入框
        patientname=self.acqHandle.window(best_match=self.yamlData["check"]["name"])
        return patientname

    def Age(self):
        #定位年龄输入框
        years=self.acqHandle.window(best_match=self.yamlData["check"]["age"])
        return years

    def Save_And_Check(self):
        #定位保存并采集按钮
        save_and_check=self.acqHandle.child_window(title=self.yamlData["check"]["saveAndCheck"],control_type=self.yamlData["check"]["saveAndCheck_Type"])
        return save_and_check
    def Apply(self):
        #定位申请诊断按钮
        apply_btu=self.acqHandle.child_window(auto_id=self.yamlData["picture_report"]["apply"],class_name=self.yamlData["picture_report"]["apply_class"])
        return apply_btu
    def Ok_Btu(self):
        #定位申请诊断的确认按钮
        Btu_ok=self.acqHandle.child_window(auto_id=self.yamlData["picture_report"]["PART_OkButton"],control_type=self.yamlData["picture_report"]["PART_OkButton_type"])
        return Btu_ok
    def Return_Btu(self):
        #定位返回主页面的返回按钮
        re_btu=self.acqHandle.child_window(title=self.yamlData["picture_report"]["return"],control_type=self.yamlData["picture_report"]["return_type"])
        return re_btu

    def Checked(self):
        #定位返回已检查按钮
        chencked=self.acqHandle.child_window(title=self.yamlData["check"]["checked"],control_type=self.yamlData["check"]["checked_type"])
        return chencked

    def Diagnosed(self):
        #定位返回待诊断数据
        diagnosed=self.acqHandle.child_window(best_match=self.yamlData["check"]["diagnosed_father"]).child_window(title=self.yamlData["check"]["diagnosed_title"], control_type=self.yamlData["check"]["diagnosed_type"])
        return diagnosed
    def get_scrren(self):
        Image_Sceern=self.BaseCom().get_scrren_save(self.acqHandle)
        return Image_Sceern

if __name__=="__main__":
    path=r"D:\pythonProject\pcclient_UI\testData\pageData\acqMain_Page_Data.yaml"
    yaml_page_path=r"D:\pythonProject\pcclient_UI\testData\pageData\loginData.yaml"
    yaml_input_path=r"D:\pythonProject\pcclient_UI\testData\inputData\login_input_data"
    name="Aquarium.Ecg.Client.Shell.exe"
    name_path=r"D:/NLEMR/RestingECG"
    Acq_Main_Locator(path,yaml_page_path, yaml_input_path, name,  name_path).Patientname()


