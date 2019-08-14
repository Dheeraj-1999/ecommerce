"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from  jumpkart.views import  startpage,productdetail,checkoutpage,addtocart,cartpage,decitemfromcart,removeitemfromcart,home,signup,checklogin,register,logout,setCategory,payment_process
from  django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
     
    path('productdetail/',productdetail),
path('setCategory/',setCategory)
,  path('checkout/',payment_process),path('addtocart/',addtocart),path('cartpage/',cartpage),
path('decitem/',decitemfromcart),
path('removeitemfromcart/',removeitemfromcart),
path('',startpage),
path('signup/',signup),
path('checklogin/',checklogin),
path('register/',register),
path('logout/',logout),
path('loginpage/',home),
url(r'^paypal/', include('paypal.standard.ipn.urls')),
url(r'^payment_process/$', payment_process, name='payment_process' ),

url(r'^payment_done/$', TemplateView.as_view(template_name= "pets/payment_done.html"), name='payment_done'),

url(r'^payment_canceled/$', TemplateView.as_view(template_name= "pets/payment_canceled.html"), name='payment_canceled'),


]
