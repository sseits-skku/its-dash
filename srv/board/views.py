from django.http import JsonResponse
from django.views.generic import View


class Post(View):
    def get(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def post(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def put(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def delete(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })


class Comment(View):
    def get(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def post(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def put(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def delete(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })


class Tag(View):
    def get(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def post(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def put(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def delete(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })


class Category(View):
    def get(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def post(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def put(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def delete(self, request, **kwargs):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })
