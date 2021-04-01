from .base import *
import os

if os.environ.get('DJANGO_DEBUG', '') == 'False':
    from .prod import *
else:
    from .dev import *
