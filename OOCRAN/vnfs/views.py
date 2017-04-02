from django.shortcuts import render, get_object_or_404, redirect
from .models import Vnf
from images.models import Image
from operators.models import Operator, Provider
from .forms import VnfForm
from nfs.models import Nf
from vims.models import Vim
from django.contrib import messages
from drivers.OpenStack.APIs.nova.nova import get_flavors
from drivers.Vagrant.APIs.api import list_boxes
from django.contrib.auth.decorators import login_required
from OOCRAN.global_functions import paginator
import tasks


@login_required(login_url='/login/')
def list(request):
    queryset_list = Vnf.objects.filter(operator__name=request.user.username)
    queryset = paginator(request, queryset_list)

    context = {
        "user": request.user,
        "object_list": queryset,
    }
    return render(request, "vnfs/list.html", context)


@login_required(login_url='/login/')
def create(request):
    nfs = Nf.objects.filter(operator__name=request.user.username)
    operator = get_object_or_404(Operator, name=request.user.username)

    if operator.vnfm == "Vagrant":
        images = list_boxes(operator)
    else:
        images = Image.objects.all()

    form = VnfForm(request.POST or None, request.FILES or None, nfs=nfs, images=images)
    if form.is_valid():
        try:
            Vnf.objects.get(operator__name=request.user.username, name=form.cleaned_data['name'])
            messages.success(request, "Name repeated!", extra_tags="alert alert-danger")
        except:
            vnf = form.save(commit=False)
            # vnf.flavor = get_flavors(vnf)
            vnf.operator = get_object_or_404(Operator, name=request.user.username)
            vnf.save()
            vnf.add_nf(form.cleaned_data['nf'])
            vim = Vim.objects.all()
            tasks.create_vnf.delay(vnf.id, vim[0].id)
            messages.success(request, "Successfully created!", extra_tags="alert alert-success")
            return redirect("vnfs:list")
    if form.errors:
        messages.success(request, form.errors, extra_tags="alert alert-danger")
        return redirect("vnfs:list")

    context = {
        "user": request.user,
        "form": form,
    }
    return render(request, "vnfs/form.html", context)


@login_required(login_url='/login/')
def delete(request, id=None):
    instance = get_object_or_404(Vnf, id=id)
    instance.delete()

    messages.success(request, "VNF successfully deleted!", extra_tags="alert alert-success")
    return redirect("vnfs:list")


@login_required(login_url='/login/')
def detail(request, id=None):
    instance = Vnf.objects.get(id=id)
        
    context = {
        "user": request.user,
        "vnf": instance,
    }
    return render(request, "vnfs/detail.html", context)
