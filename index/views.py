from django.shortcuts import render
from django.views.generic import TemplateView
from commodity.models import *


# Create your views here.
def indexViews(request):
    title = '首页'
    classContent = ''
    commodityinfos = CommodityInfos.objects.order_by('-sold').all()[:8]
    print(commodityinfos.name)
    types = Types.objects.all()
    # 宝宝服饰
    cl = [x.seconds for x in types if x.firsts == '儿童服饰']
    clothes = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]
    # 奶粉辅食
    fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
    food = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]
    # 宝宝用品
    gl = [x.seconds for x in types if x.firsts == '儿童用品']
    goods = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]
    return render(request, 'index.html', locals())


# app_index的视图类
class indexClassView(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = None
    extra_context = {'title': '首页', 'classContent': ''}

    # 重新定义模板上下文的获取方法
    def get_context_data(self, **kwargs):
        context = super(indexClassView, self).get_context_data(**kwargs)
        context['commodityInfos'] = CommodityInfos.objects.order_by('-sold').all()[:8]
        types = Types.objects.all()
        # 宝宝服饰
        cl = [x.seconds for x in types if x.firsts == '儿童服饰']
        context['clothes'] = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]
        # 奶粉辅食
        fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
        context['food'] = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]
        # 宝宝用品
        gl = [x.seconds for x in types if x.firsts == '儿童用品']
        context['goods'] = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]
        return context

    def get(self, request, *args, **kwargs):
        pass
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
