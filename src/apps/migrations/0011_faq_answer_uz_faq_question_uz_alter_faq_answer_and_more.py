# Generated by Django 4.2.16 on 2024-10-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_alter_tgservices_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='answer ru'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='question ru'),
        ),
    ]
