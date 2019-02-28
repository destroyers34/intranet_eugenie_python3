from django.db import models

from projets.models import Projet_Eugenie, Projet_TPE
from ressources.models import Employe, Tache


class Bloc(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.PROTECT, verbose_name=u"Employé")
    date = models.DateField(verbose_name=u"Date")
    tache = models.ForeignKey(Tache, on_delete=models.PROTECT, verbose_name=u"Tâche")
    temps = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=u"Temps")
    note = models.TextField(max_length=200, blank=True, verbose_name=u"Commentaires")
    banque = models.BooleanField(verbose_name=u"Heures Banque", default=False)
    approuve = models.BooleanField(verbose_name=u"Approuvé", default=False)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.employe, self.date, self.projet, self.tache, self.temps)
        
    def get_Name(self):
        return self.employe.get_Name()
    get_Name.short_description = 'Nom'

    def get_Cout(self):
        return self.temps * self.employe.taux_horaire

    get_Cout.short_description = 'Cout'

    class Meta:
        abstract = True


class Bloc_Eugenie(Bloc):
    projet = models.ForeignKey(Projet_Eugenie, on_delete=models.PROTECT, verbose_name=u"Projet")

    class Meta:
        verbose_name = u"Bloc Eugénie"
        verbose_name_plural = u"Blocs Eugénie"
        permissions = (
            ("afficher_rapport_temps_eugenie", "Afficher un rapport de temps EuGénie"),
            ("superviseur_eugenie", "Superviseur pour EuGénie Canada Inc."),
        )


class Bloc_TPE(Bloc):
    projet = models.ForeignKey(Projet_TPE, on_delete=models.PROTECT, verbose_name=u"Projet")

    class Meta:
        verbose_name = u"Bloc Techno-Pro Experts"
        verbose_name_plural = u"Blocs Techno-Pro Experts"
        permissions = (("afficher_rapport_temps_tpe", "Afficher un rapport de temps TPE"),)
        
#class Bloc_JRC(Bloc):


class Banque(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.PROTECT, verbose_name=u"Employé")
    date = models.DateField(verbose_name=u"Date")
    temps = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=u"Temps")

    class Meta:
        verbose_name = u"Bloc Banque"
        verbose_name_plural = u"Blocs Banque"
        permissions = (("afficher_rapport_banque", "Afficher un rapport de temps des heures en banque"),)
        
    def __unicode__(self):
        return u'%s %s %s' % (self.employe, self.date, self.temps)
    
    def save(self, *args, **kwargs):
        employe = Employe.objects.get(id=self.employe.id)
        employe.banque_heure += self.temps
        employe.save()
        super(Banque, self).save(*args, **kwargs)