## IMPORT REQUIRED MODULES
import os
from celery import Celery

## INSTANTIATE CELERY APP
app = Celery(
    broker=os.environ.get("CELERY_BROKER_URL", default="redis://:Pa55w0rd!@redis:6379/0"), 
    include=['tasks']
)