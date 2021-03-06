"""
    Open Orchestrator Cloud Radio Access Network

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Vim, Device, OpenStack, Azure, Aws, Gce
from operators.models import Operator
from images.models import Image
from oocran.global_functions import paginator
from django.contrib.admin.views.decorators import staff_member_required
from .forms import VimForm
from django.contrib.auth.decorators import login_required
from celery import task
from drivers.OpenStack.APIs.keystone.keystone import create_user, delete_user
from drivers.OpenStack.deployments.operator import create_operator


@login_required(login_url='/login/')
def list(request):
    """
    Show list of registered PoP
    :param request:
    :return:
    """
    vims = Vim.objects.all()

    context = {
        "user": request.user,
        "vims": vims,
    }
    return render(request, "vims/list.html", context)


@staff_member_required
def delete(request, id=None):
    """
    Delete PoP with ID id
    :param request:
    :param id:
    :return:
    """
    vim = get_object_or_404(Vim, id=id)
    vim.delete()

    messages.success(request, "VIM successfully deleted!", extra_tags="alert alert-success")
    return redirect("vims:list")


@task()
def add_actual_users(id):
    """
    Register actual operators to the new PoP with ID id
    :param id:
    :return:
    """
    operators = Operator.objects.exclude(name='admin')
    vim = Vim.objects.get(id=id)
    if vim.type == "OpenStack":
        vim = OpenStack.objects.get(name=vim.name)
    for operator in operators:
        create_user(operator, vim)
        create_operator(operator, vim)


@staff_member_required
def create(request):
    """
    Create new PoP
    :param request:
    :return:
    """
    form = VimForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            Vim.objects.get(name=form.cleaned_data['name'])
            messages.success(request, "Name repeated!", extra_tags="alert alert-danger")
        except:
            if form.cleaned_data['type'] == 'OpenStack':
                if form.cleaned_data['password'] == form.cleaned_data['password_confirmation']:
                    vim = OpenStack.objects.create(name=form.cleaned_data['name'],
                                                    ip=form.cleaned_data['ip'],
                                                    longitude=form.cleaned_data['longitude'],
                                                    latitude=form.cleaned_data['latitude'],
                                                    type=form.cleaned_data['type'],
                                                    password=form.cleaned_data['password'],
                                                    username = form.cleaned_data['username'],
                                                    project_domain = form.cleaned_data['project_domain'],
                                                    project = form.cleaned_data['project'],
                                                    public_network = form.cleaned_data['public_network'],
                                                    domain = form.cleaned_data['domain'],
                                                    )
                    vim.password = vim.encrypt(form.cleaned_data['password'])
                    vim.set_public_network()
                    vim.save()
                else:
                    messages.success(request, "Passwords are different!", extra_tags="alert alert-danger")
            elif form.cleaned_data['type'] == 'AWS':
                vim = Aws.objects.create(name=form.cleaned_data['name'],
                                            ip=form.cleaned_data['ip'],
                                            longitude=form.cleaned_data['longitude'],
                                            latitude=form.cleaned_data['latitude'],
                                            type=form.cleaned_data['type'],
                                            access_key_id=form.cleaned_data['access_key_id'],
                                            secret_access_key = form.cleaned_data['secret_access_key'],
                                            session_token = form.cleaned_data['session_token'],
                                            keypair_name  = form.cleaned_data['keypair_name'],
                                            )
                vim.secret_access_key = vim.encrypt(form.cleaned_data['secret_access_key'])
                vim.save()
            elif form.cleaned_data['type'] == 'Azure':
                vim = Azure.objects.create(name=form.cleaned_data['name'],
                                            ip=form.cleaned_data['ip'],
                                            longitude=form.cleaned_data['longitude'],
                                            latitude=form.cleaned_data['latitude'],
                                            type=form.cleaned_data['type'],
                                            tenant_id = form.cleaned_data['tenant_id'],
                                            client_id = form.cleaned_data['client_id'],
                                            client_secret = form.cleaned_data['client_secret'],
                                            subscription_id = form.cleaned_data['subscription_id'],
                                            )
                vim.client_secret = vim.encrypt(form.cleaned_data['client_secret'])
                vim.save()
            elif form.cleaned_data['type'] == 'GCE':
                vim = Gce.objects.create(name=form.cleaned_data['name'],
                                            ip=form.cleaned_data['ip'],
                                            longitude=form.cleaned_data['longitude'],
                                            latitude=form.cleaned_data['latitude'],
                                            type=form.cleaned_data['type'],
                                            google_project_id=form.cleaned_data['google_project_id'],
                                            google_client_email = form.cleaned_data['google_client_email'],
                                            google_json_key_location = form.cleaned_data['google_json_key_location'],
                                            )
                vim.save()

            add_actual_users.delay(id=vim.id)
            messages.success(request, "VIM successfully register!", extra_tags="alert alert-success")
            return redirect("vims:list")
    if form.errors:
        messages.success(request, form.errors, extra_tags="alert alert-danger")
        return redirect("vims:list")

    context = {
        "user": request.user,
        "form": form,
    }
    return render(request, "vims/form.html", context)


@login_required(login_url='/login/')
def details(request, id=None):
    """
    Show details about PoP with ID id
    :param request:
    :param id:
    :return:
    """
    vim = get_object_or_404(Vim, id=id)
    if vim.type == "OpenStack":
        vim = get_object_or_404(OpenStack, name=vim.name)
    elif vim.type == "AWS":
        vim = get_object_or_404(Aws, name=vim.name)
    elif vim.type == "GCE":
        vim = get_object_or_404(Gce, name=vim.name)
    elif vim.type == "Azure":
        vim = get_object_or_404(Azure, name=vim.name)

    context = {
        "user": request.user,
        "vim": vim,
    }
    return render(request, "vims/details.html", context)