from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from task2_4_app.models import Route, Driver


from django.http import HttpResponse
# Create your views here.


class Index(View):
    def get(self, reguest):
        drivers = Driver.objects.all()
        routes = Route.objects.all()
        context = {"routes" : routes,
                   "drivers" : drivers}
        
        return HttpResponse(render(template_name='index.html', request=reguest, context=context))