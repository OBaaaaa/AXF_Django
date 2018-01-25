import hashlib

from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Axf_wheel, Axf_nav, Axf_mustbuy, Axf_shop, Axf_mainshow, Axf_foodtypes, Axf_goods, User, Cart, \
    Order


def home(request):
    axf_wheels = Axf_wheel.objects.all()
    axf_navs = Axf_nav.objects.all()
    axf_mustbuys = Axf_mustbuy.objects.all()
    axf_shop = Axf_shop.objects.all()
    axf_shop_first = axf_shop.first()
    axf_shop_second = axf_shop[1:3]
    axf_shop_third = axf_shop[3:7]
    axf_shop_fourth = axf_shop[7:]
    axf_mainshows = Axf_mainshow.objects.all()
    data = {
        'page_title':'首页',
        'axf_wheels':axf_wheels,
        'axf_navs':axf_navs,
        'axf_mustbuys':axf_mustbuys,
        'axf_shop_first':axf_shop_first,
        'axf_shop_second': axf_shop_second,
        'axf_shop_third': axf_shop_third,
        'axf_shop_fourth': axf_shop_fourth,
        'axf_mainshows':axf_mainshows,
    }
    return render(request,'home/home.html',context=data)


def market(request,typeid,ccid,orderRule):

    foodtypes = Axf_foodtypes.objects.all()
    axf_goods = Axf_goods.objects.filter(categoryid=typeid)

    if ccid != '0' :
        axf_goods = axf_goods.filter(childcid=ccid)

    if orderRule == '1':
        axf_goods = axf_goods.order_by('productnum')
    elif orderRule == '2':
        axf_goods = axf_goods.order_by('price')
    elif orderRule == '3':
        axf_goods = axf_goods.order_by('-price')

    types = Axf_foodtypes.objects.filter(typeid=typeid).first()
    childtypename = types.childtypenames

    childtypename_list = childtypename.split('#')
    childtypename_lists = []
    for item in childtypename_list:
        temp = item.split(':')
        childtypename_lists.append(temp)

    username = request.session.get('username')
    users = User.objects.filter(u_username=username)
    if users.exists():
        user = users.first()
        user_cart = Cart.objects.filter(cart_user=user).filter(cart_belong=False)

    data = {
        'page_title': '闪购',
        'foodtypes':foodtypes,
        'axf_goods':axf_goods,
        'childs':childtypename_lists,
        'typeid':typeid,
        'ccid':ccid,
        'user_cart':user_cart,
    }

    return render(request,'market/market.html',context=data)

def cart(request):

    username = request.session.get('username')
    users = User.objects.filter(u_username=username)
    if users.exists():
        user = users.first()
        cart_list = Cart.objects.filter(cart_belong=False).filter(cart_user=user)


    data = {
        'page_title': '购物车',
        'cart_list':cart_list,
    }
    return render(request,'cart/cart.html',context=data)


def mine(request):
    data = {
        'page_title': '我',

    }
    username = request.session.get('username')
    users = User.objects.filter(u_username=username)



    if users.exists():
        user = users.first()
        orders = Order.objects.filter(user=user).filter(order_status=1)
        is_login = True
        data['user'] =  user
        data['is_login'] = is_login
        data['orders'] = orders.count()


    return render(request,'mine/mine.html',context=data)


def NoParMarket(request):
    return redirect(reverse('App:market',args=('104749','0','0')))


def registe(request):
    return render(request, 'mine/registe.html')


