from novaclient import client
from drivers.OpenStack.APIs.keystone.keystone import get_session, get_session_servers
from vims.models import Vim


def get_flavors(vnf):
    vims = Vim.objects.all()
    for vim in vims:
        nova = client.Client(2, session=get_session(vim))
        try:
            flavor = nova.flavors.find(vcpus=vnf.cpu, ram=vnf.ram, disk=vnf.disk)
        except:
            flavor = nova.flavors.create(name=vnf.name, ram=vnf.ram, vcpus=vnf.cpu, disk=vnf.disk, flavorid='auto', ephemeral=0, swap=0, rxtx_factor=1.0, is_public=True)

        flavor = flavor.name

    return flavor


def create_snapshot(vnf):
    vims = Vim.objects.all()
    nova = client.Client(2, session=get_session_servers(vnf.operator, vims[0]))
    server = nova.servers.list()
    nova.servers.create_image(server[0].id, vnf.name)

    print "snapshot"
