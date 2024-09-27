from django.core.files.storage import FileSystemStorage
from django.db import connection
from django_tenants.files.storage import TenantFileSystemStorage
from django.conf import settings
from storages.backends.s3 import S3Storage

class CustomSchemaStorage:
    def _get_storage_backend(self):
        schema_name = connection.schema_name
        if settings.ENVIRONMENT == 'development':
            if schema_name == 'public':
                return FileSystemStorage()
            else:
                return TenantFileSystemStorage()
        else:
            if schema_name == 'public':
                return S3Storage() 
            else:
                return S3TenantStorage(schema_name)

    def save(self, name, content, max_length=None):
        storage_backend = self._get_storage_backend()
        return storage_backend.save(name, content, max_length)

    def url(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.url(name)
    
    def generate_filename(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.generate_filename(name)

    def delete(self, name):
        storage_backend = self._get_storage_backend()
        storage_backend.delete(name)
        
        
class S3TenantStorage(S3Storage):
    def __init__(self, schema_name):
        super().__init__()
        self.schema_name = schema_name
        
    def save(self, name, content, max_length=None):
        path = f"{settings.MULTITENANT_RELATIVE_MEDIA_ROOT % self.schema_name}/{name}"
        return super().save(path, content, max_length)
