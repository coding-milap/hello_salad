# Generated by Django 4.1.3 on 2023-04-14 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermembership', to='store.membership'),
        ),
    ]
