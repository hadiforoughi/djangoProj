# Generated by Django 3.0.4 on 2020-03-13 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='protfol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prourl', models.URLField(blank=True)),
                ('profilepic', models.ImageField(blank=True, upload_to='pictures/userprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]