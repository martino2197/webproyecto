# Generated by Django 2.0.4 on 2018-05-09 02:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('padmex', '0003_auto_20180507_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=20)),
                ('cliente_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padmex.Cliente')),
            ],
        ),
    ]