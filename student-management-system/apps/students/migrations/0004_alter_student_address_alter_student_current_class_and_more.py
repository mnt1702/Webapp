# Generated by Django 4.1.4 on 2022-12-21 22:25

import apps.students.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0004_auto_20201124_0614'),
        ('students', '0003_merge_0002_auto_20201124_0614_0002_remove_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.studentclass', verbose_name='class'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default=apps.students.models.random_string, max_length=200, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Fullname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_mobile_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')], verbose_name='parent phone number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='passport',
            field=models.ImageField(blank=True, upload_to='students/passports/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='studentbulkupload',
            name='date_uploaded',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
