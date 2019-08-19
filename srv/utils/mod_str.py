from django.http import JsonResponse, HttpResponse     # noqa: F401
from django.core.serializers import serialize as seri  # noqa: F401
from json import loads, dumps                          # noqa: F401


def trunc(content, num):
    t = content
    if len(t) > num:
        return t[:num] + '...'
    return t


def gen_json(reason='SUCCESS', data=None,
             serialize=True, status=400, **kwargs):
    retval = kwargs
    if reason == 'SUCCESS':
        status = 200
        retval.update({'success': True, 'reason': 'SUCCESS'})
        if data:
            if serialize:
                retval.update({'data': loads(seri('json', data))})
            else:
                retval.update({'data': data})
    else:
        retval.update({'success': False, 'reason': reason})
    return JsonResponse(retval,
                        json_dumps_params={'indent': 2},
                        status=status)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
