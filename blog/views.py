from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.excel_count import open_and_read_excel
from blog.models import BlogsPost

def blog_index(request):
    blog_list = BlogsPost.objects.all()
    return render(request, "index.html", {'blog_list':blog_list})

def label_count(request):
    if request.method == 'POST':
        File = request.FILES.get("excel_file", None)
        if File is None:
            return HttpResponse("请选择需要上传的monkey日志文件")
        else:
            with open("./label_files/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            return render(request, "query.html", {"excel_data": open_and_read_excel(request).all})
    else:
        return render(request, "query.html")
