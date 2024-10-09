from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    auto_create_schema = True
    auto_drop_schema = True

class Domain(DomainMixin):
    pass


class TenantMember(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('designer', 'Designer'),
        ('programmer', 'Programmer'),
    ]
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True, default='') 
    
    class Meta:
        unique_together = ('user', 'tenant')
        
    def __str__(self):
        return f"{self.tenant.name} - {self.user.profile.name}{' (Admin)' if self.is_admin else ''}"
