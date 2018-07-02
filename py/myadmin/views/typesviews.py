from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .. models import Types

# Create your views here.



def gettypesorder():
    # 获取所有的分类信息
    # tlist = Types.objects.all()

    # select * ,concat(path,id)as paths from myadmin_types order by paths;
    tlist = Types.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')

    for x in tlist:
        if x.pid == 0:
            x.pname = '顶级分类'
        else:
            t = Types.objects.get(id=x.pid)
            x.pname = t.name
        num = x.path.count(',')-1
        x.name = (num*'<--->')+x.name

    return tlist
    


    
def add(request):
    if request.method == 'GET':
        # 返回一个添加的页面
        tlist = gettypesorder()

        context = {'tlist':tlist}

        return render(request,'myadmin/types/add.html',context)

    elif request.method == 'POST':
        # 执行分类的添加
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        if ob.pid == '0':
            ob.path = '0,'
        else:
            # 根据当前父级id获取path,再添加当前父级id
            t = Types.objects.get(id=ob.pid)
            ob.path = t.path+str(ob.pid)+','
        ob.save()

        return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_types_list')+'"</script>')



def index(request):
    
    tlist = gettypesorder()

    context = {'tlist':tlist}

    return render(request,'myadmin/types/list.html',context)




def delete(request):
    tid = request.GET.get('uid',None)
    print(tid)
    # 判断当前类下是否有子类
    num = Types.objects.filter(pid=tid).count()
    # print(num)
    if num != 0:
        data = {'msg':'当前类下有子类,不能删除','code':1}

    else:
        # 判断当前类下是否有商品
        ob = Types.objects.get(id=tid)
        ob.delete()
        data = {'msg':'删除成功','code':0}

    return JsonResponse(data)





def edit(request):
    # 显示修改和执行修改
    
    
    # 获取对象
    # ob = Goods.objects.get(id=uid)

    if request.method == 'GET':
        # 接收参数

        uid = request.GET.get('uid',None)
        print(uid)
        ob = Types.objects.filter()
        ob = ob.order_by('path')

        for x in ob:
            num = x.path.count(',')-1
            x.name = (num*'<--->')+x.name
        # 分配数据
        context = {'tlist':ob}
        # 显示编辑页面
        return render(request,'myadmin/types/edit.html',context)
        
    if request.method == 'POST':
        
        # uid = request.POST.get('uid',None)
        
        # name = request.POST.get('name',None)
        # print(uid,type(uid))
        # ob = Types.objects.get(id = uid)

        # ob.name = name
        # ob.path = ob.path
        # ob.pid = ob.pid

        # ob.save()

        return HttpResponse('<script>alert("修改成功");location.href="'+reverse('myadmin_types_list')+'"</script>')
        # except:
        #     return HttpResponse('<script>alert("修改失败");location.href="'+reverse('myadmin_goods_edit')+'?uid='+str(ob.id)+'"</script>')




