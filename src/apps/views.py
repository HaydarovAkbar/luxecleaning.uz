from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
