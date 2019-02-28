# Generated by Django 2.1.5 on 2019-02-22 20:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet_Eugenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=30, unique=True, verbose_name='Numéro du projet')),
                ('nom', models.CharField(default='X', max_length=30, verbose_name='Nom du projet')),
                ('date_soumission', models.DateField(blank=True, null=True, verbose_name='Date de soumission')),
                ('date_debut', models.DateField(default=django.utils.timezone.now, verbose_name='Date de début')),
                ('date_fin', models.DateField(default=django.utils.timezone.now, verbose_name='Date de fin')),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('en_attente', models.BooleanField(verbose_name='En attente')),
                ('modele', models.CharField(default='X', max_length=30, verbose_name='Modèle')),
                ('serial_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Numéro de série')),
                ('budget_mat', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Budget MAT ($)')),
                ('budget_mo', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Budget MO (H)')),
                ('priority', models.DecimalField(decimal_places=0, default='9', max_digits=2, verbose_name='Priorité')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Compagnie', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Projet EuGénie',
                'verbose_name_plural': 'Projets EuGénie',
                'ordering': ['-numero'],
            },
        ),
        migrations.CreateModel(
            name='Projet_TPE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=30, unique=True, verbose_name='Numéro du projet')),
                ('nom', models.CharField(default='X', max_length=30, verbose_name='Nom du projet')),
                ('date_soumission', models.DateField(blank=True, null=True, verbose_name='Date de soumission')),
                ('date_debut', models.DateField(default=django.utils.timezone.now, verbose_name='Date de début')),
                ('date_fin', models.DateField(default=django.utils.timezone.now, verbose_name='Date de fin')),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('en_attente', models.BooleanField(verbose_name='En attente')),
                ('description', models.CharField(default='X', max_length=30, verbose_name='Description')),
                ('serial_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Numéro de série')),
                ('budget_mat', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Budget MAT ($)')),
                ('budget_mo', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Budget MO (H)')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Compagnie', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Projet Techno-Pro Experts',
                'verbose_name_plural': 'Projets Techno-Pro Experts',
                'ordering': ['-numero'],
            },
        ),
    ]