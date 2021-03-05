# Generated by Django 3.1.7 on 2021-03-02 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('hireDate', models.DateField()),
            ],
            options={
                'verbose_name': '人员信息',
            },
        ),
        migrations.CreateModel(
            name='Vocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('payment', models.IntegerField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ps', to='index.personinfo')),
            ],
            options={
                'verbose_name': '职业信息',
            },
        ),
    ]