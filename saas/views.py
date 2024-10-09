from django.shortcuts import render, redirect
from django.core.management import call_command
from django_tenants.utils import schema_context
from django.contrib.auth import login
from django.conf import settings
from a_tenant_manager.models import *
from .forms import TenantForm

def home_view(request):
    tenant_form = TenantForm()
    
    if request.method == "POST":
        tenant_form = TenantForm(request.POST)
        if tenant_form.is_valid():
            tenant = tenant_form.save()
            
            # No need call_command actually
            # call_command('migrate_schemas', schema_name=tenant.schema_name)
            
            domain = Domain.objects.create(
                tenant=tenant,
                domain=f"{tenant.schema_name}.{settings.BASE_URL}",
                is_primary=True
            )
            
            TenantMember.objects.create(
                user=request.user,
                tenant=tenant,
                is_admin=True
            )
            
            with schema_context(tenant.schema_name):  
                request.user.backend = 'allauth.account.auth_backends.AuthenticationBackend'
                login(request, request.user)
            
            return redirect(f"http://{domain.domain}{settings.PORT}")
    
    # Check if user is a tenant member
    try:
        tenant_member = TenantMember.objects.get(user=request.user, tenant=request.tenant)
    except:
        tenant_member = None 
    
    # Get the list of tenants for the user
    if request.user.is_authenticated:
        user_tenants = TenantMember.objects.filter(user=request.user)
    else:
        user_tenants = []
        
    base_domain = f"{settings.BASE_URL}{settings.PORT}"
    
    if not hasattr(request, 'tenant'):
        template_name = 'home.html'
    else:
        template_name = 'home_tenant.html' 
    
    context = {
        'tenant_form': tenant_form,
        'tenant_member': tenant_member,
        'user_tenants' : user_tenants,
        'base_domain': base_domain,
        'member_roles': TenantMember.ROLE_CHOICES,
    }    
    return render(request, template_name, context)


def tenant_member_role(request, tenant_id):
    if request.method == "POST":
        role = request.POST.get('role')
        tenant = Tenant.objects.get(id=tenant_id)
        
        tenant_member, created = TenantMember.objects.get_or_create(
            user=request.user,
            tenant=tenant,
        )
        tenant_member.role = role.lower()
        tenant_member.save()
        
        return redirect(f"http://{tenant.schema_name}.{settings.BASE_URL}{settings.PORT}")
