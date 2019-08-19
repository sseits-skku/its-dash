from django.views.generic import View

from utils.mod_str import gen_json


class ThingTypeView(View):
    def get(self, request, **kwargs):
        if 'ttype_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'ttype_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def put(self, request, **kwargs):
        if 'ttype_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def delete(self, request, **kwargs):
        if 'ttype_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')


class ThingView(View):
    def get(self, request, **kwargs):
        if 'thing_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'thing_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def put(self, request, **kwargs):
        if 'thing_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def delete(self, request, **kwargs):
        if 'thing_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')


class SeatView(View):
    def get(self, request, **kwargs):
        if 'seat_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'seat_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def put(self, request, **kwargs):
        if 'seat_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def delete(self, request, **kwargs):
        if 'seat_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')
