import json
import unittest
import sys

sys.path.append("./")
from common.configHttp import runMain
import testFile.getUrlParams as getUrlParams
import urllib.parse
import paramunittest

import testFile.readExcel as readExcel

url = getUrlParams.getUrlParams().get_Url()
login_xls = readExcel.readExcel().get_xls("userCase.xlsx", "login")


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def test01case(self):
        self.checkResult()

    def checkResult(self):
        # url1 = "http://www.xxx.com/login?"
        # new_url = url1 + self.query
        # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        data1 = dict(urllib.parse.parse_qsl(self.query))
        info = runMain().run_main(self.method, url, data1)
        ss = json.loads(info)
        if self.case_name == "login":
            assert ss["code"] == 200
        if self.case_name == "login_error":
            assert ss["code"] == -1
        if self.case_name == "login_null":
            assert ss["code"] == 10001


if __name__ == "__main__":
    unittest.main
