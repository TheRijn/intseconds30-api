# Generated by Django 2.2.5 on 2019-09-12 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190912_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='words', to='api.Category'),
        ),
    ]
