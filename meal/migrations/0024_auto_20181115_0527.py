# Generated by Django 2.1.3 on 2018-11-15 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('meal', '0023_auto_20181115_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('totalsum', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'ckecks',
            },
        ),
        migrations.CreateModel(
            name='MealsToOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('meals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mealstoorders', to='meal.Meal')),
            ],
            options={
                'verbose_name_plural': 'mealstoorders',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablename', models.CharField(default='table1', max_length=250)),
                ('date', models.CharField(max_length=300)),
                ('isitopen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='meal.Status')),
                ('tableid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='meal.Table')),
                ('waiterid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='user.User')),
            ],
            options={
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.AddField(
            model_name='mealstoorder',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mealstoorders', to='meal.Order'),
        ),
        migrations.AddField(
            model_name='check',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checks', to='meal.Order'),
        ),
        migrations.AddField(
            model_name='check',
            name='servicefee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checks', to='meal.ServicePercentage'),
        ),
    ]