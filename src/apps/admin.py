from django.contrib import admin
from .models import Dashboard, DashboardCategory, About, Services, ImportantInformation, Footer, WhyChooseUs
from django_summernote.widgets import SummernoteWidget
from django.db import models


# Register your models here.
class EditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }


admin.site.register(Dashboard)
admin.site.register(DashboardCategory, EditorAdmin)
admin.site.register(About, EditorAdmin)
admin.site.register(Services, EditorAdmin)
admin.site.register(ImportantInformation)
admin.site.register(Footer, EditorAdmin)
admin.site.register(WhyChooseUs, EditorAdmin)
