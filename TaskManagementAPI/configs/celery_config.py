from celery import Celery
from TaskManagementAPI.configs.env_loader import BROKER_URL, RESULT_BACKEND


celery = Celery(
    'tasks',
    broker=BROKER_URL,
    backend=RESULT_BACKEND
)

@celery.task
def send_otp(data):
    try:
        pass
    except Exception as error:
        pass