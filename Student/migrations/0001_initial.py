# Generated by Django 3.0.4 on 2020-07-03 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Classe')),
            ],
        ),
        migrations.AddField(
            model_name='classe',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.School'),
        ),
    ]
