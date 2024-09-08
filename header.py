from django.template import Library
from a_home.models import SiteSetting

register = Library() 

@register.inclusion_tag('includes/header.html') 
def header_view(request):
    branding = SiteSetting.objects.first()
    if branding:
        color = branding.color
    else:
        color = None
 
    context = {
        'request' : request,
        'color' : color,
    }
    return context
