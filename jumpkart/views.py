from django.shortcuts import render,redirect
from  django.http  import  request
from .models  import Product,Cart,MySiteUser,Reviews
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse

# Create your views here.


def startpage(request):

	obj=None
	if   'cat'  in request.session:
		obj=Product.objects.filter(category=request.session['cat'])
	else:
		obj=Product.objects.all()
	
	if   'isuserloggedin'  in request.session:
		count=len(Cart.objects.filter(userid=request.session['isuserloggedin']))
		request.session['cartitemnumber']=count
		return render(request,"startpage.html",{'obj':obj,'cartitemnumber':request.session['cartitemnumber']})
	else:
		return render(request,"startpage.html",{'obj':obj})

def productdetail(request):
	
	
	p=request.POST.get("pid")
	print(p)
	row=Product.objects.filter(pid=p)
	
	rate=[]
	for i in range(0,row[0].rating):
		rate.append("star")
		
	unstar=5-len(rate)
	
	unstarlist=[]
	
	
	rev=Reviews.objects.filter(pid=p)
	
	for i in range(0,unstar):
		unstarlist.append("star")
		
	if   'isuserloggedin'  in request.session:
	
		count=len(Cart.objects.filter(userid=request.session['isuserloggedin']))
		request.session['cartitemnumber']=count
		return render(request,"productdetail.html",{'obj':row[0],'rate':rate,'unstarlist':unstarlist,'cartitemnumber':request.session['cartitemnumber'],'reviews':rev})
	else:
		return render(request,"productdetail.html",{'obj':row[0],'rate':rate,'unstarlist':unstarlist,'reviews':rev})
		

def addtocart(request):

	pi=request.POST.get("pid")
	
	productvalue=Product.objects.filter(pid=pi)
	
	if   'isuserloggedin'  in request.session:
		row=Cart.objects.filter(pid=pi,userid=request.session['isuserloggedin'])
	

		if(len(row)>0):
		
			quant =int(row[0].quantity)+1
		
			Cart.objects.filter(pid=pi,userid=request.session['isuserloggedin']).update(quantity=quant)




		else:
			product=productvalue[0]
			obj =Cart.objects.create(pid=product.pid,name=product.name,des=product.des,rating=product.rating,img=product.img,price=product.price,category="",specify="",quantity="1",userid=request.session['isuserloggedin'])
			obj.save()
			count=len(Cart.objects.filter(userid=request.session['isuserloggedin']))
			request.session['cartitemnumber']=count
	
	return  redirect("http://localhost:8000/cartpage")
	
	
	
	
	
	
def checkoutpage(request):

		
		if   'isuserloggedin'  in request.session:
		
			base=request.POST.get("price")

			grand = float(base)+ 40
		
		
		
			return render(request,"payment_process.html",{'grand':grand,'baseprice':base,'cartitemnumber':request.session['cartitemnumber']})

		else:
			return redirect("http://localhost:8000/loginpage")


def cartpage(request):
	
	if   'isuserloggedin'  in request.session:
		obj=Cart.objects.filter(userid=request.session['isuserloggedin'])
		sum=0
		for i in obj :
			sum = sum+float(i.price)*int(i.quantity)
	
	
		grand=sum+5
	
		return  render(request,"cartpage.html",{'cartitems':Cart.objects.filter(userid=request.session['isuserloggedin']),'cartitemnumber':request.session['cartitemnumber'],'sum':sum,"grand":grand})
	else:
		
		return  redirect("http://localhost:8000/loginpage")

def decitemfromcart(request):

	if   'isuserloggedin'  in request.session:
		pi=request.POST.get("pid")
		quant=request.POST.get("quant")
		Cart.objects.filter(pid=pi,userid=request.session['isuserloggedin']).update(quantity=quant)
		return  redirect("http://localhost:8000/cartpage")
		
	else :
	
		return redirect("http://localhost:8000/loginpage")
		
		
def removeitemfromcart(request):

	if   'isuserloggedin'  in request.session:
		pi=request.POST.get("pid")
		print(pi)
	
		Cart.objects.filter(pid=pi,userid=request.session['isuserloggedin']).delete()
		count=len(Cart.objects.filter(userid=request.session['isuserloggedin']))
		request.session['cartitemnumber']=count
	
		return  redirect("http://localhost:8000/cartpage")
		
	else:
	
		return  redirect("http://localhost:8000/loginpage")


def  home(request):
	
	request.session['validemail']=""
	request.session['validlogin']=""
	
	return render(request,"login.html",{'path':'http://localhost:8000/static/','error':request.session['validlogin']})

def signup(request):
	
	return render(request,"signup.html",{'path':'http://localhost:8000/static/','error':request.session['validemail']})

def checklogin(request):

	n= request.POST.get("uname")
	p= request.POST.get("pass")
	
	row = MySiteUser.objects.filter(email=n,password=p)
	i=0
	for k in row:
		i+=1

	if i>0:
		request.session['validlogin']=""
		request.session['isuserloggedin']=n
		return redirect("http://localhost:8000/")
	else:
		request.session['validlogin']="invalid email or  password"
		
		return redirect("http://localhost:8000/loginpage")
		
		
	


	

def register(request):

	fname= request.POST.get("fname")
	lname= request.POST.get("lname")
	em= request.POST.get("email")
	p= request.POST.get("password")

	row=MySiteUser.objects.filter(email=em)
	if  len(row)>0 :
		request.session['validemail']="email already in use"
		return redirect("http://localhost:8000/signup")
		
	else:
		obj = MySiteUser(firstname=fname,lastname=lname,email=em,password=p,country="not available",address="not available",town="not available",zipcode="0000",phone="not availabe",comment="")
		obj.save()
		request.session['validemail']=""
		return redirect("http://localhost:8000/loginpage")

		
		
def logout(request):

	if   'isuserloggedin'  in request.session:
	
		del request.session['isuserloggedin']
		return redirect("http://localhost:8000/")
		
	else:
		return redirect("http://localhost:8000/loginpage")
		
		
		
		
def setCategory(request):
	cat=request.GET.get('cat')
	request.session['cat']=cat
	return redirect("http://localhost:8000")
	
	
	
def payment_process(request):
	host = request.get_host()
	paypal_dict = {
       'business': "niteshdsharma44@gmail.com" ,
       'amount': '1',
       'item_name': 'Item_Name_xyz',
       'invoice': ' Test Payment Invoice',
       'currency_code': 'USD',
       'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
       'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
       'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
       }
	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, 'payment_process.html', {'form': form })
	
	
	
	
	