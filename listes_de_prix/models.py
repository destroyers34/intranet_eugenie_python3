from django.db import models
from ressources.models import Devise
from decimal import *


class Categorie(models.Model):
    nom = models.CharField(verbose_name=u"Nom", max_length=30, unique=True)
    nom_en = models.CharField(verbose_name=u"Nom Anglais", max_length=30, unique=True)

    def __unicode__(self):
        return u"%s" % self.nom

    class Meta:
        ordering = ['nom', 'nom_en']


class Fournisseur(models.Model):
    nom = models.CharField(verbose_name=u"Nom", max_length=100)
    telephonne = models.CharField(verbose_name=u"Numéro de téléphonne", max_length=100, blank=True, null=True)
    fax = models.CharField(verbose_name=u"Numéro de fax", max_length=100, blank=True, null=True)
    siteweb = models.CharField(verbose_name=u"Site web", max_length=100, blank=True, null=True)
    devise = models.ForeignKey(Devise, on_delete=models.PROTECT, verbose_name=u"Devise")
    ratio = models.DecimalField(verbose_name=u"Ratio", max_digits=5, decimal_places=2, default='1')
    ratio_us = models.DecimalField(verbose_name=u"Ratio US", max_digits=5, decimal_places=2, default='1')
    actif = models.BooleanField(verbose_name=u"Actif")

    def __unicode__(self):
        return u"%s" % self.nom

    class Meta:
        ordering = ['nom']


class Machinerie(models.Model):
    numero = models.CharField(verbose_name=u"Numéro", max_length=100, unique=True)
    details = models.TextField(verbose_name=u"Détails", blank=True, null=True)
    details_en = models.TextField(verbose_name=u"Détails Anglais", blank=True, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.PROTECT, verbose_name=u"Fournisseur")
    prix_fournisseur = models.DecimalField(verbose_name=u"Prix du fournisseur", max_digits=9, decimal_places=2)
    dateprix = models.DateField(verbose_name=u"Date du prix", null=True, blank=True)
    escompte = models.DecimalField(verbose_name=u"Escompte (%)", max_digits=5, decimal_places=2, default='0')
    ratio = models.DecimalField(verbose_name=u"Ratio", max_digits=5, decimal_places=2, default='0')
    ratio_us = models.DecimalField(verbose_name=u"Ratio US", max_digits=5, decimal_places=2, default='0')

    class Meta:
        abstract = True
        permissions = (("afficher_listes_prix", "Afficher les listes de prix"),
                       ("afficher_listes_prix_en", "Afficher les listes de prix US"))
        ordering = ['numero']
    
    def prixCAD(self):
        return self.fournisseur.devise.toCAD(self.prix_fournisseur)
    prixCAD.short_description = 'Prix ($ CAD)'

    def prixUS(self):
        taux = Devise.objects.get(code_iso='USD')
        if taux:
            return self.fournisseur.devise.toCAD(self.prix_fournisseur) * taux.taux_inverse
        else:
            return 0
    prixUS.short_description = 'Price ($ US)'
    
    def cost(self):
        taux = Devise.objects.get(code_iso='CAD')
        if taux:
            pourcentage = 1 - (self.escompte / 100)
            return self.prix_fournisseur * pourcentage * taux.taux_toCAD
        else:
            return 0
    cost.short_description = 'Cost ($ CAD)'
    
    def ratioEffectif(self):
        if self.ratio == 0:
            ratio = self.fournisseur.ratio
        else:
            ratio = self.ratio
        return ratio
    ratioEffectif.short_description = 'Ratio'

    def ratioEffectifUs(self):
        if self.ratio_us == 0:
            ratio = self.fournisseur.ratio_us
        else:
            ratio = self.ratio_us
        return ratio
    ratioEffectifUs.short_description = 'Ratio US'

    def plMin(self):
        return self.prixCAD() * self.ratioEffectif()
    plMin.short_description = 'Prix Vente ($ CAD)'

    def plMinUS(self):
        if self.prixUS() != 0:
            return self.prixUS() * self.ratioEffectif() * self.ratioEffectifUs()
        else:
            return 'Inconnu'
    plMinUS.short_description = 'Prix Vente ($ US)'

    def profit(self):
        return self.plMin() - Decimal(self.cost())
    profit.short_description = 'Profit ($ CAD)'

    def profitUs(self):
        taux = Devise.objects.get(code_iso='USD')
        if taux:
            return self.plMinUS() * taux.taux_toCAD - self.cost()
        else:
            return 0
    profitUs.short_description = 'Profit ($ CAD)'

    def profit_pourcent(self):
        return self.profit() / self.plMin() * 100
    profit_pourcent.short_description = 'Profit (% Brute)'

    def profit_pourcentUs(self):
        taux = Devise.objects.get(code_iso='USD')
        if taux:
            return self.profitUs() / (self.plMinUS() * taux.taux_toCAD) * 100
        else:
            return 0
    profit_pourcentUs.short_description = 'Profit (% Brute)'


class Machine(Machinerie):
    description = models.CharField(max_length=50, verbose_name=u"Nom", blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, verbose_name=u"Catégorie")
    actif = models.BooleanField(verbose_name=u"Actif")

    def __unicode__(self):
        if self.description:
            return u"%s - %s" % (self.numero, self.description)
        else:
            return u"%s" % self.numero


class Option(Machinerie):
    machines = models.ManyToManyField(Machine, related_name='options_machine')

    def __unicode__(self):
        if self.details:
            if len(self.details) > 50:
                return u"%s - %s..." % (self.numero, self.details[0:50])
            else:
                return u"%s - %s" % (self.numero, self.details)