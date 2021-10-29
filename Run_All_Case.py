import pytest
import allure
import os,shutil
from common.send_Email import send_mail
import traceback
from common.log import Logger
try:
    if os.path.isdir(r"D:\pythonProject\pcclient_UI\result\allure-report"):
        shutil.rmtree(r"D:\pythonProject\pcclient_UI\result\allure-report")
    pytest.main(["-s","-q",r"D:\pythonProject\pcclient_UI\testCase","--alluredir",r"D:\pythonProject\pcclient_UI\result\allure-report"])
#os.system("pytest -s -q D:/pythonProject/pcclient_UI/testCase --alluredir  D:/pythonProject/pcclient_UI/resultallure-report")

    os.system("allure generate D:/pythonProject\pcclient_UI/result/allure-report -o D:/pythonProject/pcclient_UI/result/allure-report-html --clean")
except Exception as E:
    message=traceback.format_exc()
    Logger("error").get_logger().debug(message)

#content="无需回复，本次测试报告如下：</br>"+open(r"D:\pythonProject\pcclient_UI\result\allure-report-html\index.html","r",encoding="utf-8").read()

#send_mail(r"D:\pythonProject\pcclient_UI\result\allure-report-html\index.html",content)
