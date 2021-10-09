# Generated by Django 3.2.8 on 2021-10-09 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_model_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='cars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='main_app.cars'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=50)),
                ('models', models.ManyToManyField(to='main_app.Model')),
            ],
        ),
    ]
