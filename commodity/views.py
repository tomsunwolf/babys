from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import *


# Create your views here.
def commodityView(request):
    title = '商品列表'
    classContent = 'commoditys'
    # 根据模型Types生成商品分类列表
    firsts = Types.objects.values('firsts').distinct()
    typeList = Types.objects.all()
    # 获取请求参数
    t = request.GET.get('t', '')
    s = request.GET.get('s', '')
    p = request.GET.get('p', '')
    n = request.GET.get('n', '')
    # 根据请求参数查询商品信息
    commodityInfos = CommodityInfos.objects.all()
    if t:
        types = Types.objects.filter(id=t).first()
        commodityInfos = commodityInfos.filter(types=types.seconds)
    if s:
        commodityInfos = commodityInfos.order_by('-' + s)
    if n:
        commodityInfos = commodityInfos.filter(name__contains=n)
    # 分页功能
    paginator = Paginator(commodityInfos, 6)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'commodity.html', locals())


def detailView(request, id):
    title = '商品介绍'
    classContent = 'details'
    commoditys = CommodityInfos.objects.filter(id=id).first
    items = CommodityInfos.objects.exclude(id=id).order_by('-sold')[:5]
    likesList = request.session.get('likes', [])
    likes = True if id in likesList else False
    return render(request, 'details.html', locals())
