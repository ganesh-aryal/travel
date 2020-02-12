from django.shortcuts import render,redirect
from app.models import User
from app.models import Package
from app.models import Customer
from app.models import Booking
from app.models import Admin
from app.forms import UserForm, PackageForm ,CustomerForm, BookingForm, AdminForm
from app.authenticate import Authenticate
from django.http import HttpResponse,JsonResponse

def search(request):
	packages=Package.objects.filter(PackageName__contains=request.GET['search']).values()
	return JsonResponse(list(packages),safe=False)

def home(request):
	packages=Package.objects.all()
	return render(request,'index.html',{'packages':packages})

def layout(request):
	return render(request,'layout.html')

def signin(request):
	return render(request,'signin.html')

def entry(request):
	request.session['name']=request.POST['name']
	return redirect('/package')

def signup(request):
	return render(request,'form.html')

@Authenticate.valid_admin
def index(request):
	users=User.objects.all()
	return render(request,"dashboard.html",{'users':users})


def createuser(request):
	if request.method=="POST":
		form=UserForm(request.POST)
		form.save()
		return redirect('/dash')
	form=UserForm()
	return render(request,'createuser.html',{'form':form}) 


def edituser(request,id):
	user=User.objects.get(User_id=id)
	return render(request,'edituser.html',{'user':user})


def updateuser(request,id):
	user=User.objects.get(User_id=id)
	form=UserForm(request.POST,request.FILES,instance=user)
	form.save()
	return redirect('/dash')
	

def deleteuser(request,id):
	user=User.objects.get(User_id=id)
	user.delete()
	return redirect('/dash')



def package(request):
	# limit=3
	# page=1
	# if request.method=="POST":
	# 	if "next" in request.POST:
	# 		page=(int(request.POST['page'])+1)
	# 	elif "prev" in request.POST:
	# 		page=(int(request.POST['page'])-1)
	# 	tempoffset=page-1
	# 	offset=tenpoffset*page
	# 	package=Packages.objects.raw("select * from packages limit 3 offset %s",[offset])
	# else:
	# 	package=Packages.object.raw("select * from packages limit 3 offset 0")
	# return render(request."package.html",{'package':package})

	 packages=Package.objects.all()
	 return render(request,"package.html",{'packages':packages})

def createpackage(request):
	if request.method=="POST":
		form=PackageForm(request.POST,request.FILES)
		form.save()
		return redirect('/package')
	form=PackageForm()
	return render(request,'createpackage.html',{'form':form}) 

def editpackage(request,id):
	package=Package.objects.get(package_id=id)
	return render(request,'editpackage.html',{'package':package})

def updatepackage(request,id):
	package=Package.objects.get(package_id=id)
	form=PackageForm(request.POST,request.FILES,instance=package)
	form.save()
	return redirect('/package')


def deletepackage(request,id):
	package=Package.objects.get(package_id=id).PackageImage.delete()
	package=Package.objects.get(package_id=id)
	package.delete()
	return redirect('/package')

def booking(request):
	bookings=Booking.objects.all()
	return render(request,"booking.html",{'bookings':bookings})

def customer(request):
	customers=Customer.objects.all()
	return render(request,"customer.html",{'customers':customers})


def createcustomer(request):
	if request.method=="POST":
		form=CustomerForm(request.POST)
		form.save()
		return redirect('/customer')
	form=CustomerForm()
	return render(request,'createcustomer.html',{'form':form}) 

def createcustomer_self(request):
	if request.method=="POST":
		form=CustomerForm(request.POST)
		form.save()
		customer=Customer.objects.order_by('-customer_id')[0]
		request.session['sess_cust_id']=customer.customer_id
	return redirect('/')


def editcustomer(request,id):
	customer=Customer.objects.get(customer_id=id)
	return render(request,'editcustomer.html',{'customer':customer})


def updatecustomer(request,id):
	customer=Customer.objects.get(customer_id=id)
	form=CustomerForm(request.POST,request.FILES,instance=customer)
	form.save()
	return redirect('/customer')


def deletecustomer(request,id):
	customer=Customer.objects.get(customer_id=id)
	customer.delete()
	return redirect('/customer')

def book(request):
	if request.method=="POST":
		print(request.POST)
		form=BookingForm(request.POST)
		form.save()
		del request.session['sess_cust_id']
		return redirect('/')


def book_delete(request,id):
	book=Booking.objects.get(booking_id=id)
	book.delete()
	return redirect('/booking')


def index2(request):
	limit=3
	page=1
	if request.method=="POST":
		
		if 'prev' in request.POST:
			page=(int(request.POST['page'])-1)
		else:
			page=(int(request.POST['[page]'])+1)
		tempoffset=page-1
		offset=0
		if tempoffset > 0:
			offset=tempoffset * limit
		packages=Package.objects.raw("select * from package limit 3 offset %s",[offset])
	else:
		packages=Package.objects.raw("select * from package limit 3 offset 0")
	count=Package.objects.count()
	return render(request,"package.html",{'packages':packages,'counts':count,'page':page})