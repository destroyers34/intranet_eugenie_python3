from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Compagnie(models.Model):
    nom = models.CharField(max_length=60, verbose_name=u"Nom")
    code = models.CharField(max_length=3, verbose_name=u"Code", null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.nom
            
    class Meta:
        verbose_name = u"Compagnie"


class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.SET_NULL, verbose_name=u"Compagnie", blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True, verbose_name=u"Date d'embauche")
    banque_heure = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=u"Heure(s) en banque", default=0.00)
    taux_horaire = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Taux horaire", default=0.00)
    superviseur = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)
            
    class Meta:
        verbose_name = u"Employé"
        ordering = ['user__first_name']

    def get_Name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)
    get_Name.short_description = 'Nom'


class Devise(models.Model):
    nom = models.CharField(verbose_name=u"Nom", max_length=100)
    code_iso = models.CharField(verbose_name=u"Code ISO", max_length=3)
    symbole = models.CharField(verbose_name=u"Symbole", max_length=3)
    taux_toCAD = models.DecimalField(verbose_name=u"Taux vers ($CA)", max_digits=13, decimal_places=10, default='1')
    taux_inverse = models.DecimalField(verbose_name=u"Taux inverse", max_digits=13, decimal_places=10, default='1')
    date_taux = models.DateField(verbose_name=u"Date des taux")

    def __unicode__(self):
        return u"%s (%s)" % (self.nom, self.symbole)

    def toCAD(self, price):
        return price * self.taux_toCAD
    
    def toDevise(self, price):
        return price * self.taux_inverse


class Tache(models.Model):
    POSITIF = 'PO'
    NEGATIF = 'NE'
    TASK_MODE = (
        (POSITIF, 'Positif'),
        (NEGATIF, 'Négatif'),
    )
    numero = models.CharField(max_length=10, verbose_name=u"Numéro")
    description = models.CharField(max_length=60, verbose_name=u"Description")
    type = models.CharField(max_length=2, choices=TASK_MODE, default=POSITIF, verbose_name=u"Type de tache:")

    def __unicode__(self):
        return u'%s %s' % (self.numero, self.description)

    class Meta:
        verbose_name = u"Tâche"
        ordering = ['numero']


class Compte_gl(models.Model):
    DEBIT = 'DT'
    CREDIT = 'CT'
    BLANK = ' '
    TASK_MODE = (
        (DEBIT, 'DT'),
        (CREDIT, 'CT'),
        (BLANK, ' ')
    )
    POSTE = '0'
    RUBRIQUE = '1'
    TOTAL = '2'
    TITRE = '3'
    COMPTE_TYPE = (
        (POSTE, 'Poste'),
        (RUBRIQUE, 'Rubrique'),
        (TOTAL, 'Total'),
        (TITRE, 'Titre')
    )
    numero = models.IntegerField(verbose_name=u"Numéro")
    description = models.CharField(max_length=60, verbose_name=u"Description")
    sens = models.CharField(max_length=2, choices=TASK_MODE, default=BLANK, verbose_name=u"Sens du solde")
    devise = models.ForeignKey(Devise, on_delete=models.SET_NULL, verbose_name=u"Devise", blank=True, null=True)
    type = models.CharField(max_length=1, choices=COMPTE_TYPE, default=BLANK, verbose_name=u"Type de compte")
    solde = models.DecimalField(max_digits=12, decimal_places=3, verbose_name=u"Solde", default=0.00)
    inactif = models.BooleanField(verbose_name=u"Inactif", default=False)
    employe = models.ForeignKey(Employe, on_delete=models.SET_NULL, blank=True, null=True)
    def __unicode__(self):
        return u'%s %s' % (self.numero, self.description)