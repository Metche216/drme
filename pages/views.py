import json
from authlib.integrations.django_client import OAuth
from django.contrib.auth import login as local_login
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

from core.models import User


def index(request):
    try:
        user = User.objects.get(email=request.session["user"]["userinfo"]["email"])
        local_login(request, user)
    except KeyError:
        user = None

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
            "user": user,
        },
    )

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

