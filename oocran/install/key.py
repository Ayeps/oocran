###
#    Open Orchestrator Cloud Radio Access Network
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
###

import os,sys

secret = os.urandom(32).encode('base-64').split('\n')[0]

file = open(sys.argv[1]+"/oocran/django/oocran/secret_key.py", "w+")
file.write("SECRET_KEY = '"+secret+"'")
file.close()
