import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__))+'')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'plotter2010.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
