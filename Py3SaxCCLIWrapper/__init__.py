import os
import re
from pathlib import Path
import subprocess as sub
import importlib

try:
    SAXONPATH = sub.run(['locate', f'{Path.home()}/*/saxon9he.jar'], capture_output=True, text=True).stdout.splitlines()[0]
    print(f'Saxon path set to {SAXONPATH}.')
except IndexError as Error:
    print('Saxon jar file not found.')
    print('The Saxon 9 HE jars could not be located. Please specifiy the path directly or when  instanciating the objects.')
    SAXONPATH = ''
except:
    SAXONPATH = ''

from . import SaxWrapper
