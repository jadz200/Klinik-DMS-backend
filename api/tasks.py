from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time
from .models import *

@shared_task
def remindpatients():
    patients=Patient.objects.all()
    print(f"Patient")