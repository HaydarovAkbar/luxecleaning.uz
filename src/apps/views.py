from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from telegram import Update
from django.conf import settings
from .bot.main import bot, dispatcher
import requests
import json
from django.views import View
from telegram.error import RetryAfter
import time


from .models import Dashboard, DashboardCategory, About, Services, WhyChooseUs, Footer, TgUsers, FAQ


def index(request):
    dashboards = Dashboard.objects.all().first()
    dashboard_categories = DashboardCategory.objects.all()
    abouts = About.objects.all().first()
    services = Services.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    footer = Footer.objects.all().first()
    faqs = FAQ.objects.all()
    data = {
        'dashboards': dashboards,
        'categories': dashboard_categories,
        'abouts': abouts,
        'services': services,
        'why_choose_us': why_choose_us,
        'footer': footer,
        'faqs': faqs,
    }
    return render(request, 'index.html', data)


@csrf_exempt
def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        tg_msg = f"""
📩 New message from website:

📛 Name: {name}

☎️ Phone: {phone}

📥 Message: {message}
"""
        for admin in TgUsers.objects.filter(is_admin=True):
            try:
                requests.post('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(
                    settings.TOKEN, admin.chat_id, tg_msg))
            except Exception as e:
                print(e)
        return redirect('/')
    return HttpResponse("Invalid request!")


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
        except RetryAfter as e:
            print(f"Flood control exceeded. Retrying in {e.retry_after} seconds...")
            time.sleep(e.retry_after)  # Wait before retrying
            dispatcher.process_update(update)  # Retry processing the update
        except Exception as e:
            print(e)
        return HttpResponse('POST request')
