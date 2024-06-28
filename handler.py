import datetime
import logging
import smtplib
from email.message import EmailMessage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    print("Mimiiii")