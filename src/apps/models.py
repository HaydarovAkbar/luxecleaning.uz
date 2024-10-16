from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


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
        verbose_name = 'Dash Category'
        verbose_name_plural = 'Dash Categories'
        db_table = 'dashboard_category'


class FAQ(models.Model):
    question = models.CharField(verbose_name='question ru', max_length=500, null=True, blank=True)
    answer = models.TextField(verbose_name='answer ru', null=True, blank=True)

    question_uz = models.CharField(max_length=500, null=True, blank=True)
    answer_uz = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        db_table = 'faq'


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
                                            message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed."
                                        )
                                    ],
                                    null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    lang = models.CharField(max_length=2, default='uz')

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        db_table = 'tg_users'
        indexes = [
            models.Index(fields=['chat_id'], name='chat_id_idx'),
            models.Index(fields=['username'], name='username_idx'),
            models.Index(fields=['phone_number'], name='phone_number_idx'),
        ]


class TgServices(models.Model):
    title_uz = models.CharField(max_length=355, null=True, blank=True)
    title_ru = models.CharField(max_length=355, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title_uz

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(TgServices, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tg Xizmat'
        verbose_name_plural = 'Tg Xizmatlari'
        db_table = 'tg_services'


class TgServicesPrice(models.Model):
    service = models.ForeignKey(TgServices, on_delete=models.SET_NULL, null=True)

    size_uz = models.CharField(max_length=255, null=True, blank=True)
    daily_price_uz = models.CharField(max_length=255, null=True, blank=True)
    monthly_price_uz = models.CharField(max_length=255, null=True, blank=True)

    size_ru = models.CharField(max_length=255, null=True, blank=True)
    daily_price_ru = models.CharField(max_length=255, null=True, blank=True)
    monthly_price_ru = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.service.title_uz

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(TgServicesPrice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tg Xizmat Narxi'
        verbose_name_plural = 'Tg Xizmat Narxlari'
        db_table = 'tg_services_price'


class Orders(models.Model):
    _panding = 'pending'
    _completed = 'completed'
    _canceled = 'canceled'
    ORDER_STATUS = (
        (_panding, _panding),
        (_completed, _completed),
        (_canceled, _canceled),
    )

    user = models.ForeignKey(TgUsers, on_delete=models.CASCADE)
    service = models.ForeignKey(TgServices, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=30, choices=ORDER_STATUS, default=_panding)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        return super(Orders, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Order (Zakaz)'
        verbose_name_plural = 'Orders (Zakazlar)'
        db_table = 'orders'


class Stock(models.Model):
    title_uz = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = 'Chegirma'
        verbose_name_plural = 'Chegirmalar'
        db_table = 'stock'
