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

from __future__ import absolute_import, unicode_literals
from .models import Bbu
from celery import task
from drivers.Vagrant.APIs.main import vagrant_launch_nvf, vagrant_destroy_nvf, vagrant_ssh


@task()
def launch_nvf(id):
    """
    Celery function that launch the BBU with id ID
    :param id: BBU ID
    :return:
    """
    nvf = Bbu.objects.get(id=id)
    vagrant_launch_nvf(nvf)


@task()
def shut_down_nvf(id):
    """
    Celery function that shut down the VNF with id ID
    :param id:
    :return:
    """
    nvf = Bbu.objects.get(id=id)
    vagrant_destroy_nvf(nvf)


@task()
def reconfigure_nvf(id, script):
    """
    Celery function that reconfigure the VNF with id ID with commands specify on the script
    :param id:
    :param script:
    :return:
    """
    nvf = Bbu.objects.get(id=id)
    vagrant_ssh(nvf=nvf, script=script)
