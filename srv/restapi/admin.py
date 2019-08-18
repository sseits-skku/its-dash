from django.contrib import admin

from .models import ThingType, Thing, Seat, Seminar,  \
                    Card, Comment, Category, Tag, Post, \
                    Person, Member

# Register your models here.

admin.site.register(ThingType)
admin.site.register(Tag)
admin.site.register(Thing)
admin.site.register(Seat)
admin.site.register(Seminar)
admin.site.register(Card)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Member)
admin.site.register(Comment)
