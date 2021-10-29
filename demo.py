from pywinauto.application import Application
import os
import time
import  uiautomation
import psutil
def get_connect(name):
    '''
    判断程序是否打开
    否：打开程序，建立连接
    是：建立连接
    :param name: 启动exe文件名字
    :return:
    '''
    os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    name_path= "D:/NLEMR/aECG-One"
    start_cmd='d: & cd '+name_path+' & start Galaxy.Gemini.Shell.exe'
    you_path_pid=None
    for i in psutil.pids():
        p=psutil.Process(i)
        if str(p.name())==name:
            you_path_pid=i
    if you_path_pid is None:
        os.system(start_cmd)
        p2=psutil.process_iter()
        for j in p2:
            if j.name()==name:
                you_path_pid=j.pid
                you_name_app=Application(backend = "uia").connect(process = you_path_pid)
                time.sleep(1)
                username = you_name_app.window(auto_id = "Login").child_window(auto_id = "CboUserName")
                username.type_keys("qdrsh")
                time.sleep(1)
                password = you_name_app.window(auto_id ="Login").child_window(auto_id ="TxtPwd")
                password.type_keys("123456")
                time.sleep(1)
                BtnLogin = you_name_app.window(auto_id = "Login").child_window(auto_id = "BtnLogin")
                BtnLogin.click()
    else:
        you_name_app=Application(backend = "uia").connect(process = you_path_pid)
    time.sleep(3)
    d=you_name_app.window_(title_re=u"心电医生工作站",class_name="WindowsForms10.Window.8.app.0.1983833_r6_ad1")
    patientname=d.child_window(auto_id="BePatientName", control_type="Edit")
    #patientname.wait(wait_for="exists ready",timeout=5,retry_interval=3)
    patientname.type_keys("朱瑾瑜")
    search=d.child_window(auto_id="BtnSearch", control_type="Button")
    search.click()
    time.sleep(2)
    b=d.child_window(title="受理", control_type="Button")
    b.click()
    d.close()
    return you_name_app

if __name__=="__main__":
    get_connect("Galaxy.Gemini.Shell.exe")