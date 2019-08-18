from django.http import JsonResponse
from django.views.generic import View


class Notice(View):
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


class Service(View):
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


class Recruit(View):
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
