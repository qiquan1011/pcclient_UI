import json
import os
import xlrd



class get_excel():
    def __init__(self):
        self.cls=[]
        self.curret_path=os.path.abspath(__file__)

        self.father_path=os.path.abspath(os.path.dirname(self.curret_path))

        self.father_path2=os.path.abspath(os.path.dirname(self.father_path))

        self.path=os.path.join(self.father_path2,"testFile","testSource.xlsx")

        print(self.path)

    def get_sheetNames(self,sheet_name):
        data=xlrd.open_workbook(self.path)
        sheet=data.sheet_by_name(sheet_name)
        nrows=sheet.nrows
        for j in range(nrows):
            if sheet.row_values(j)[0]!= u"case_name":
                self.cls.append(sheet.row_values(j))

                parm_data=','.join(sheet.row_values(0))
                #print(self.cls)

                return parm_data,self.cls

if __name__=="__main__":
    k=get_excel().get_sheetNames(sheet_name="Sheet1")



