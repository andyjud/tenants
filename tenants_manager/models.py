from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    auto_create_schema = True
    auto_drop_schema = True
    
class Domain(DomainMixin):
    pass
