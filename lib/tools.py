import  unittest
import glob
from conf import setting
import BeautifulReport as  br
import  time
import os

def create_py():
    with open(setting.CASE_TEMPLATE,encoding='utf-8') as fr : #读取CASE_TEMPLATE文件
        src_content= fr.read()

    all_yaml =glob.glob(setting.DATA_PATH + os.sep +'*.yaml')
    for file in all_yaml:
        class_name = os.path.split(file)[-1].replace('.yaml','').title()
        py_content = src_content % (class_name, file)
        py_path =os.path.join(setting.CASE_PATH,class_name.lower()+'.py') #cases目录下创建python文件
        open(py_path,'w',encoding='utf-8').write(py_content) #向cases目录下的python文件中写入内容


def run_all_case():
    test_suite =unittest.TestSuite()
    all_py = unittest.defaultTestLoader.discover(setting.CASE_PATH,'*.py')
    [test_suite.addTest(case) for case in all_py]
    report =br.BeautifulReport(test_suite)
    title = '%s_测试报告' %time.strftime('%Y_%m_%d_%H_%M_%s')
    report.report(title,title,setting.REPORT_PATH) #title 为测试报告的名称
    return report.filename,report.success_count,report.failure_count