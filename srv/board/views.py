import json

from django.contrib.auth.hashers import check_password
from django.db.models import Model
from django.views.generic import View

from utils.mod_str import gen_json, get_client_ip

from .models import Post, Category, Comment, Tag


class PostView(View):
    def get(self, request, **kwargs):
        if 'post_id' in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        else:
            all_post = Post.objects.all()
            if all_post.exists():
                return gen_json(data=all_post)
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'post_id' in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        try:
            data = json.loads(request.body)
            Post.objects.create(ip_addr=get_client_ip(request),
                                **data)
            return gen_json()
        except (KeyError, json.JSONDecodeError):
            return gen_json(reason='WRONG_REQUEST')

    def put(self, request, **kwargs):
        if 'post_id' in kwargs:
            try:
                data = json.loads(request.body)
                post = Post.objects.get(pk=kwargs['post_id'])
                if not check_password(data['passwd'], post.passwd):
                    return gen_json(reason='WRONG_PASSWD')
                data.update(ip_addr=get_client_ip(request))
                post.update(data)
                return gen_json()
            except (KeyError, json.JSONDecodeError, Post.DoesNotExist):
                return gen_json(reason='WRONG_REQUEST')
        return gen_json(reason='MEANINGLESS_OP')

    def delete(self, request, **kwargs):
        if 'post_id' in kwargs:
            try:
                passwd = json.loads(request.body)['passwd']
                post = Post.objects.get(pk=kwargs['post_id'])
                if not check_password(passwd, post.passwd):
                    return gen_json(reason='WRONG_PASSWD')
            except (KeyError, json.JSONDecodeError, Model.DoesNotExist):
                return gen_json(reason='WRONG_REQUEST')
        else:
            # TODO: Should be authenticated.
            post = Post.objects.all()
        if not post:
            return gen_json(reason='EMPTY_DATA')
        post.delete()
        return gen_json()


class CommentView(View):
    def get(self, request, **kwargs):
        if 'comment_id' not in kwargs:
            all_com = Comment.objects.all()
            if all_com.exists():
                return gen_json(data=all_com)
        else:
            return gen_json(reason='MEANINGLESS_OP')
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'comment_id' in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        try:
            data = json.loads(request.body)
            data.update(ip_addr=get_client_ip(request))
            com = Comment(data)
            com.save()
            return gen_json()
        except (KeyError, json.JSONDecodeError):
            return gen_json(reason='WRONG_REQUEST')

    def put(self, request, **kwargs):
        if 'comment_id' not in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        try:
            data = json.loads(request.body)
            com = Comment.objects.get(pk=kwargs['comment_id'])
            if not check_password(data['passwd'], com.passwd):
                return gen_json(reason='WRONG_PASSWD')
            data.update(ip_addr=get_client_ip(request))
            com.update(data)
            return gen_json()
        except (KeyError, json.JSONDecodeError, Model.DoesNotExist):
            return gen_json(reason='WRONG_REQUEST')

    def delete(self, request, **kwargs):
        if 'comment_id' in kwargs:
            try:
                passwd = json.loads(request.body)['passwd']
                com = Comment.objects.get(pk=kwargs['comment_id'])
                if not check_password(passwd, com.passwd):
                    return gen_json(reason='WRONG_PASSWD')
            except (KeyError, json.JSONDecodeError, Model.DoesNotExist):
                return gen_json(reason='WRONG_REQUEST')
        else:
            # TODO: Should be authenticated.
            com = Comment.objects.all()
        if not com:
            return gen_json(reason='EMPTY_DATA')
        com.delete()
        return gen_json()


class TagView(View):
    def get(self, request, **kwargs):
        if 'tag_name' in kwargs:
            tag = Tag.objects.filter(
                title=kwargs['tag_name']
             )
            if tag:
                return gen_json(data=tag)
        else:
            all_tag = Tag.objects.all()
            if all_tag.exists():
                return gen_json(data=all_tag)
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        # TODO: Should be authenticated.
        if 'tag_name' in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        try:
            title = json.loads(request.body)['title']
            tag = Tag(title=title)
            tag.save()
            return gen_json()
        except (KeyError, json.JSONDecodeError):
            return gen_json(reason='WRONG_REQUEST')

    def put(self, request, **kwargs):
        # TODO: Should be authenticated.
        if 'tag_name' not in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        try:
            title = json.loads(request.body)['title']
            tag = Tag.objects.get(title=kwargs['tag_name'])
            tag.update(title=title)
            return gen_json()
        except (KeyError, json.JSONDecodeError, Model.DoesNotExist):
            return gen_json(reason='WRONG_REQUEST')

    def delete(self, request, **kwargs):
        # TODO: Should be authenticated.
        if 'tag_name' in kwargs:
            tag = Tag.objects.filter(
                title=kwargs['tag_name']
            )
        else:
            tag = Tag.objects.all()
        if not tag:
            return gen_json(reason='EMPTY_DATA')
        tag.delete()
        return gen_json()


class CategoryView(View):
    def get(self, request, **kwargs):
        if 'category_name' in kwargs:
            cat = Category.objects.filter(
                title=kwargs['category_name']
            )
            if cat:
                return gen_json(data=cat)
        else:
            all_cat = Category.objects.all()
            if all_cat.exists():
                return gen_json(data=all_cat)
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        # TODO: Should be authenticated.
        if 'category_name' in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        try:
            title = json.loads(request.body)['title']
            cat = Category(title=title)
            cat.save()
            return gen_json()
        except (KeyError, json.JSONDecodeError):
            return gen_json(reason='WRONG_REQUEST')

    def put(self, request, **kwargs):
        # TODO: Should be authenticated.
        if 'category_name' not in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        try:
            title = json.loads(request.body)['title']
            cat = Category.objects.filter(
                title=kwargs['category_name']
            ).first()
            cat.update(title=title)
            return gen_json()
        except (KeyError, json.JSONDecodeError):
            return gen_json(reason='WRONG_REQUEST')

    def delete(self, request, **kwargs):
        # TODO: Should be authenticated.
        if 'category_name' in kwargs:
            cat = Category.objects.filter(
                title=kwargs['category_name']
            )
        else:
            cat = Category.objects.all()
        if not cat:
            return gen_json(reason='EMPTY_DATA')
        cat.delete()
        return gen_json()
