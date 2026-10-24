from pathlib import Path
from urllib.parse import quote

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_http_methods

from .forms import EnquiryForm


DESTINATION_GALLERY_FOLDERS = ("bodh-gaya", "rajgir", "nalanda", "vaishali & Kesariya")
SUPPORTED_IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}


@require_GET
def gallery_manifest(request):
    """Return the local image files for every destination gallery.

    This lets the site use every supported photo dropped into a destination
    folder, without requiring a template or JavaScript change for each image.
    """
    gallery_root = Path(settings.BASE_DIR) / "static" / "images" / "destinations"
    galleries = {}
    for destination in DESTINATION_GALLERY_FOLDERS:
        folder = gallery_root / destination
        if not folder.exists():
            galleries[destination] = []
            continue
        galleries[destination] = [
            f"{settings.STATIC_URL}images/destinations/{quote(destination)}/{quote(image.name)}"
            for image in sorted(folder.iterdir(), key=lambda item: item.name.casefold())
            if image.is_file() and image.suffix.lower() in SUPPORTED_IMAGE_TYPES
        ]
    return JsonResponse(galleries)


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            send_enquiry_emails(enquiry)
            messages.success(
                request,
                "Thank you. Your B2B requirement has been received. Our team will contact you shortly.",
            )
            return redirect(f"{reverse('home')}#enquiry")
        messages.error(request, "Please correct the highlighted fields and submit again.")
    else:
        form = EnquiryForm()
    return render(request, "home.html", {"form": form})


def send_enquiry_emails(enquiry):
    """Send sales notification and an acknowledgement; email is console-only in local development."""
    details = f"""
New B2B quote request

Agent: {enquiry.name}
Company: {enquiry.company_name}
Email: {enquiry.email}
Phone: {enquiry.phone}
Location: {enquiry.city_country}
Dates: {enquiry.travel_start_date} to {enquiry.travel_end_date or 'Not specified'}
Guests: {enquiry.guests}
Destinations: {enquiry.destinations}
Tour type: {enquiry.tour_type}
Hotels: {enquiry.hotel_category}
Transport: {enquiry.transport}
Requirements: {enquiry.requirements}
""".strip()
    EmailMessage(
        subject=f"New B2B enquiry — {enquiry.company_name}",
        body=details,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.SALES_EMAIL],
        reply_to=[enquiry.email],
    ).send(fail_silently=True)

    reply = f"""
Dear {enquiry.name},

Thank you for contacting Uruvela Journeys. We have received your Bihar tour requirement for {enquiry.guests} guest(s) and will share a B2B quotation shortly.

Regards,
Uruvela Journeys
""".strip()
    EmailMessage(
        subject="We received your B2B tour requirement",
        body=reply,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[enquiry.email],
    ).send(fail_silently=True)
