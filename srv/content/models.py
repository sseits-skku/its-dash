from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import uuid

from utils.permissions import OwnerMixin


class Content(models.Model):
    content_id = models.UUIDField(verbose_name=_('Content UUID Field'),
                                  default=uuid.uuid4,
                                  primary_key=True,
                                  editable=False)
    member_only = models.BooleanField(verbose_name=_('Content for member only'),
                                      default=False)
    created_date = models.DateTimeField(verbose_name=_('Content created date'),
                                        auto_now_add=timezone.now)
    modified_date = models.DateTimeField(verbose_name=_('Content modified date'),
                                         auto_now=timezone.now)

    class Meta:
        app_label = 'content'
        abstract = True
        ordering = ('-created_date', )
        verbose_name = _('content')

    def __str__(self):
        return str(self.content_id)


class ImageContent(Content, OwnerMixin):
    image = models.ImageField(verbose_name=_('Image'),
                              blank=True)

    class Meta:
        app_label = 'content'
        ordering = ('-created_date', )
        verbose_name = _('image content')


class FileContent(Content, OwnerMixin):
    file = models.FileField(verbose_name=_('File'))
    caption = models.CharField(max_length=255,
                               verbose_name=_('File caption'),
                               blank=True, null=True)

    class Meta:
        app_label = 'content'
        ordering = ('-created_date', )
        verbose_name = _('file content')


class TextSnippet(Content):
    text = models.TextField(verbose_name=_('Content'),
                            blank=True)
    content_type = models.CharField(max_length=255,
                                    verbose_name=_('Content type'),
                                    default='Markdown')

    class Meta:
        app_label = 'content'
        abstract = True
        ordering = ('-created_date', )
        verbose_name = _('text snippet')
