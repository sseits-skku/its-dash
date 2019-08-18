from django.http import JsonResponse
from django.views.generic import View


class Person(View):
    def get(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def post(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def put(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def delete(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })


class Member(View):
    def get(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def post(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def put(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def delete(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })


class Token(View):
    def get(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def post(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def put(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })

    def delete(self, request):
        return JsonResponse({
            'success': False,
            'reason': 'NOT_IMPLEMENTED'
        })
