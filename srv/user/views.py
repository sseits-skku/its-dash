from django.views.generic import View

from utils.mod_str import gen_json


class PersonView(View):
    def get(self, request, **kwargs):
        if 'person_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'person_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def put(self, request, **kwargs):
        if 'person_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def delete(self, request, **kwargs):
        if 'person_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')


class MemberView(View):
    def get(self, request, **kwargs):
        if 'member_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'member_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def put(self, request, **kwargs):
        if 'member_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def delete(self, request, **kwargs):
        if 'member_id' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')


class TokenView(View):
    def put(self, request, **kwargs):
        pass   # TODO
        return gen_json(reason='EMPTY_DATA')
