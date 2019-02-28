# coding: utf-8
from django.db import models
from ressources.models import Compte_gl, Employe
from projets.models import *


def upload_path(self, filename):
        return 'factures/%s/%s/%s/%s' % (self.date.strftime("%Y"),self.date.strftime("%m"),self.date.strftime("%d"), filename)

# Create your models here.
class Depense_Eci(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.PROTECT, verbose_name=u"Employé")
    date = models.DateField(verbose_name=u"Date")
    detail = models.CharField(max_length=50,verbose_name=u"Détails")
    projet = models.ForeignKey(Projet_Eugenie, on_delete=models.PROTECT, verbose_name=u"Numéro de projet")
    gl = models.ForeignKey(Compte_gl, on_delete=models.PROTECT, verbose_name=u"GL")
    montant = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"Montant sans taxes", default=0.00)
    tps = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"TPS/TVH", default=0.00)
    tvq = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"TVQ", default=0.00)
    photo = models.ImageField(upload_to=upload_path, blank=True)
    approuve = models.BooleanField(verbose_name=u"Approuvé?", default=False)
    paye = models.BooleanField(verbose_name=u"Payé?", default=False)
    approved_by = models.ForeignKey(Employe, on_delete=models.PROTECT, verbose_name=u"Approuvé par", related_name="approving_employe",null=True, blank=True,)
    approved_on = models.DateTimeField(verbose_name=u"Approuvé le", null=True, blank=True,)

    def fac_total(self):
        return self.montant + self.tps + self.tvq
    fac_total.short_description = 'Total'

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.photo)
    image_thumb.allow_tags = True

    def __str__(self):
        return 'ECI_%s: %s - %s - %s - %s - %s$' % (self.id, self.date, self.detail, self.projet, self.gl, self.fac_total())

    class Meta:
        verbose_name = u"Dépense Eugénie Canada"
        verbose_name_plural = u"Dépenses Eugénie Canada"
        permissions = (
            ("creer_cdd_eci", "Creer une depense EuGénie"),
            ("admin_cdd_eci", "Superviseur pour EuGénie Canada Inc."),
        )


class Petite_Caisse_Eci(models.Model):
    date = models.DateField(verbose_name=u"Date")
    employe = models.ForeignKey(Employe, on_delete=models.PROTECT, verbose_name=u"Employé")
    detail = models.CharField(max_length=50,verbose_name=u"Détails")
    projet = models.ForeignKey(Projet_Eugenie, on_delete=models.PROTECT, verbose_name=u"Numéro de projet")
    gl = models.ForeignKey(Compte_gl, on_delete=models.PROTECT, verbose_name=u"GL")
    montant = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"Montant sans taxes", default=0.00)
    tps = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"TPS/TVH", default=0.00)
    tvq = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"TVQ", default=0.00)
    nb_penny = models.IntegerField(verbose_name=u"Nombre de 1 sous", default=0)
    nb_nickel = models.IntegerField(verbose_name=u"Nombre de 5 sous", default=0)
    nb_dime = models.IntegerField(verbose_name=u"Nombre de 10 sous", default=0)
    nb_quarter = models.IntegerField(verbose_name=u"Nombre de 25 sous", default=0)
    nb_un = models.IntegerField(verbose_name=u"Nombre de 1$", default=0)
    nb_deux = models.IntegerField(verbose_name=u"Nombre de 2$", default=0)
    nb_cinq = models.IntegerField(verbose_name=u"Nombre de billet de 5", default=0)
    nb_dix = models.IntegerField(verbose_name=u"Nombre de billet de 10", default=0)
    nb_vingt = models.IntegerField(verbose_name=u"Nombre de billet de 20", default=0)
    nb_cinquante = models.IntegerField(verbose_name=u"Nombre de billet de 50", default=0)
    nb_cent = models.IntegerField(verbose_name=u"Nombre de billet de 100", default=0)

    def fac_total(self):
        return self.montant + self.tps + self.tvq
    fac_total.short_description = 'Total'

    def __str__(self):
        return 'ECI_%s: %s - %s - %s - %s - %s$' % (self.id, self.date, self.detail, self.projet, self.gl, self.fac_total())

    class Meta:
        verbose_name = u"Petite caisse Eugénie Canada"
        verbose_name_plural = u"Petite caisse Eugénie Canada"
        permissions = (
            ("creer_pc_eci", "Creer depense petite caisse EuGénie"),
            ("admin_pc_eci", "Superviseur pour EuGénie Canada Inc."),
        )


class Depense_Tpe(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.PROTECT, verbose_name=u"Employé")
    date = models.DateField(verbose_name=u"Date")
    detail = models.CharField(max_length=50,verbose_name=u"Détails")
    projet = models.ForeignKey(Projet_TPE, on_delete=models.PROTECT, verbose_name=u"Numéro de projet")
    gl = models.ForeignKey(Compte_gl, on_delete=models.PROTECT, verbose_name=u"GL")
    montant = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"Montant sans taxes", default=0.00)
    tps = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"TPS/TVH", default=0.00)
    tvq = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"TVQ", default=0.00)
    photo = models.ImageField(upload_to=upload_path, blank=True)
    approuve = models.BooleanField(verbose_name=u"Approuvé?", default=False)
    paye = models.BooleanField(verbose_name=u"Payé?", default=False)
    approved_by = models.ForeignKey(Employe, on_delete=models.PROTECT, verbose_name=u"Approuvé par", related_name="approving_employe_tpe",null=True, blank=True,)
    approved_on = models.DateTimeField(verbose_name=u"Approuvé le", null=True, blank=True,)

    def fac_total(self):
        return self.montant + self.tps + self.tvq
    fac_total.short_description = 'Total'

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.photo)
    image_thumb.allow_tags = True

    def __str__(self):
        return 'TPE_%s: %s - %s - %s - %s - %s$' % (self.id, self.date, self.detail, self.projet, self.gl, self.fac_total())

    class Meta:
        verbose_name = u"Dépense Techno-Pro Expert"
        verbose_name_plural = u"Dépenses Techno-Pro Expert"
        permissions = (
            ("creer_cdd_tpe", "Creer une depense Techno-Pro Expert"),
            ("admin_cdd_tpe", "Superviseur pour Techno-Pro Expert"),
        )