# Generated by Django 2.2.7 on 2020-01-08 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='THPTQG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('A', models.CharField(max_length=5000)),
                ('B', models.CharField(max_length=5000)),
                ('C', models.CharField(max_length=5000)),
                ('D', models.CharField(max_length=5000)),
                ('Answer', models.CharField(max_length=1)),
                ('Exam', models.ForeignKey(blank=True, max_length=11, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='LOP10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('A', models.CharField(max_length=5000)),
                ('B', models.CharField(max_length=5000)),
                ('C', models.CharField(max_length=5000)),
                ('D', models.CharField(max_length=5000)),
                ('Answer', models.CharField(max_length=1)),
                ('Exam', models.ForeignKey(blank=True, max_length=11, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Exam')),
            ],
        ),
    ]
