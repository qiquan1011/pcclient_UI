
from pywinauto.application import Application
import os
import time

import psutil
from common.get_randon_name import random_name
from common.get_Num import get_num
from pywinauto.keyboard import send_keys
from pywinauto import mouse
import shutil
patient_Name=random_name()
yearold=get_num()
def get_connect(name):
    '''
    判断程序是否打开
    否：打开程序，建立连接
    是：建立连接
    复制dat文件进行数据采集
    :param name: 启动exe文件名字
    :return:
    '''
    os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    name_path=r"D:/NLEMR/RestingECG"
    start_cmd='d: & cd '+name_path+' & start '+name
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
                you_name_app=Application(backend="uia").connect(process=you_path_pid)
                time.sleep(2)
                username = you_name_app.window(title="心电采集客户端").child_window(auto_id="UserSelc")
                username.type_keys("qdrjc")
                time.sleep(1)
                password = you_name_app.window(title="心电采集客户端").child_window(auto_id="PasswordBox")
                password.type_keys("123456")
                send_keys("^a")
                password.type_keys("123456")
                btnlogin = you_name_app.window(title="心电采集客户端").child_window(title="登   录", control_type="Button")
                btnlogin.click()

    else:
        you_name_app=Application(backend="uia").connect(process=you_path_pid)



    #a=you_name_app.window(title="心电检查客户端").print_control_identifiers()
    #print(a)
    time.sleep(2)

    c=you_name_app.window(title_re=u"心电检查客户端",class_name="Window")
    # 姓名框定位,并输入姓名
    patientname=c.window(best_match="姓名Edit")
    #patientname.wait("exists ready",timeout = 5,retry_interval = 3)
    patient_Name = random_name()
    patientname.type_keys(patient_Name)
    #年龄框定位，并输入年龄
    years=c.window(best_match="年龄Edit")
    #years.wait(wait_for="exists ready", timeout = 5, retry_interval = 3)
    yearold = get_num()
    years.type_keys(yearold)
    #保存采集
    save_and_check=c.child_window(title="保存并采集",auto_id="", control_type="Button")
    save_and_check.click()
    time.sleep(5)#等待采集程序启动
    if os.path.exists(r"D:\DCMDATA\check_data.dat"):  # 如果文件存在,删除文件
        os.remove(r"D:\DCMDATA\check_data.dat")
    shutil.copy2(r"D:\Dat采集文件\check_data.dat", r"D:\DCMDATA")#复制dat文件
    time.sleep(10)#等待上传
    #申请诊断
    b=c.child_window(auto_id="menuMore",class_name="Button")
    b.click()
    mouse.move(coords=(1800,951))
    mouse.click(button='left', coords=(1800,951))
    a=c.child_window(title="确定", auto_id="PART_OkButton", control_type="Button")
    a.click()
    time.sleep(4)
    #返回主页
    e = c.child_window(title="返 回", control_type="Button")
    e.click()
    time.sleep(1)
    #关闭应用
    c.close()

if __name__=="__main__":
    get_connect("Aquarium.Ecg.Client.Shell.exe")