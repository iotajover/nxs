# Generated by Django 2.2.7 on 2019-11-13 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Studen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('value', models.DecimalField(decimal_places=4, max_digits=14)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Professor')),
                ('studen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Studen')),
            ],
        ),
    ]
