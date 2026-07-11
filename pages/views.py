import json
from authlib.integrations.django_client import OAuth
from django.contrib.auth import login as local_login
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

from core.models import User, Testimonio
from .forms import TestimonioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


def index(request):
    try:
        user = User.objects.get(email=request.session["user"]["userinfo"]["email"])
        local_login(request, user)
    except KeyError:
        user = None

    testimonials_list = Testimonio.objects.filter(published=True).select_related('user').order_by('-created_at')[:3]

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
            "user": user,
            "testimonials": testimonials_list,
        },
    )

def surgeries(request):
    try:
        user = User.objects.get(email=request.session["user"]["userinfo"]["email"])
        local_login(request, user)
    except (KeyError, AttributeError):
        user = None

    return render(
        request,
        "surgeries.html",
        context={
            "session": request.session.get("user"),
            "user": user,
        },
    )

def diagnostic(request):
    try:
        user = User.objects.get(email=request.session["user"]["userinfo"]["email"])
        local_login(request, user)
    except (KeyError, AttributeError):
        user = None

    return render(
        request,
        "diagnostic.html",
        context={
            "session": request.session.get("user"),
            "user": user,
        },
    )

def about(request):
    try:
        user = User.objects.get(email=request.session["user"]["userinfo"]["email"])
        local_login(request, user)
    except (KeyError, AttributeError):
        user = None

    return render(
        request,
        "about.html",
        context={
            "session": request.session.get("user"),
            "user": user,
        },
    )

def testimonials(request):
    try:
        user = User.objects.get(email=request.session["user"]["userinfo"]["email"])
        local_login(request, user)
    except (KeyError, AttributeError):
        user = None

    if request.method == 'POST':
        if not user:
            messages.error(request, 'You must be logged in to leave a testimonial.')
            return redirect('login')
        form = TestimonioForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = user
            testimonial.save()
            messages.success(request, 'Su testimonio ha sido enviado y está pendiente de aprobación.')
            return redirect('testimonials')
    else:
        initial_data = {'name': user.get_full_name() or user.username} if user else {}
        form = TestimonioForm(initial=initial_data)

    testimonials_list = Testimonio.objects.filter(published=True).select_related('user').order_by('-created_at')
    
    return render(
        request,
        "testimonials.html",
        context={
            "session": request.session.get("user") if hasattr(request, 'session') else None,
            "user": user,
            "testimonials": testimonials_list,
            "form": form,
        },
    )

def is_moderator(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

@user_passes_test(is_moderator)
def moderator_dashboard(request):
    pending_testimonials = Testimonio.objects.filter(published=False).order_by('-created_at')
    approved_testimonials = Testimonio.objects.filter(published=True).order_by('-created_at')
    
    return render(
        request,
        "moderator_dashboard.html",
        context={
            "pending_testimonials": pending_testimonials,
            "approved_testimonials": approved_testimonials,
            "user": request.user,
        },
    )

@require_POST
@user_passes_test(is_moderator)
def approve_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonio, pk=pk)
    testimonial.published = not testimonial.published # toggle state
    testimonial.save()
    status = "aprobado" if testimonial.published else "ocultado"
    messages.success(request, f'Testimonio de {testimonial.name} fue {status}.')
    return redirect('moderator_dashboard')

# Auth0
oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    #Check if the user is already in the database
    print("pre try block")
    try:
        user_email = request.session["user"]["userinfo"]["email"]
        user, created = User.objects.get_or_create(email=user_email, username=user_email)
        print(created)
        print(user)
        if created:
            user.save()
            print("user created")
    except KeyError:
        print("KeyError: user not found")
        user = None
    return redirect(request.build_absolute_uri(reverse("index")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
                "federated": "",  # Force logout from identity provider (Google, etc.)
            },
            quote_via=quote_plus,
        ),
    )

