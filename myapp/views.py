from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *
# from django.utils import simplejson as json

# Create your views here.

def start(request):
	return render (request,'index.html')


def contact(request):
	role="add"
	return render(request,'contact.html',{'role':role})

def addcontact(request):
	if request.method == 'POST':
		uname=request.POST.get("userName")
		unumber=request.POST.get("userPhone")
		obj=Contact(name=uname,number=unumber)
		obj.save()
		return allcontacts(request)

def update_contact(request,uid):
	obj=Contact.objects.get(id=uid)
	role="update"
	uname=obj.name
	unumber=obj.number
	uid=obj.id
	return render(request,'contact.html',{'role':role,'name':uname,'number':unumber,'uid':uid})	

def up_contact(request,uid):
	obj=Contact.objects.get(id=uid)
	if request.method =='POST':
		uname=request.POST.get("userName")
		unumber=request.POST.get("userPhone")
		obj.name=uname
		obj.number=unumber
		obj.save()
		contacts=Contact.objects.all()
		return render(request,'contacts.html',{'contacts':contacts})

def find(request):
	return render(request,'find.html')

def findcontact(request):
	if request.method == 'POST':
		if request.POST.get("userName"):
			uname=request.POST.get("userName")
			contacts=Contact.objects.filter(name=uname)
			return render(request,'contacts.html',{'contacts':contacts})
		if request.POST.get("userPhone"):
			unumber=request.POST.get("userPhone")
			contacts=Contact.objects.filter(number=unumber)
			return render(request,'contacts.html',{'contacts':contacts})

# def ajax(request):
#    if request.POST.has_key('client_response'):
#         x = request.POST['client_response']                  
#         y = socket.gethostbyname(x)                           
#         response_dict = {}                                          
#         response_dict.update({'server_response': y })                                                                   
#         return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript') 
#    else:
#         return render('index.html', context_instance=RequestContext(request)


def allcontacts(request):
	contacts=Contact.objects.all()
	return render(request,'contacts.html',{'contacts':contacts})


def del_contact(request,uid):
	Contact.objects.get(id=uid).delete()
	return allcontacts(request)