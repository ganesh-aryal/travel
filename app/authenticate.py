from django.shortcuts import redirect
from app.models import Admin
from django.contrib import messages
class Authenticate:
	def valid_admin(function):
		def wrap(request):
			try:
				User.objects.get(admin_name=request.session['name'])
				return function(request)
			except:
				messages.warning(request,"Please Login")
				return redirect('/signin')
		return wrap
