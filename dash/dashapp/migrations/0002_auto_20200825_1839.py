# Generated by Django 3.0.8 on 2020-08-25 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PageView',
            new_name='Visits',
        ),
        migrations.RenameField(
            model_name='visits',
            old_name='page_views',
            new_name='page_visits',
        ),
    ]