def doRegiste(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    password = my_md5(password)

    email = request.POST.get('email')
    phone = request.POST.get('phone')
    icon = request.FILES['icon']
    sex = request.POST.get('sex')

    if sex=='True':
        sex = True
    elif sex=='False':
        sex = False
    else:
        sex = None

    user = User()
    user.u_username = username
    user.u_password = password
    user.u_email = email
    user.u_phone = phone
    user.u_icon = icon
    user.u_sex = sex
    user.save()



    request.session['username'] = username

    response = HttpResponseRedirect(reverse('App:mine'))

    return response


def usernameCheck(request):
    username = request.GET.get('username')
    user = User.objects.filter(u_username=username)
    data = {'status':'200','msg':'用户名可用'}
    if user.exists():
        data['status'] = '901'
        data['msg'] = '用户名已存在'
    return JsonResponse(data)


def logout(request):
    del request.session['username']

    response = HttpResponseRedirect(reverse('App:mine'))
    response.delete_cookie('sessionid')
    response.delete_cookie('login_res')

    return response


def login(request):
    data = {
        'page_title':'登录',
    }
    print(request.COOKIES.get('login_res'))
    if request.COOKIES.get('login_res')=='F':
        data['login_res'] = '用户名或密码错误'

    return render(request,'mine/login.html',context=data)


def doLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    users = User.objects.filter(u_username=username)
    response = HttpResponseRedirect(reverse('App:login'))
    if users.exists():
        user = users.first()
        # print(my_md5(password))
        if my_md5(password) == user.u_password:
            request.session['username'] = username
            response.delete_cookie('login_res')
            return redirect(reverse('App:mine'))
        else:
            response.set_cookie('login_res','F')
    else:
        response.set_cookie('login_res', 'F')

    return response


def my_md5(num):
    md5 = hashlib.md5()
    md5.update(num.encode('utf-8'))
    return md5.hexdigest()


def addGoods(request):

    data = {'status':'200','goods_num':'1'}
    username = request.session.get('username')
    goods_id = request.GET.get('goods_id')
    if not username:
        data['status'] = '901'
        return JsonResponse(data)

    users = User.objects.filter(u_username=username)
    goods_s = Axf_goods.objects.filter(pk = goods_id)

    if goods_s.exists():
        if users.exists():
            user = users.first()
            goods = goods_s.first()
            carts = Cart.objects.filter(cart_belong=False).filter(Q(cart_user=user) & Q(cart_goods=goods))
            if carts.exists():
                cart_my = carts.first()
                cart_my.cart_num += 1
                cart_my.save()
            else:
                cart_my = Cart()
                cart_my.cart_user = user
                cart_my.cart_goods = goods
                cart_my.save()
            data['status'] = '200'
            data['goods_num'] = str(cart_my.cart_num)
            return JsonResponse(data)
    data['status'] = '900'
    return JsonResponse(data)

def subGoods(request):
    data = {'status': '200', 'goods_num': '0'}
    username = request.session.get('username')
    goods_id = request.GET.get('goods_id')
    if not username:
        data['status'] = '901'
        return JsonResponse(data)

    users = User.objects.filter(u_username=username)
    goods_s = Axf_goods.objects.filter(pk=goods_id)

    if goods_s.exists():
        if users.exists():
            user = users.first()
            goods = goods_s.first()
            carts = Cart.objects.filter(cart_belong=False).filter(Q(cart_user=user) & Q(cart_goods=goods))
            if carts.exists():
                cart_my = carts.first()
                if cart_my.cart_num > 1:
                    cart_my.cart_num -= 1
                    cart_my.save()
                    data['goods_num'] = str(cart_my.cart_num)
                elif cart_my.cart_num == 1:
                    cart_my.delete()
            data['status'] = '200'
            return JsonResponse(data)
    data['status'] = '900'
    return JsonResponse(data)


def subShopping(request):
    data = {'status':'200','goods_num':'0'}
    goods_id = request.GET.get('goods_id')
    username = request.session.get('username')
    users = User.objects.filter(u_username=username)
    if users.exists():
        goods_s = Cart.objects.filter(pk=goods_id)
        if goods_s.exists():
            goods = goods_s.first()
            if goods.cart_num == 1:
                del goods
                data['status'] = '400'
            else:
                goods.cart_num -= 1
                goods.save()
                data['goods_num'] = goods.cart_num
            return JsonResponse(data)
        else:
            data['status'] = '901'
        return JsonResponse(data)


def addShopping(request):
    data = {'status': '200', 'goods_num': '1'}
    goods_id = request.GET.get('goods_id')
    username = request.session.get('username')
    users = User.objects.filter(u_username=username)
    if users.exists():
        goods_s = Cart.objects.filter(pk=goods_id)
        if goods_s.exists():
            goods = goods_s.first()
            goods.cart_num += 1
            goods.save()
            data['goods_num'] = goods.cart_num
        else:
            data['status'] = '400'
        return JsonResponse(data)


def changeCheck(request):
    data = {'status':'901'}
    goods_id = request.GET.get('goods_id')
    carts = Cart.objects.filter(pk=goods_id)
    if carts.exists():
        cart_my = carts.first()
        check_flag = cart_my.cart_check
        cart_my.cart_check = not check_flag
        cart_my.save()
        data['status'] = '200'
    return JsonResponse(data)


def makeOrder(request):
    data = {'status':'200'}
    username = request.session.get('username')
    user = User.objects.filter(u_username=username).first()
    good_id_list = request.GET.get('good_id_list').split('#')
    order = Order()
    order.user = user
    order.save()

    for id in good_id_list:
        cart_my = Cart.objects.filter(pk=id).first()
        cart_my.cart_belong = True
        cart_my.cart_order = order
        cart_my.save()

    data['order_id'] = order.id

    return JsonResponse(data)


def getOrder(request):

    order_id = request.GET.get('order_id')
    order = Order.objects.filter(pk=order_id).first()
    cart_list = order.cart_set.all()
    data = {
        'page_title':'order',
        'order_id':order_id,
        'cart_list':cart_list,


    }

    return render(request,'cart/order.html',context=data)


def pay(request):


    order_id = request.GET.get('order_id')
    order = Order.objects.filter(pk=order_id).first()
    order.order_status = 1
    order.save()
    data = {'status': '200'}
    return JsonResponse(data)