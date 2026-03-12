from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


SERVICES = [
    {"icon": "globe-alt",          "title": "Digital Transformation",   "colour": "teal",
     "description": "We guide East African businesses through end-to-end digital transformation — from legacy modernisation to cloud-native systems."},
    {"icon": "device-phone-mobile","title": "Mobile & Web Development", "colour": "orange",
     "description": "Crafting blazing-fast, beautiful web and mobile applications that delight users and scale effortlessly."},
    {"icon": "chart-bar",          "title": "Data & Analytics",         "colour": "teal",
     "description": "Turn your raw data into actionable intelligence with custom dashboards and predictive analytics solutions."},
    {"icon": "shield-check",       "title": "Cybersecurity",            "colour": "orange",
     "description": "Security-first approach covering audits, penetration testing, and ongoing threat monitoring."},
    {"icon": "cloud",              "title": "Cloud Infrastructure",     "colour": "teal",
     "description": "AWS, GCP, or Azure — we architect, migrate, and optimise your cloud environment for performance."},
    {"icon": "academic-cap",       "title": "Tech Training & Bootcamps","colour": "orange",
     "description": "Upskilling the next generation of African engineers through intensive, project-based training."},
]


def home(request):
    return render(request, "core/home.html", {
        "page_title": "Home",
        "services_preview": SERVICES[:3],
    })


def about(request):
    return render(request, "core/about.html", {"page_title": "About Us"})


def services(request):
    return render(request, "core/services.html", {
        "page_title": "Our Services",
        "services": SERVICES,
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            send_mail(
                subject=f"[Trovia Contact] {contact_msg.subject or 'New enquiry'}",
                message=f"From: {contact_msg.name} <{contact_msg.email}>\n\n{contact_msg.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
            messages.success(request, "Thank you! Your message has been received. We'll be in touch within 24 hours. 🌍")
            return redirect("core:contact")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"page_title": "Contact Us", "form": form})


def error_404(request, exception=None):
    return render(request, "errors/404.html", status=404)


def error_500(request):
    return render(request, "errors/500.html", status=500)
