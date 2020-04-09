from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from .validators import CustomEmailValidator


class CustomUser(AbstractUser):

    username = None

    email = models.EmailField(
        _('email address'),
        unique=True,
        validators=[CustomEmailValidator],
        help_text=_('Emails ending with socar-aqs.com are only accepted.'),
        error_messages={
            'unique': _("An user with that email already exists."),
        },
    )

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['department', 'workplace']
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


