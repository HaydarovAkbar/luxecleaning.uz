from django.shortcuts import render

from .models import Dashboard, DashboardCategory, About, Services, WhyChooseUs


def index(request):
    dashboards = Dashboard.objects.all().first()
    dashboard_categories = DashboardCategory.objects.all()
    abouts = About.objects.all()
    services = Services.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    data = {
        'dashboards': dashboards,
        'categories': dashboard_categories,
        'abouts': abouts,
        'services': services,
        'why_choose_us': why_choose_us
    }
    print(dashboards.image.url)
    return render(request, 'index.html', data)
