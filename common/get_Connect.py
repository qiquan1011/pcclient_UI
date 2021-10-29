import os,psutil,time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from common.baseCom import base_Com
import PIL
import os
class Login():
    def __init__(self,yaml_page_path,yaml_input_path):
        '''
        初始化读取yaml文件
        :param yaml_page_path:页面元素数据路径
        :param yaml_input_path: 输入页面数据路径
        '''
        self.yaml_page_data = base_Com().open_yaml(yaml_page_path)
        self.yaml_input_data = base_Com().open_yaml(yaml_input_path)

    def get_acq_connect(self,name,name_path):
        '''

     实现检查端登录
    :param name:进程名称
    :param name_path: 应用程序位置

    :return: 窗口句柄
        '''

        os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    #name_path=r"D:/NLEMR/RestingECG"
        start_cmd='d: & cd '+name_path+' & start '+name
        you_path_pid=None
        for i in psutil.pids():
            p=psutil.Process(i)
            if str(p.name())==name:
                you_path_pid=i
        if you_path_pid is None:
            os.system(start_cmd)
            pid=psutil.process_iter()
            for j in pid:
                if j.name()==name:
                    you_path_pid=j.pid
                    you_name_app=Application(backend="uia").connect(process=you_path_pid)
                    acq_login_handle=you_name_app.window(title=self.yaml_page_data["acqLogin"]["login_name"])
                    username = acq_login_handle.child_window(auto_id=self.yaml_page_data["acqLogin"]["username"])
                    username.type_keys(self.yaml_input_data["acqlogin"]["user"])
                    password = acq_login_handle.child_window(auto_id=self.yaml_page_data["acqLogin"]["password"])
                    password.type_keys(self.yaml_input_data["acqlogin"]["pass"])
                    send_keys("^a")
                    password.type_keys(self.yaml_input_data["acqlogin"]["pass"])
                    btnlogin = acq_login_handle.child_window(title=self.yaml_page_data["acqLogin"]["loginBtn"],control_type=self.yaml_page_data["acqLogin"]["control_type"])
                    btnlogin.click()
                    acq_handle=you_name_app.window(title_re=self.yaml_page_data["acqLogin"]["name"],control_type=self.yaml_page_data["acqLogin"]["name_class"])
                    time.sleep(2)
                    acq_handle.capture_as_image().save(r"D:\pythonProject\pcclient_UI\testFile\登录成功.png")

        else:
            you_name_app=Application(backend="uia").connect(process=you_path_pid)
            acq_handle = you_name_app.window(title_re=self.yaml_page_data["acqLogin"]["name"],control_type=self.yaml_page_data["acqLogin"]["name_class"])
        return acq_handle
    def get_ggh_connect(self,name,name_path):
        '''
        诊断端登录
        :param name:进程名称
        :param name_path: 应用程序启动文件
        :return: 窗口句柄
        '''
        os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
        #name_path = "D:/NLEMR/aECG-One"
        start_cmd = 'd: & cd ' + name_path + ' & start '+name
        you_path_pid = None
        for i in psutil.pids():
            p = psutil.Process(i)
            if str(p.name()) == name:
                you_path_pid = i
        if you_path_pid is None:
            os.system(start_cmd)
            p2 = psutil.process_iter()
            for j in p2:
                if j.name() == name:
                    you_path_pid = j.pid
                    you_name_app = Application(backend="uia").connect(process=you_path_pid)
                    ggh_handle=you_name_app.window(auto_id=self.yaml_page_data["gghLogin"]["name"])
                    username = ggh_handle.child_window(auto_id=self.yaml_page_data["gghLogin"]["username"])
                    username.type_keys(self.yaml_input_data["gghlogin"]["user"])
                    #time.sleep(1)
                    password = ggh_handle.child_window(auto_id=self.yaml_page_data["gghLogin"]["password"])
                    password.type_keys(self.yaml_input_data["gghlogin"]["pass"])
                    time.sleep(1)
                    BtnLogin = ggh_handle.child_window(auto_id=self.yaml_page_data["gghLogin"]["BtnLogin"])
                    BtnLogin.click()
                    time.sleep(4)
                    ggh_other_handle = you_name_app.window(title=self.yaml_page_data["gghLogin"]["login_name"],class_name=self.yaml_page_data["gghLogin"]["login_name_class"])
                    #ggh_other_handle=you_name_app.child_window(title="心电医生工作站", auto_id="ShellView", control_type="Window")
                    if os.path.exists(r"D:\pythonProject\pcclient_UI\testFile\screenshot\诊断端登录成功.png"):
                        os.remove(r"D:\pythonProject\pcclient_UI\testFile\screenshot\诊断端登录成功.png")
                    a=ggh_other_handle.capture_as_image()
                    a.save(r"D:\pythonProject\pcclient_UI\testFile\screenshot\诊断端登录成功.png")
        else:
            you_name_app = Application(backend="uia").connect(process=you_path_pid)
            ggh_handle = you_name_app.window(title=self.yaml_page_data["gghLogin"]["login_name"],class_name=self.yaml_page_data["gghLogin"]["login_name_class"])
            
            if os.path.exists(r"D:\pythonProject\pcclient_UI\testFile\screenshot\诊断端登录成功.png"):
                os.remove(r"D:\pythonProject\pcclient_UI\testFile\screenshot\诊断端登录成功.png")
            a=ggh_handle.capture_as_image()
            a.save(r"D:\pythonProject\pcclient_UI\testFile\screenshot\诊断端登录成功.png")
            print("保存成功")
            
        return ggh_handle
if __name__=="__main__":
    #name="Aquarium.Ecg.Client.Shell.exe"
    name = "Galaxy.Gemini.Shell.exe"
    #name_path=r"D:/NLEMR/RestingECG"
    name_path=r"D:/NLEMR/aECG-One"
    yaml_page_path=r"D:\pythonProject\pcclient_UI\testData\pageData\loginData.yaml"
    yaml_input_path=r"D:\pythonProject\pcclient_UI\testData\inputData\login_input_data"
    #Login(yaml_page_path,yaml_input_path).get_acq_connect(name,name_path)
    Login(yaml_page_path,yaml_input_path).get_ggh_connect(name,name_path)