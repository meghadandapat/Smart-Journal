# Generated by Django 4.1.6 on 2023-05-05 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0006_remove_profileentries_user_profileentries_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileentries',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
