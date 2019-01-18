from django.db import models


class Compagnie(models.Model):
    nom = models.CharField(max_length=50, default=u"Entrez un nom", verbose_name=u"Nom")
    adresse = models.CharField(max_length=50, verbose_name=u"Adresse", blank=True)
    ville = models.CharField(max_length=50, verbose_name=u"Ville", blank=True)
    province_etat = models.CharField(max_length=50, verbose_name=u"Province/État", blank=True)
    postal_code = models.CharField(max_length=50, verbose_name=u"Code Postal", blank=True)
    pays = models.CharField(max_length=50, verbose_name=u"Pays", blank=True)
    telephonne = models.CharField(max_length=50, verbose_name=u"Numéro de téléphonne", blank=True)
    fax = models.CharField(max_length=50, verbose_name=u"Numéro de fax", blank=True)

    def __unicode__(self):
        return u'%s' % (self.nom)

    class Meta:
        verbose_name = u"Compagnie"

    ordering = ['nom']


class Contact(models.Model):
    prenom = models.CharField(max_length=50, verbose_name=u"Prénom", blank=True)
    nom = models.CharField(max_length=50, verbose_name=u"Nom", blank=True)
    fonction = models.CharField(max_length=50, verbose_name=u"Fonction", blank=True)
    telephonne = models.CharField(max_length=50, verbose_name=u"Numéro de téléphonne", blank=True)
    email = models.CharField(max_length=50, verbose_name=u"Adresse courriel", blank=True)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE, verbose_name=u"Compagnie")

    def __unicode__(self):
        return u'%s %s - %s' % (self.prenom, self.nom, self.fonction)

    class Meta:
        verbose_name = u"Contact"
        ordering = ['prenom', 'nom']
