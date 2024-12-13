# Generated by Django 5.1.2 on 2024-10-31 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('gender_type', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('department', models.CharField(max_length=200)),
                ('date_of_join', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.PositiveIntegerField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='employee')),
            ],
        ),
    ]