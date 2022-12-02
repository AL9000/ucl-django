from django.shortcuts import resolve_url
from django.test import TestCase

from inscriptions.models import InscriptionRequest, User


class InscriptionRequestTestCase(TestCase):
    def test_accepted_inscription_request_does_not_appear_in_list(self):
        user = User.objects.create_user(username="test")
        InscriptionRequest.objects.create(candidat=user)
        InscriptionRequest.objects.create(candidat=user, accepted=True)
        url = resolve_url("inscriptions:list")
        response = self.client.get(url)
        self.assertEqual(InscriptionRequest.objects.count(), 2)
        self.assertEqual(response.context["object_list"].count(), 1)
