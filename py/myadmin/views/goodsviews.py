from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse

from . typesviews import gettypesorder
from . userviews import uploads

from ..models import Goods,Types
import time
# Create your views here.
def add(request):
    if request.method == 'GET':
        tlist = gettypesorder()
        context = {'tlist':tlist}

        context['info'] = '<table class="standard-table" width="1239" style="width: 679px;"><tbody><tr class="standard-table-group firstRow" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">基础信息</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">品牌</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">魅族</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">型号</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">魅蓝6T</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">尺寸</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">152.3*73*8.4mm</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">电池容量</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">3300mAh</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">重量</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">145g</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">屏幕</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">屏幕尺寸</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">5.7英寸</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">对比度</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">1000:1</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">分辨率</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">1440x720</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">PPI</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">282</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">亮度</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">450cd/m²（典型值）</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">容量</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">运行内存（RAM）</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">3GB/4GB</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">机身内存</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">32GB<br/>64GB</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">处理器</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">CPU</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">MT6750 八核处理器</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">GPU</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">ARM Mali-T860 图形处理器</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">CPU频率</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">ARM®&nbsp;Cortex®-A53™ 1.5 GHz x4 +<br/>ARM® Cortex®-A53™ 1.0GHz x4</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">摄像</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">前置摄像头</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">800万像素<br/>ƒ/2.0 光圈<br/>4 片式镜头<br/>ArcSoft® 美颜算法 自适应美肤技术<br/>Face AE 自动人脸识别 亮度增强</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">后置摄像头</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">1300 万像素 200 万像素<br/>PDAF 相位对焦 自动对焦系统<br/>人像背景虚化模式<br/>ƒ/2.2 光圈 ƒ/2.4 光圈<br/>5片式镜头 3片式镜头<br/>连拍模式<br/>全景模式<br/>后置闪光灯 补光自然柔和</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">mTouch</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">响应速度</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">0.2s</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">识别角度</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">360°</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">指纹组数</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">5组</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">mTouch传感器</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">电容式触摸传感器</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">运营商与制式</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">全网通</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">全网通（公开版）<br/>移动 4G TD-LTE<br/>联通/电信 4G TD/FDD-LTE<br/>移动 3G TD-SCDMA<br/>联通 3G WCDMA<br/>电信 3G EVDO<br/>移动/联通 2G GSM<br/>电信 2G CDMA</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">其他参数</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">WLAN功能</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">支持 5GHz 和 2.4GHz 频段<br/>802.11 a/b/g/n 无线网络</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">蓝牙</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">Bluetooth 4.1<br/>支持 BLE</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">多媒体</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">视频</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">支持 MP4、3GP、MOV、MKV、AVI、FLV、MPEG 视频格式</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">音频</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">支持 FLAC、APE、AAC、MKA、OGG、MP3、MIDI、M4A、AMR 音频格式</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">图片</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">支持 JPEG、PNG、GIF、BMP 图片格式</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">系统与应用</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">传感器</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">重力感应<br/>红外距离感应<br/>环境光度感应<br/>触摸感应<br/>电子罗盘<br/>软陀螺仪</td></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">导航定位</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">GPS<br/>A-GPS<br/>GLONASS<br/>电子罗盘</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">操作环境</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">操作环境</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">工作环境温度 0 至 35°C<br/>存储温度 -20 至 45°C</td></tr><tr class="standard-table-group" style="background: rgb(244, 245, 246); text-indent: 30px;"><th colspan="2" style="border-color: rgb(220, 220, 220); width: 1238px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">包装清单</th></tr><tr><th style="border-color: rgb(220, 220, 220); width: 296px; color: rgb(51, 51, 51); font-weight: 400; padding: 14px 0px;">包装清单</th><td style="border-color: rgb(220, 220, 220); padding: 10px 40px; line-height: 28px; color: rgb(153, 153, 153);">主机 x 1<br/>电源适配器 x 1<br/>保修证书 x 1<br/>SIM卡顶针 x 1<br/>数据线 x 1</td></tr></tbody></table><p><br/></p>'

        return render(request,'myadmin/goods/add.html',context)
    
    elif request.method == 'POST':
        try:
            # 先判断是否有图片上传
            if not request.FILES.get('pic',None):
                return HttpResponse('<script>alert("必须选择商品图片");location.href="'+reverse('myadmin_goods_add')+'"</script>')
            pic = uploads(request)
            if pic == 1:
                return HttpResponse('<script>alert("图片类型错误");location.href="'+reverse('myadmin_goods_add')+'"</script>')

            # 执行商品的添加
            # 接收表单提交的数据
            data = request.POST.copy().dict()
            # print(data)
            # 删除掉 csrf验证的字段数据
            del data['csrfmiddlewaretoken']
            pics = request.FILES.get('pic')
            if pics:
                data['pics'] = uploads(request)
            else:
                data['pics'] = '/static/pics/users.jpg'
            data['typeid'] = Types.objects.get(id = data['typeid'])
                
            # 执行用户的创建
            ob = Goods()
            ob.pics = data['pics']
            ob.typeid = data['typeid']
            ob.title = data['title']
            ob.save()

            return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_goods_list')+'"</script>')
        except:    
            return HttpResponse('<script>alert("添加失败");location.href="'+reverse('myadmin_goods_add')+'"</script>')

            return HttpResponse('post')



