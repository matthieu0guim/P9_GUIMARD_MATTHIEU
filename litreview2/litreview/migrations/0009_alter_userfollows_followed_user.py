# Generated by Django 3.2.9 on 2021-12-22 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('litreview', '0008_alter_ticket_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollows',
            name='followed_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL, verbose_name=''),
        ),
    ]