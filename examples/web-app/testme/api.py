import base64

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from .models import Profile


@login_required
@require_POST
def clickme(request):
    user = request.user
    profile: Profile = Profile.objects.get(user_id=user.id)

    profile.add_click()

    return JsonResponse({
        "clicks": profile.clicks
    })


@require_GET
def addme(request):
    x = request.GET.get("x", 0)
    y = request.GET.get("y", 0)

    return JsonResponse({
        "result": x + y
    })


@require_GET
def base64me(request):
    arg = request.GET.get("arg", "")

    return JsonResponse({
        "result": base64.b64encode(arg)
    })
