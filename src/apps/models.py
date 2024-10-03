from django.db import models
from django.core.validators import RegexValidator


class Dashboard(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='dashboard/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dashboard'
        verbose_name_plural = 'Dashboards'
        db_table = 'dashboard'


class DashboardCategory(models.Model):
    title1 = models.CharField(max_length=255, null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    title2 = models.CharField(max_length=255, null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='icon/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title1

    class Meta:
        verbose_name = 'Dashboard Category'
        verbose_name_plural = 'Dashboard Categories'
        db_table = 'dashboard_category'


class About(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
        db_table = 'about'


class Services(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        db_table = 'services'


class ImportantInformation(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='important/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Important Information'
        verbose_name_plural = 'Important Informations'
        db_table = 'important_information'


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='why_choose_us/', null=True, blank=True)
    image2 = models.ImageField(upload_to='why_choose_us/', null=True, blank=True)
    image3 = models.ImageField(upload_to='why_choose_us/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Почему выбирают нас'
        verbose_name_plural = 'Почему выбирают нас?'
        db_table = 'why_choose_us'


class Footer(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    telegram = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone1 = models.CharField(max_length=255, null=True, blank=True)
    phone2 = models.CharField(max_length=255, null=True, blank=True)

    address = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'
        db_table = 'footer'


class TgUsers(models.Model):
    chat_id = models.PositiveIntegerField(null=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13,
                                    validators=[
                                        RegexValidator(
                                            regex=r'^\+998\d{9}$',  # Example regex for international phone numbers
                                            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                        )
                                    ],
                                    null=True, blank=True)

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        db_table = 'tg_users'
