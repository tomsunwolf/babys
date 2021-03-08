from django.shortcuts import render,HttpResponse


# Create your views here.
def shopperView(request):
    return HttpResponse('商城视图')


def loginView(request):
    return HttpResponse('登录视图')


def logoutView(request):
    return HttpResponse('退出视图')


def shopcartView(request):
    return HttpResponse('购物车视图')
