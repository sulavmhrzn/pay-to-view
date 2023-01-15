import io

import weasyprint
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import Membership


def send_pdf(user_email):
    membership = Membership.objects.first()
    subject = "Membership Activated"
    message = "Your membership has been successfully activated. Please, find the attached invoice."
    email = EmailMessage(subject, message, "admin@medium.com", [user_email])
    html = render_to_string("payment/pdf.html", {"membership": membership})
    buffer = io.BytesIO()
    weasyprint.HTML(string=html).write_pdf(buffer)
    email.attach("membership_activated.pdf", buffer.getvalue(), "application/pdf")

    email.send()
