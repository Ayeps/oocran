from __future__ import unicode_literals
from django.db import models
from drivers.OpenStack.APIs.neutron.neutron import get_public_network


class Vim(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    hypervisor = models.CharField(max_length=120, null=True, blank=True)
    ip = models.CharField(max_length=120)
    latitude = models.FloatField(max_length=120)
    longitude = models.FloatField(max_length=120)
    username = models.CharField(max_length=120, default="admin")
    password = models.CharField(max_length=120, null=True, blank=True)
    project_domain = models.CharField(max_length=120, default="default")
    project = models.CharField(max_length=120, default="admin")
    public_network = models.CharField(max_length=120, default="network")
    domain = models.CharField(default="default", max_length=120)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def set_public_network(self):
        self.public_network = get_public_network(self)
