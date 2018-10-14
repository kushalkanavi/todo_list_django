from django.shortcuts import render, redirect
from django.views import View
from .forms import TaskinformForm
from .models import task

import datetime

from django.db.models import Q
from django.contrib import messages

import pdb

class index(View):
	def get(self, request, *args, **Kwargs):

		form = TaskinformForm()
		taskinfo = task.objects.order_by('Due_Date').all()
		today  = datetime.date.today()
		
		context = {
			'form':form,
			'task':taskinfo,
			'todayDate':today
			}
		return render(request,'my_app/index.html',context)

class saveTaskInfo(View):
	def post(self, request, *args, **Kwargs):

		form=TaskinformForm(self.request.POST)
		
		if form.is_valid():
			form.save()

		return redirect( 'app:index' )

def tasksearch(request):
	if request.method == 'POST':
		srch  = request.POST['search']

		if srch:
			match = task.objects.filter(Q(Title__icontains = srch))

			form = TaskinformForm()
			taskinfo = task.objects.order_by('Due_Date').all()
			today  = datetime.date.today()

			if match:
				context = {
				'srch':match,
				'form':form,
				'task':taskinfo,
				'todayDate' :today
				}
				return render(request,'my_app/index.html',context)

			else:
				messages.error(request,'No Result Found.')
		       
		else:
			return render(request,'my_app/index.html')

	return render(request,'my_app/index.html')

def taskfilter(request):
	datefilter = request.POST.get('filter')
	today  = datetime.date.today()

	if datefilter == 'today':
		taskinfo = task.objects.filter(Due_Date__icontains=today).order_by('Due_Date')
	elif datefilter == 'thisweek':
		startdate = datetime.date.today()
		enddate = startdate + datetime.timedelta(days=6)
		taskinfo = task.objects.filter(Due_Date__range=[startdate, enddate]).order_by('Due_Date')
	elif datefilter == 'nextweek':
		startdate = datetime.date.today() + datetime.timedelta(days=6)
		enddate = startdate + datetime.timedelta(days=6)
		taskinfo = task.objects.filter(Due_Date__range=[startdate, enddate]).order_by('Due_Date')
	else:
		None
	
	form = TaskinformForm()
	
	context = {
		'form':form,
		'task':taskinfo,
		'todayDate':today
		}
	return render(request,'my_app/index.html',context)

class edittask(View):
	def get(self, request, *args, **Kwargs):
		taskid = request.session['taskid'] = Kwargs['id']

		if (task.objects.filter(id = taskid).exists()):
			form = TaskinformForm(instance = task.objects.get(id = taskid))
			return render(request,'my_app/edit_task.html',{'form' : form})

		else:
			form = TaskinformForm()
			return render(request,'my_app/edit_task.html',{'form' : form})
	
		return redirect( 'app:index' )

	def post(self, request, *args, **Kwargs):
		taskid = request.session['taskid']

		if (task.objects.filter(id = taskid).exists()):
			if self.request.method == 'POST':
				form=TaskinformForm(self.request.POST,instance = task.objects.get(id = taskid))

				if form.is_valid():
					form.save()
					return redirect( 'app:index' )
            
		else:
			form = TaskinformForm(self.request.POST)
			if self.request.method == 'POST':
				if form.is_valid():
					fform = form.save()

		return redirect( 'app:index' )

def addsubtask(request):
	
	return redirect( 'app:index' )

















