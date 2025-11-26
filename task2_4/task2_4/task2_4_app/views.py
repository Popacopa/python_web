from django.shortcuts import render, redirect
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
    

class Form(View):
    def get(self, request, item):
        drivers = Driver.objects.all()
        context = {
            'item': item,
            'drivers': drivers,
            'is_update': False,
        }
        return HttpResponse(render(template_name='form.html', request=request, context=context))
    
    def post(self, request, item):
        if item == 'driver':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            age = request.POST.get('age')
            stage = request.POST.get('stage')
            Driver.objects.create(first_name=first_name, last_name=last_name, age=age, stage=stage)
        elif item == 'route':
            city_from = request.POST.get('city_from')
            city_to = request.POST.get('city_to')
            driver_id = request.POST.get('driver_id')
            driver = Driver.objects.get(id=driver_id)
            try:
                exiting = Route.objects.get(driver_id=driver)
            except Route.DoesNotExist:
                Route.objects.create(city_from=city_from, city_to=city_to, driver_id=driver)
        return redirect('/')
    
class Delete(View):
    def get(self, request, id, item):
        if item == "driver":
            Driver.objects.get(id=id).delete()
        if item == "route":
            id = id.split(' ')
            driver = Driver.objects.get(first_name=id[0], last_name=id[1])
            Route.objects.get(driver_id=driver).delete()
        return redirect('/')
    


class Update(View):
    def get(self, request, item, id):
        drivers = Driver.objects.all()
        context = {
            'item': item,
            'drivers': drivers,
            'is_update': True,
        }
        return HttpResponse(render(template_name='form.html', request=request, context=context))
    def post(self, request, item, id):
        if item == 'driver':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            age = request.POST.get('age')
            stage = request.POST.get('stage')
            driver = Driver.objects.filter(id = id)
            driver.update(first_name=first_name, last_name=last_name, age=age, stage=stage)
        elif item == 'route':
            city_from = request.POST.get('city_from')
            city_to = request.POST.get('city_to')
            driver_id = request.POST.get('driver_id')
            id = id.split(' ')
            driver = Driver.objects.get(first_name=id[0], last_name=id[1])
            exiting = Route.objects.get(driver_id=driver)
            Route.objects.filter(driver_id=driver).update(city_from=city_from, city_to=city_to, driver_id=driver_id)
        return redirect('/')