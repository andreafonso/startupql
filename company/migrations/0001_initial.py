# Generated by Django 2.1.7 on 2019-03-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_city', models.ForeignKey(on_delete='cascade', related_name='employee_city', to='company.City')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_title',
            field=models.ForeignKey(on_delete='cascade', related_name='employee_title', to='company.Title'),
        ),
    ]
