import io
from decimal import Decimal

import stripe
import weasyprint
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from .models import Membership

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def membership_list(request):
    membership = Membership.objects.all()
    return render(
        request, "payment/membership_list.html", context={"membership": membership}
    )


@login_required
def payment_process(request):
    membership = Membership.objects.first()
    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("payment:completed"))
        cancel_url = request.build_absolute_uri(reverse("payment:canceled"))
        session_data = {
            "mode": "payment",
            "client_reference_id": request.user.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "customer_email": request.user.email,
            "line_items": [
                {
                    "price_data": {
                        "currency": "aud",
                        "product_data": {"name": membership.title},
                        "unit_amount": int(membership.price * Decimal("100")),
                    },
                    "quantity": 1,
                }
            ],
        }

        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    return redirect("payment:membership_list")


def completed(request):
    return render(request, "payment/completed.html")


def canceled(request):
    return render(request, "payment/canceled.html")
