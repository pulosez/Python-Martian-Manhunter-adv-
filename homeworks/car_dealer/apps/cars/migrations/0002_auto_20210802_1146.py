# Generated by Django 3.2.5 on 2021-08-02 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.color'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.model'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='picture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.picture'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='property',
            field=models.ManyToManyField(to='cars.Property'),
        ),
    ]