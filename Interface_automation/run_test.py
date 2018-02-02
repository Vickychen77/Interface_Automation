import sys
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
sys.path.append('./interface')
sys.path.append('./db_fixture')

test_dir=os.path.dirname(__file__)+'/interface'
print(test_dir)

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__=='__main__':
    now_time=time.strftime('%Y-%m-%d_%H_%M_%S')
    filename= os.path.dirname(__file__)+'/report/'+'result_'+now_time+'_test_report.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='Test Report',
                          description='test for practice')
    runner.run(discover)
    fp.close()





