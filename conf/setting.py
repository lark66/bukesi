import  os
#程序主目录
#os.path.abspath()  #取得当前目录
#os.path.dirname() #取得当前目录的上一级目录
#os.path.join()   #目录拼接
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH =os.path.join(BASE_PATH,'data')
CASE_PATH = os.path.join(BASE_PATH,'cases')
LOG_PATH =os.path.join(BASE_PATH,'logs')
REPORT_PATH = os.path.join(BASE_PATH,'report')
CASE_TEMPLATE =os.path.join(BASE_PATH,'conf','case_template')

print(DATA_PATH)
print(CASE_PATH)
print(CASE_TEMPLATE)
print(BASE_PATH)