# Generated by Django 4.2.9 on 2024-01-18 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('integrators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PointOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=50)),
                ('terminal_id', models.CharField(max_length=16)),
                ('brand', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pops', to='pops.location')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('MCC', models.PositiveSmallIntegerField(default=0)),
                ('integrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchants', to='integrators.integrator')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='pops.merchant'),
        ),
    ]
