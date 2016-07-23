from django.shortcuts import render, HttpResponse
from django.views.generic import View

class hola(View):
	def get(self,request):
		return HttpResponse('Khe miras prro >:v!!')
		