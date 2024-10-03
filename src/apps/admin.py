from django.contrib import admin
from .models import Dashboard, DashboardCategory, About, Services, ImportantInformation, Footer, WhyChooseUs, TgUsers
from django_summernote.widgets import SummernoteWidget
from django.db import models


# Register your models here.
class EditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }


class Editor2Admin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }
    list_display = ('title', 'created_at', 'updated_at')


class BaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


class TGUsersAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'first_name', 'last_name', 'is_admin', 'created_at')


admin.site.register(Dashboard, BaseAdmin)
admin.site.register(DashboardCategory, EditorAdmin)
admin.site.register(About, Editor2Admin)
admin.site.register(Services, Editor2Admin)
admin.site.register(ImportantInformation)
admin.site.register(Footer, BaseAdmin)
admin.site.register(WhyChooseUs, Editor2Admin)
admin.site.register(TgUsers, TGUsersAdmin)
