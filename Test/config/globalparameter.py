import time,os

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#配置文件
config_file_path = project_path + '\\config\config.ini'

#chromedriver
chrome_driver_path = project_path + '\\driver\\chromedriver.exe'

#excel测试数据
test_data_path = project_path + "\\testdata\\testDaate.xlxs"

#日志
log_path = project_path + "\\logs\logs.log"

#测试报告
report_path = project_path + "\\report\\"
report_name = report_path + time.strftime('%Y%m%d%H%S',time.localtime())

#异常截图
img_path = project_path+"\\error_img\\"+time.strftime('%Y%m%d%H%S', time.localtime())

#测试用例
test_case_path = project_path + "\\testcase"