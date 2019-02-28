from django.db import models
from projets.models import Projet_Eugenie


class Categorie(models.Model):
    nom = models.CharField(max_length=60, verbose_name=u"Catégorie", unique=True)

    def __unicode__(self):
        return u'%s' % self.nom

    class Meta:
        verbose_name = u"Catégorie"
        ordering = ['nom']


class Fournisseur(models.Model):
    nom = models.CharField(verbose_name=u"Nom", max_length=100, unique=True)

    def __unicode__(self):
        return u"%s" % self.nom

    class Meta:
        verbose_name = u"Fournisseur"
        ordering = ['nom']


class Materiel_Eugenie(models.Model):
    date = models.DateField(verbose_name=u"Date")
    projet = models.ForeignKey(Projet_Eugenie, on_delete=models.PROTECT, verbose_name=u"Projet")
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.PROTECT, verbose_name=u"Fournisseur", null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, verbose_name=u"Catégorie")
    montant = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=u"Montant")

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.date, self.projet, self.fournisseur, self.categorie, self.montant)

    class Meta:
        verbose_name = u"Matériel Eugénie"
        verbose_name_plural = u"Matériel Eugénie"

