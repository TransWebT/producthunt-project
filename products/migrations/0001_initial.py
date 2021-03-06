# Generated by Django 2.2 on 2019-04-21 19:33

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=300)),
                ('pub_date', models.DateTimeField()),
                ('votes_total', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(upload_to='images/')),
                ('icon', models.ImageField(upload_to='images/')),
                ('body', models.TextField(max_length=2000)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
