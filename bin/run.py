from  lib import tools
#import sys,os
#sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    tools.create_py()
    file_name,success_count,fail_count = tools.run_all_case()
    print(file_name,success_count,fail_count)

main()