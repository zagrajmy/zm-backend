import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Zagrajmy user model."""

    auth0_id = models.PositiveIntegerField(blank=True, null=True)
    locale = models.CharField(max_length=20, default="en")
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:  # noqa: D106
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "cr_user"

    def __str__(self) -> None:
        return self.get_full_name()
