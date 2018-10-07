from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.
from blog.excel_count import open_and_read_excel
from blog.models import BlogsPost
from release_query.query import open_and_query_excel

def blog_index(request):
    blog_list = BlogsPost.objects.all()
    return render(request, "index.html", {'blog_list':blog_list})

def label_count(request):
    if request.method == 'POST':
        File = request.FILES.get("excel_file", None)
        #File = request.POST.get("excel_file", None)
        if File is None:
            return HttpResponse("请选择需要上传的monkey日志文件")
        else:
            with open("./label_files/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            template = "query.html"
            data = open_and_read_excel(request).all
            return render(request, template, {"excel_data": data})
    else:
        return render(request, "query.html")

def release_result(request):
    if request.method == 'POST':
        File = request.FILES.get("excel_file", None)
        if File is not None:
            with open("./label_files/release.xlsx", 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)

    df = pd.read_excel("./label_files/release.xlsx", usecols=[0, 1, 2, 12])
    nrows = len(df)
    result_plan = []
    result_unrelease = []
    result_release = []
    object = open_and_query_excel(request)
    for i in range(0, nrows):
        row = list(df.ix[i])
        result_plan.append(row)
        flag = 0
        for obj in object:
            if str(row[3]) == str(obj['label']):
                flag = 1
                result_release.append(row)
                break
        if flag == 0:
            result_unrelease.append(row)

    template = "release.html"
    return_data = {"result_plan": result_plan,"result_unrelease":result_unrelease,"result_release":result_release}
    return render(request, template, return_data)
