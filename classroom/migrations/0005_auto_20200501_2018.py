# Generated by Django 3.0.5 on 2020-05-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20200501_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Applicants'},
        ),
        migrations.AlterModelOptions(
            name='studentanswer',
            options={'verbose_name': 'Applicant Answer', 'verbose_name_plural': 'Applicant Answers'},
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
