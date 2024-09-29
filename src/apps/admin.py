from django.contrib import admin
from .models import Dashboard, DashboardCategory, About, Services, ImportantInformation, Footer

admin.site.register(Dashboard)
admin.site.register(DashboardCategory)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(ImportantInformation)
admin.site.register(Footer)