"""
使用openpyxl实现以下需求

使用excel 写入一组数据，姓名，身高，体重
计算是否为健康体重，如果是健康体重，则在旁边备注健康，并将姓名打印出来
健康体重计算公式：（身高cm-70）×60%
(可以做一部分优化)
"""

from openpyxl import Workbook, load_workbook

class PracticeExcel:

    wb = Workbook()
    ws1 = wb.active
    ws1.title = "create"
    ws1["A1"] = "姓名"
    ws1["B1"] = "身高"
    ws1["C1"] = "体重"
    ws1["D1"] = "备注"
    name = ["dong", "fang", "shen", "qi"]
    data_dict1 = {"dong": 180, "fang": 160, "shen": 170, "qi": 155}
    data_keys1 = [i for i in data_dict1.keys()]
    data_dict2 = {data_dict1[data_keys1[0]]: 66, data_dict1[data_keys1[1]]: 51, data_dict1[data_keys1[2]]: 60, data_dict1[data_keys1[3]]: 81}
    data_keys2 = [i for i in data_dict2.keys()]

    for i in range(len(name)):
        ws1.cell(row=i + 2, column=1).value = data_keys1[i]
        ws1.cell(row=i + 2, column=2).value = data_keys2[i]
        ws1.cell(row=i + 2, column=3).value = data_dict2[data_keys2[i]]

    wb.save("data.xlsx")

    def health_data(self):
        ld = load_workbook(filename="data.xlsx")
        sheet = ld["create"]

        for i in range(4):
            height = sheet.cell(row=i + 2, column=2).value
            weight = sheet.cell(row=i + 2, column=3).value

            health_weight = (height - 70) * 0.6
            if weight == health_weight:
                print("这是健康的体重", weight)
                sheet.cell(row=i + 2, column=4).value = "健康体重"
        ld.save(filename="data.xlsx")

pe = PracticeExcel()
pe.health_data()
