# Generated by Django 3.0.8 on 2020-07-20 18:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0057_page_locale_fields_notnull'),
        ('blog', '0005_i18n_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpeoplerelationship',
            name='locale',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Locale'),
        ),
        migrations.AlterField(
            model_name='blogpeoplerelationship',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
