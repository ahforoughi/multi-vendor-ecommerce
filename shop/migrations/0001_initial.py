# Generated by Django 3.2.3 on 2021-05-26 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveBigIntegerField()),
                ('shop_id', models.PositiveIntegerField(default=0)),
                ('creation_date', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('state', models.BooleanField(default=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]