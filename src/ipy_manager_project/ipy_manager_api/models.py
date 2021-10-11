from django.db import models
from uuid import uuid4

class network(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)  
    network = models.GenericIPAddressField(protocol='IPv4')
    create_at = models.DateField(auto_now_add=True)
    owner = models.TextField(max_length=30)
    tag  = models.TextField(max_length=10)
    netmask = models.GenericIPAddressField(protocol='IPv4')

class range(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)  
    network = models.GenericIPAddressField(protocol='IPv4')
    create_at = models.DateField(auto_now_add=True)
    owner = models.TextField(max_length=30)
    tag  = models.TextField(max_length=10)


class ip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)  
    ip = models.GenericIPAddressField(protocol='IPv4')
    in_use = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    owner = models.TextField(max_length=30)
    tag  = models.TextField(max_length=10)
    
    class Meta:
        ordering = ['-create_at']



