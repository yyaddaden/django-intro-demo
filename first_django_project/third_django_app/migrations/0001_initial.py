# Generated by Django 3.1.3 on 2020-12-12 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('initial_val', models.FloatField()),
                ('final_val', models.FloatField()),
                ('initial_met', models.CharField(choices=[('C', 'Celsieus'), ('F', 'Fahrenheit')], max_length=1)),
                ('final_met', models.CharField(choices=[('C', 'Celsieus'), ('F', 'Fahrenheit')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='third_django_app.user')),
            ],
        ),
    ]
