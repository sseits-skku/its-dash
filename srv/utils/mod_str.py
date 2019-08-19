from django.http import JsonResponse, HttpResponse     # noqa: F401
from django.core.serializers import serialize as seri  # noqa: F401
from json import loads, dumps                          # noqa: F401


def trunc(content, num):
    t = content
    if len(t) > num:
        return t[:num] + '...'
    return t


def gen_json(reason='SUCCESS', data=None, serialize=True, **kwargs):
    retval = kwargs
    if reason == 'SUCCESS':
        retval.update({'success': True, 'reason': 'SUCCESS'})
        if data:
            if serialize:
                retval.update({'data': loads(seri('json', data))})
            else:
                retval.update({'data': data})
    else:
        retval.update({'success': False, 'reason': reason})
    return JsonResponse(retval, json_dumps_params={'indent': 2})
