from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
import re
from a_tenant_manager.models import *


class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'schema_name']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Add Name ...'}),
            'schema_name' : forms.TextInput(attrs={'placeholder': 'Add Subdomain ...'}),
        } 
        
    def clean_schema_name(self):
        schema_name = self.cleaned_data['schema_name'].lower() 

        if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', schema_name):
            raise ValidationError("Subdomains can only contain lowercase letters, numbers, and hyphens!")
        
        if Tenant.objects.filter(schema_name=schema_name).exists():
            raise ValidationError("This subdomain is already taken.")
        
        return schema_name
