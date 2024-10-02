from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from telegram import Update
from .bot.main import bot, dispatcher
import json
from django.views import View

from .models import Dashboard, DashboardCategory, About, Services, WhyChooseUs, Footer


def index(request):
    dashboards = Dashboard.objects.all().first()
    dashboard_categories = DashboardCategory.objects.all()
    abouts = About.objects.all().first()
    services = Services.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    footer = Footer.objects.all().first()
    data = {
        'dashboards': dashboards,
        'categories': dashboard_categories,
        'abouts': abouts,
        'services': services,
        'why_choose_us': why_choose_us,
        'footer': footer,
    }
    return render(request, 'index.html', data)


@csrf_exempt
def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(name, phone, message)

        return HttpResponse("Thank you for your message!")

    return render(request, 'index.html')


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request')

    def post(self, request, *args, **kwargs):
        try:
            body = request.body
            body_json = json.loads(body)
            update: Update = Update.de_json(body_json, bot)
            dispatcher.process_update(update)
        except Exception as e:
            print(e)
        return HttpResponse('POST request')
