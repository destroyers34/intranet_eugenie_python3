from django import template
from gpao.models import Piece

register = template.Library()

@register.filter(name='get_piece_display')
def get_piece_display(value):
    try:
        return Piece.objects.get(id=value).__unicode__()
    except:
        return None
