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

from django import forms
from .models import Script


class ScriptForm(forms.ModelForm):
    type = forms.CharField(max_length=32)

    def __init__(self, *args, **kwargs):
        super(ScriptForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'id': 'Ufile'})
        self.fields['type'] = forms.ChoiceField(required=False,
                                                widget=forms.Select(attrs={"onChange": 'select(this);'}),
                                                choices=[("Script", "Script"),
                                                         ("Direct Input", "Direct Input"),
                                                         ("File", "File"),
                                                         ("Ansible", "Ansible"),
                                                         ("Puppet", "Puppet"),
                                                         ("Salt", "Salt"),
                                                         ("Chef", "Chef")])

    class Meta:
        model = Script
        fields = [
            "name",
            "description",
            "script",
            "file",
            "type",
        ]
