import xlrd

# 读取excel表格
def read_excel(filename):
    workbook=xlrd.open_workbook(filename)
    sheet=workbook.sheet_by_index(0)

    #双列表形式 ，一行一个用例
    all_case_info = []
    for i in range(1,sheet.nrows):
        case_info=[]
        for j in range(sheet.ncols):
            case_info.append(sheet.cell_value(i,j))
        all_case_info.append(case_info)   #注意，python以对齐来确定循环的所定义区域
    return all_case_info


print(read_excel(r"C:\Users\Administrator\Desktop\data\data.xlsx")[0])