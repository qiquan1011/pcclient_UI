from pageObject.acq_main_object import Acq_Main_Object
from common.log import Logger
import pytest,allure
import traceback
from common.get_excel import get_excel

def setup_function():
    pass
try:
    @allure.feature("test_01")
    @pytest.mark.parametrize(*get_excel().get_sheetNames("Sheet1"))
    def test_01(case_name,path,yaml_page_data,yaml_input_data,name,name_path,Image_path):

        diagnosed_text=Acq_Main_Object(path,yaml_page_data,yaml_input_data,name,name_path).acq_check(Image_path)
        assert diagnosed_text=="待诊断"
    @allure.feature("test_02")
    def test_02():
        assert 1==2

    @allure.feature("test_03")
    def test_03():
        assert 1==1
except Exception as e:
    message=traceback.format_exc()
    Logger("ERROR").get_logger().debug(message)
def teardown_function(self):
    pass

if __name__=="__main__":
    pytest.main([("test_check_report.py"),("-sv")])