from django.shortcuts import redirect,resolve_url
from django.urls import reverse
from apps.users.views import login_view,signup_view





class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and (view_func == login_view or view_func == signup_view):
            next_url = request.GET.get('next',reverse('home'))
            resolved_next_url = resolve_url(next_url)
            return redirect(resolved_next_url)
        return None
            