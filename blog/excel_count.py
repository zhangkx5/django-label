import xlrd
from blog import models

def open_and_read_excel(request):
    File = request.FILES.get("excel_file", None)
    excel = xlrd.open_workbook("./label_files/%s" % File.name)
    sheet = excel.sheets()[0]
    nrows = sheet.nrows

    for i in range(0, nrows):
        name = sheet.cell_value(i, 0)
        label = sheet.cell_value(i, 1)
        num = sheet.cell_value(i, 2)
        sum = sheet.cell_value(i, 3)
        models.ExcelCount.objects.create(name=name, label=label, num=num, sum=sum)

    list = models.ExcelCount.objects.all()

    return list