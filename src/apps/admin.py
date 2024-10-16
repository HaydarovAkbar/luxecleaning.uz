from django.contrib import admin
from .models import Dashboard, DashboardCategory, About, Services, FAQ, Footer, \
    TgUsers, TgServices, Orders, Stock, TgServicesPrice
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


# admin.site.register(Dashboard, BaseAdmin)
admin.site.register(DashboardCategory, EditorAdmin)
admin.site.register(About, Editor2Admin)
admin.site.register(Services, Editor2Admin)
# admin.site.register(ImportantInformation)
admin.site.register(Footer, BaseAdmin)
# admin.site.register(WhyChooseUs, Editor2Admin)
admin.site.register(TgUsers, TGUsersAdmin)
admin.site.register(FAQ, EditorAdmin)


# admin.site.register(TgServices, EditorAdmin)
# admin.site.register(Orders, BaseAdmin)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'status', 'created_at', 'update_at')
    list_filter = ('status',)
    search_fields = ('user', 'service', 'status')
    list_editable = ('status',)


@admin.register(TgServices)
class TgServicesAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'created_at', 'updated_at')


@admin.register(TgServicesPrice)
class TgServicesPriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'daily_price_ru', 'daily_price_uz', 'monthly_price_uz', 'monthly_price_ru')
    list_editable = ('daily_price_ru', 'daily_price_uz', 'monthly_price_ru', 'monthly_price_uz')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'created_at', 'updated_at')
    # list_editable = ('title',)
