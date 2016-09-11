from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from .models import *

# 首页
# 1，增加任务
# 2,列出所有的任务task_content
def home(request):

    # 获取所有的任务,按照倒序排列
    task_list = Task.objects.all().order_by('created').reverse()

    # 增加一个任务
    if request.method == 'POST':
        task = request.POST
        if task['content']:
            Task.objects.create(
                content= task['content'],
                status= 0,
            )

    return render(request,'index.html',locals())

# 编辑某个任务
def edit(request,id):

    # from form import TaskForm
    # form = TaskForm()
    if request.method == 'POST':
        # content = u"修改的内容,已经修改了"
        if id:
            content = request.POST["content"]
            Task.objects.filter(id=id).update(content=content)
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    return render(request,'index.html',locals())

# 删除某个任务
def delete(request,id):
    if id:
        Task.objects.filter(id=id).delete()
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')

# 完成某个任务
def finish(request,id):
    if id:
        Task.objects.filter(id=id).update(status=1)
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')

# 取消完成某个任务
def unfinish(request,id):
    if id:
        Task.objects.filter(id=id).update(status=0)
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')