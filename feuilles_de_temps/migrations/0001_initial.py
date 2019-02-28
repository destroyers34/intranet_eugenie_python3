# Generated by Django 2.1.5 on 2019-02-22 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ressources', '0001_initial'),
        ('projets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('temps', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Temps')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ressources.Employe', verbose_name='Employé')),
            ],
            options={
                'verbose_name': 'Bloc Banque',
                'verbose_name_plural': 'Blocs Banque',
                'permissions': (('afficher_rapport_banque', 'Afficher un rapport de temps des heures en banque'),),
            },
        ),
        migrations.CreateModel(
            name='Bloc_Eugenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('temps', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Temps')),
                ('note', models.TextField(blank=True, max_length=200, verbose_name='Commentaires')),
                ('banque', models.BooleanField(default=False, verbose_name='Heures Banque')),
                ('approuve', models.BooleanField(default=False, verbose_name='Approuvé')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ressources.Employe', verbose_name='Employé')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projets.Projet_Eugenie', verbose_name='Projet')),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ressources.Tache', verbose_name='Tâche')),
            ],
            options={
                'verbose_name': 'Bloc Eugénie',
                'verbose_name_plural': 'Blocs Eugénie',
                'permissions': (('afficher_rapport_temps_eugenie', 'Afficher un rapport de temps EuGénie'), ('superviseur_eugenie', 'Superviseur pour EuGénie Canada Inc.')),
            },
        ),
        migrations.CreateModel(
            name='Bloc_TPE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('temps', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Temps')),
                ('note', models.TextField(blank=True, max_length=200, verbose_name='Commentaires')),
                ('banque', models.BooleanField(default=False, verbose_name='Heures Banque')),
                ('approuve', models.BooleanField(default=False, verbose_name='Approuvé')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ressources.Employe', verbose_name='Employé')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projets.Projet_TPE', verbose_name='Projet')),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ressources.Tache', verbose_name='Tâche')),
            ],
            options={
                'verbose_name': 'Bloc Techno-Pro Experts',
                'verbose_name_plural': 'Blocs Techno-Pro Experts',
                'permissions': (('afficher_rapport_temps_tpe', 'Afficher un rapport de temps TPE'),),
            },
        ),
    ]
