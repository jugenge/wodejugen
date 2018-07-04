from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from  ..models import Orders
def index(request):
    #  找到所有订单
    orderlist = Orders.objects.all()

    # 导入分页类
    from django.core.paginator import Paginator
    # 实例化分页对象,参数1,数据集合,参数2 每页显示条数
    paginator = Paginator(orderlist, 10)
    # 获取当前页码数
    p = request.GET.get('p',1)
    # 获取当前页的数据
    orderlist = paginator.page(p)

    return render(request,'myadmin/order/list.html',{"orderlist":orderlist})

def edit(request):
    
    if request.method == "GET":

        orderid = request.GET.get("orderid",None)
        order = Orders.objects.get(id = orderid)

        return render(request,"myadmin/order/edit.html",{"order":order})
    elif request.method == "POST":
        pass