from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from .list_choices import UF



class ModelTime(models.Model):
    created = models.DateTimeField(_('criado em'), auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(_('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Client(ModelTime):
    first_name = models.CharField(_('nome'), max_length=100)
    last_name = models.CharField(_('sobre nome'), max_length=100)
    phone = models.CharField(_('telefone'), max_length=11)
    cell = models.CharField(_('celular'), max_length=12, blank=True)
    address = models.CharField(_(u'endereço'), max_length=200)
    city = models.CharField(_('cidade'), max_length=150)
    zip_code = models.CharField(_(u'codigo postal'), max_length=8)
    state = models.CharField(_('estado'), max_length=80, choices=UF)
    cpf = models.CharField(_('cpf'), max_length=11)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    full_name = property(__str__)

    def get_absolute_url(self):
        return reverse("core:home_view")
