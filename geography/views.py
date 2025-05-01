from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

@login_required
def test_auth(request):
    return JsonResponse({
        'user': request.user.username,
        'status': 'authenticated'
    })
favicon_view = RedirectView.as_view(
    url=staticfiles_storage.url('images/favicon.ico'),
    permanent=True
)