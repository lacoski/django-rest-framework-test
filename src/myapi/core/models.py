import binascii
import os

from jsonfield import JSONField

from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class MyOwnToken(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(verbose_name=_("Key"), max_length=40, primary_key=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )

    openstack_cache = models.TextField(verbose_name=_("Openstack Cache"), blank=True, null=True)

    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True)
    expired = models.DateTimeField(verbose_name=_('Expired'), blank=True, null=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(MyOwnToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key