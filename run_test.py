import os
import time
import unittest
import HTMLTestRunner


current_path=os.path.dirname(__file__)
report_path=os.path.join( current_path,'report')

cases_path=os.path.join( current_path,'TestCase')
html_path=os.path.join( report_path,'report_%s.html'%time.strftime('%Y_%m_%d_%H_%M_%S'))

discover=unittest.defaultTestLoader.discover(start_dir=cases_path,
                                             pattern='*_case.py',
                                             top_level_dir=cases_path)
# 主套件 所有的测试用例
main_suite=unittest.TestSuite()
main_suite.addTest( discover )

file=open(html_path,'wb')
html_runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                          title='C2C的自动化测试',
                                          description='回归测试')

html_runner.run(main_suite)


# if __name__=="__main__":
#     suite01=unittest.TestLoader().loadTestsFromTestCase(test_case.SendStatus)
#     unittest.main(defaultTest='suite01')