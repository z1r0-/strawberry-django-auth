# Generated by Django 3.2.12 on 2022-03-29 08:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('text', models.CharField(editable=False, max_length=50)),
                ('insert_time', models.DateTimeField(auto_now_add=True)),
                ('tries', models.IntegerField(default=0)),
            ],
        ),
    ]