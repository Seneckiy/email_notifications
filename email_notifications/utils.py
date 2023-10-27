import logging

from aoi.models import AoI
from user.models import User

from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


def send_email_notification(user_mail, email_message, subject):
    result = 0
    try:
        result = send_mail(subject, email_message, None, [user_mail])
    except Exception as ex:
        logger.error(f"Error while sending mail: {str(ex)}")
    if result == 1:
        logger.info(f"Email sent successfully! for email '{user_mail}'")
    else:
        logger.info(f"Failed to send the email for email '{user_mail}'")


def email_notification(request, status):
    user_data = User.objects.filter(id=request.user_id).first()
    aoi_name = AoI.objects.filter(id=request.aoi_id).first()
    if not user_data.receive_notification:
        logger.info(f"Not sending email for user '{user_data.email}'")
        return

    message = f"""Your request for AOI '{aoi_name.name if aoi_name else request.polygon.wkt}' and layer '{request.component_name}' is {status}
    \n\nClick the link below to visit the site:\n{request.request_origin}"""
    send_email_notification(user_data.email, message, settings.EMAIL_SUBJECT)

    if settings.DEFAULT_SYSTEM_NOTIFICATION_EMAIL:
        system_message=f"""
        Status: {status.upper()},
        Error: {', '.join(request.user_readable_errors) if request.user_readable_errors else request.error},
        Domain: {request.request_origin},

        AoI Name: {aoi_name.name if aoi_name else None},
        AoI polygon: {request.polygon.wkt},
        Component name: {request.component_name},
        Start date: {request.date_from.strftime("%Y/%m/%d") if request.date_from else None},
        End date: {request.date_to.strftime("%Y/%m/%d") if request.date_to else None},
        Additional parameter value: {request.additional_parameter},

        User name: {user_data.username},
        User email: {user_data.email}
        """
        send_email_notification(settings.DEFAULT_SYSTEM_NOTIFICATION_EMAIL, system_message, f"{settings.EMAIL_SUBJECT} - {status.upper()}")