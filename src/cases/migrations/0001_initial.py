# Generated by Django 5.0.7 on 2024-07-23 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garages', models.IntegerField()),
                ('floors', models.IntegerField()),
                ('year_built', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('url', models.URLField(max_length=255)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='cases.case')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
    ]