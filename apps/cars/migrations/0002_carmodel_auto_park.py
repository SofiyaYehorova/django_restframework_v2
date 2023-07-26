# Generated by Django 4.2.3 on 2023-07-26 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel'),
            preserve_default=False,
        ),
    ]
