# Generated by Django 3.2.25 on 2024-03-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20240320_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='electricity',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newapp.user'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.user'),
        ),
    ]
