import unittest
import nnreport
test_suite =unittest.TestCase()
test_suite.addTest(unittest,makeSuite(s))

report =nnreport.BeautifulReport(test_suite)
report.report(description='报告描述',filename='文件名称.html')