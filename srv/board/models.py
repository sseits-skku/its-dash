from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from account.models import AnonymousUser
from utils.placeholder_models import PlaceholderModel, SharedCharField, \
                                     MarkdownSnippet


class Category(PlaceholderModel):
    title = SharedCharField(vname='Category name',
                            unique=True,
                            null=False, blank=False)

    class Meta:
        app_label = 'board'
        ordering = ('title', )
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Tag(PlaceholderModel):
    title = SharedCharField(vname='Tag name',
                            unique=True,
                            null=False, blank=False)

    class Meta:
        app_label = 'board'
        ordering = ('title', )
        verbose_name = _('tag')


class PostStatus(PlaceholderModel):
    title = SharedCharField(vname='Post status',
                            unique=True,
                            null=False, blank=False)
    detail = SharedCharField(vname='Post detail',
                             null=False, blank=False)

    class Meta:
        app_label = 'board'
        ordering = ('title', )
        verbose_name = _('post status')
        verbose_name_plural = _('post statuses')


class Comment(AnonymousUser, MarkdownSnippet):
    # content from MarkdownSnippet
    # password from AnonymousUser
    ip_addr = models.GenericIPAddressField(verbose_name=_('Wrote IP Address'))
    deleted = models.BooleanField(verbose_name=_('Is deleted'),
                                  default=False)
    # nickname from AnonymousUser
    is_subcomment = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True,
                               related_name='subcomment',
                               on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name=_('Wrote IP Address'),
                                        auto_now_add=timezone.now)
    modified_date = models.DateTimeField(verbose_name=_('Wrote IP Address'),
                                         auto_now=timezone.now)

    class Meta:
        app_label = 'board'
        ordering = ('-created_date', )
        verbose_name = _('post')


class Post(AnonymousUser, MarkdownSnippet):
    title = SharedCharField(vname='Post title',
                            null=False, blank=False)
    # content from MarkdownSnippet
    # password from AnonymousUser
    ip_addr = models.GenericIPAddressField(verbose_name=_('Wrote IP Address'))
    deleted = models.BooleanField(verbose_name=_('Is deleted'),
                                  default=False)
    # nickname from AnonymousUser
    status = models.ForeignKey('PostStatus',
                               verbose_name=_('Post status'),
                               on_delete=models.SET_NULL,
                               null=True)
    created_date = models.DateTimeField(verbose_name=_('Wrote IP Address'),
                                        auto_now_add=timezone.now)
    modified_date = models.DateTimeField(verbose_name=_('Wrote IP Address'),
                                         auto_now=timezone.now)
    category = models.ForeignKey('Category',
                                 verbose_name=_('Post category'),
                                 on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag',
                                  verbose_name=_('Post Tags'),
                                  related_name='tag',
                                  related_query_name='tag')
    comment = models.ManyToManyField('Comment',
                                     verbose_name=_('Post comments'),
                                     related_name='comment',
                                     related_query_name='comment')

    class Meta:
        app_label = 'board'
        ordering = ('-created_date', )
        verbose_name = _('post')
