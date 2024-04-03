from typing import Any
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.safestring import mark_safe
from django.http import HttpRequest, HttpResponse


class CustomLoginView(LoginView):
    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        ret = super().form_valid(form)
        message = "Login success!<br>Hi, %(username)s" % {
            "username": self.request.user.username
        }
        messages.add_message(
            self.request,
            messages.INFO,
            mark_safe(message)
        )
        return ret

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.add_message(
            self.request,
            messages.WARNING,
            mark_safe("Wrong login or password")
        )
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        messages.add_message(self.request, messages.INFO, "See you later!")
        return super().dispatch(request, *args, **kwargs)
