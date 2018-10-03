# Generated by Django 2.1 on 2018-09-05 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.CharField(choices=[('cheap', 'Cheap'), ('mid-price', 'Mid-price'), ('expensive', 'Expensive')], max_length=20)),
                ('time', models.CharField(choices=[('soon', 'Soon'), ('long duration', 'Long Duration')], max_length=20)),
                ('kitchen', models.CharField(choices=[('pizza', 'Pizza'), ('fast-food', 'Fast-food'), ('kebab', 'Kebab'), ('dessert', 'Dessert'), ('flat-bread', 'Flat bread'), ('stuffed-vegetables', 'Stuffed vegetables')], max_length=20)),
                ('hunger', models.CharField(choices=[('famished', 'Famished'), ('starving', 'Starving'), ('satisfied', 'Satisfied')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a place title (e.g. Orhan Aspava, Dolmacı etc.', max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.FloatField()),
            ],
            options={
                'ordering': ['-rate'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField()),
                ('vote_datetime', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_votes', to='common.Place')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_votes', to='common.Profile')),
            ],
            options={
                'ordering': ['-rate'],
            },
        ),
        migrations.AddField(
            model_name='condition',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Place'),
        ),
    ]