def index(request):


    glist = Goods.objects.all()

    context = {'glist':glist}

    return render(request,'myadmin/goods/list.html',context)



def delete(request):
    try:
        uid = request.GET.get('uid',None)
        obj = Goods.objects.get(id=uid)

        obj.delete()
        
        data = {'msg':'删除成功','code':0}
        
    except:
        data = {'msg':'删除失败','code':1}

    return JsonResponse(data)



def edit(request):
    print(123)

    if request.method == 'GET':
        # 接收参数
        uid = request.GET.get('uid',None)

        # 获取对象
        obj = Goods.objects.get(id=uid)
        # 分配数据
        context = {'uinfo':obj}
        # 显示编辑页面
        return render(request,'myadmin/goods/edit.html',context)

    elif request.method == 'POST':
        uid = request.GET.get('uid',None)

        # 获取对象
        obj = Goods.objects.get(id=uid)

        try:
                # 判断是否上传了新的图片
            if request.FILES.get('pic',None):
                if obj.pics:
                    # 如果使用的不是默认图 则删除之前上传的头像
                    import os
                    os.remove('.'+obj.pics)

        # 执行上传
                obj.pics = uploads(request) 

            obj.title = request.POST['title']
            obj.descr = request.POST['descr']
            obj.price = request.POST['price']
            obj.store = request.POST['store']
            obj.save()

            return HttpResponse('<script>alert("修改成功");location.href="'+reverse('myadmin_goods_list')+'"</script>')
        except:
            return HttpResponse('<script>alert("修改失败");location.href="'+reverse('myadmin_goods_edit')+'?uid='+str(obj.id)+'"</script>')

# 执行文件的上传 



# 执行文件的上传 
def uploads(request):
    # 获取请求中的 文件 File
    myfile = request.FILES.get('pic',None)
    # 获取上传文件的后缀名 myfile.name.split('.').pop
    p = myfile.name.split('.').pop()
    arr = ['jpg','png','jpeg','gif']
    if p not in arr:
        return 2333

    import time,random
    # 生成新的文件名
    filename = str(time.time())+str(random.randint(1,9999))+'.'+p
    # 打开文件
    destination = open('./static/pics/'+filename,'wb+')
    # 分块写入文件
    for chunk in myfile.chunks():
        destination.write(chunk)
        # destination.write(myfile.read()) 不推荐使用

        # 关闭文件
        destination.close()

    return '/static/pics/'+filename