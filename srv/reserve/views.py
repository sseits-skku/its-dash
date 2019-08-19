from django.views.generic import View
from django.db.models import Model
from django.contrib.auth.hashers import check_password

import json

from .models import Card, Service
from user.models import Person
from utils.mod_str import gen_json, get_client_ip


class CardView(View):
    def get(self, request, **kwargs):
        if 'card_id' in kwargs:
            card = Card.objects.filter(
                pk=kwargs['card_id']
            )
            if card:
                return gen_json(data=card)
        else:
            all_card = Card.objects.all()
            if all_card.exists():
                return gen_json(data=all_card)
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        # TODO: Should be authenticated.
        if 'card_id' in kwargs:
            return gen_json(reason='MEANINGLESS_OP')
        else:
            try:
                data = json.loads(request.body)
                person_data, card_data = data['person'], data['card']
                person, _ = Person.objects.get_or_create(person_data)
                card = Card(person=person.pk, **card_data)
                card.save()
                return gen_json()
            except (KeyError, json.JSONDecodeError):
                return gen_json(reason='WRONG_REQUEST')

    def put(self, request, **kwargs):
        if 'card_id' in kwargs:
            try:
                data = json.loads(request.body)
                person_data, card_data = data.get('person'), data.get('card')
                person, _ = Person.objects.get_or_create(pk=kwargs['card_id'],
                                                         **person_data)
                Card.objects.get(person=person.pk).update(**card_data)
                return gen_json()
            except (KeyError, json.JSONDecodeError):
                return gen_json(reason='WRONG_REQUEST')
        else:
            return gen_json(reason='MEANINGLESS_OP')
        return gen_json(reason='EMPTY_DATA')

    def delete(self, request, **kwargs):
        if 'card_id' in kwargs:
            pass  # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')


class SeminarView(View):
    def get(self, request, **kwargs):
        if 'seminar_id' in kwargs:
            pass   # TODO
        elif 'room_name' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def post(self, request, **kwargs):
        if 'seminar_id' in kwargs:
            pass   # TODO
        elif 'room_name' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def put(self, request, **kwargs):
        if 'seminar_id' in kwargs:
            pass   # TODO
        elif 'room_name' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')

    def delete(self, request, **kwargs):
        if 'seminar_id' in kwargs:
            pass   # TODO
        elif 'room_name' in kwargs:
            pass   # TODO
        else:
            pass   # TODO
        return gen_json(reason='EMPTY_DATA')
