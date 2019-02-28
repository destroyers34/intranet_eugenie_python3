from models import *
from django.db.models import Sum, Count

def employe_cdd_detail(request):
    factures = Depense_Eci.objects.filter(employe=request.user.id,paye=False)[:10]
    fac_total = factures.aggregate(total=Sum('montant') + Sum('tps') + Sum('tvq'), nb_fac=Count('id'))
    return {
        'factures':  factures,
        'fac_total': fac_total,
        'user':      request.user,
    }