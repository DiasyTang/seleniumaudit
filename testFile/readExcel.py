import os
import sys

sys.path.append("./")
from testFile import getPathInfo
from xlrd import open_workbook

path = getPathInfo.get_Path()


class readExcel:
    def get_xls(self, xls_name, sheet_name):
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, "case", xls_name)
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u"case_name":
                cls.append(sheet.row_values(i))
        return cls


if __name__ == "__main__":
    print(readExcel().get_xls("userCase.xlsx", "login"))
    print(readExcel().get_xls("userCase.xlsx", "login")[0][1])
    print(readExcel().get_xls("userCase.xlsx", "login")[1][2])

