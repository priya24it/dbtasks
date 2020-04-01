import unittest
import HtmlTestRunner
import email.utils
import pandas as pd

class Execution(unittest.TestCase):

    def test_function_one(self):
        print("test_function_one execute.")
        self.assertEqual(1, 1, "test_function_one.")

    def test_function_two(self):
        print("test_fun.")
        self.assertNotEqual(1, 2, "test_function_two.")

    def test_CountValidationTesting(self):
        print("test_function_one execute.")
        dfexcel1 = pd.read_excel("Res10.xlsx",sheet_name="MDMMAP_Tables")
        df1 = pd.DataFrame(dfexcel1)
        l2 = df1['Count'].values.tolist()
        l1 = df1['TargetCount'].values.tolist()
        Testcase = df1['Testcase'].values.tolist()
        for i in range(len(l1)):
            with self.subTest(i=i):
                self.assertEqual(l2[i], l1[i], Testcase[i]+':'+str(l2[i]))


html_report_dir = './html_report'
xml_report_dir = './xml_report'
# Run all test function and generate html report.
def run_all_test_generate_xml_report():
 # Run all test functions with HtmlTestRunner to generate html test report.
 testReport = unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=xml_report_dir))
 #testReport = unittest.main(testRunner=xmlrunner.XMLTestRunner(output=xml_report_dir))
 print("Test Report Name" + testReport)


if __name__ == '__main__':
     testReport = run_all_test_generate_xml_report()
     print("Test Report Name" + testReport)



