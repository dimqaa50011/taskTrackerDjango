from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        validators=[username_validator]
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.CharField(
        _("email address"),
        max_length=256,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        }, blank=True, null=True
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. \
            Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = [USERNAME_FIELD]

    def get_full_name(self):
        return "%s %s" % (
            self.first_name, self.last_name
        )
