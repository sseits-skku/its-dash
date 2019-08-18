from django.http import JsonResponse
from django.views.generic import View


class ThingType(View):
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


class Thing(View):
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


class Seat(View):
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
