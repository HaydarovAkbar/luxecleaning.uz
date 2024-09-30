from django.shortcuts import render

from .models import Dashboard, DashboardCategory, About, Services


def index(request):
    dashboards = Dashboard.objects.all()
    dashboard_categories = DashboardCategory.objects.all()
    abouts = About.objects.all()
    services = Services.objects.all()
    data = {
        'dashboards': dashboards,
        'categories': dashboard_categories,
        'abouts': abouts,
        'services': services,
    }
    return render(request, 'index.html', data)
