from django.core.files.storage import FileSystemStorage
from django.db import connection
from django_tenants.files.storage import TenantFileSystemStorage

class DynamicStorage:
    def __init__(self, *args, **kwargs):
        self.public_storage = FileSystemStorage()
        self.tenant_storage = TenantFileSystemStorage()

    def _get_storage_backend(self):
        schema_name = connection.schema_name
        if schema_name == 'public':
            return self.public_storage
        else:
            return self.tenant_storage

    def save(self, name, content, max_length=None):
        storage_backend = self._get_storage_backend()
        return storage_backend.save(name, content, max_length)

    def url(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.url(name)
    
    def generate_filename(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.get_available_name(name)
    
    def delete(self, name):
        storage_backend = self._get_storage_backend()
        storage_backend.delete(name)
