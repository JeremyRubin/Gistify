import sys
import subprocess as sp
import os
import json
decode = json.JSONDecoder()
for f in sys.argv[1:]:
        fi = open(f,'r')
        fulltext = fi.read()
        fi.close()
        son = {"description": 'auto-added by Gistify',\
        "public": 'true',\
        "files": {\
        str(os.urandom(20).encode('hex')): {\
        "content": fulltext\
        }\
        }\
        }\

        x = sp.check_output(['curl','--data', json.dumps(son),\
        'https://api.github.com/gists'])
        url = decode.decode(x)['html_url']
        p1 = sp.Popen(['echo',"%s"%(url)],stdout=sp.PIPE)
        p2 = sp.Popen(['pbcopy',],stdin=p1.stdout, stdout=sp.PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        output = p2.communicate()[0]
              
