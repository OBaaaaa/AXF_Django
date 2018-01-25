from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^market/$',views.NoParMarket,name='NoParMarket'),
    url(r'^market/(\d+)/(\d+)/(\d+)/',views.market,name='market'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^registe/',views.registe,name='registe'),
    url(r'^doregiste',views.doRegiste,name='doRegiste'),
    url(r'^usernamecheck/',views.usernameCheck,name='usernameCheck'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^login/',views.login,name='login'),
    url(r'^dologin/',views.doLogin,name='doLogin'),
    url(r'^addgoods/',views.addGoods,name='addGoods'),
    url(r'^subgoods/',views.subGoods,name='subGoods'),
    url(r'^subshopping/',views.subShopping,name='subShopping'),
    url(r'^addshopping/',views.addShopping,name='addShopping'),
    url(r'^changecheck/',views.changeCheck,name='changeCheck'),
    url(r'^makeorder/',views.makeOrder,name='makeOrder'),
    url(r'^getorder/',views.getOrder,name='getOrder'),
    url(r'^pay/',views.pay,name='pay'),
]