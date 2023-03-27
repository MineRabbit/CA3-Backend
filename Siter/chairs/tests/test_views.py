from django.test import TestCase, Client
from django.urls import reverse
from chairs.models import Chairs, Owner


class ViewsTesting(TestCase):

    def CreateClient(self):
        self.client = Client()

    def test_index(self):

        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'chairs/index.html')

    def test_detail(self):
        owner = Owner.objects.create(name='TestOwner', address='TestAddress')
        chair = Chairs.objects.create(name="TestChair", owner_idowner=owner)
        response = self.client.get(reverse('detail', args=[chair.pk]))

        # Creating test owner and chair and testing if the view is working properly

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'chairs/detail.html')

    def test_sell(self):

        response = self.client.get(reverse('sell'))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'chairs/sell.html')

    def test_confirm(self):

        response = self.client.get(reverse('confirm'))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'chairs/detail.html')

        # Testing for the redirect in case of a missing request post

    def test_buy(self):
        owner = Owner.objects.create(name='TestOwner', address='TestAddress')
        chair = Chairs.objects.create(name="TestChair", owner_idowner=owner)
        response = self.client.get(reverse('buy', args=[chair.pk]))

        # Creating test owner and chair and testing if the view is working properly

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'bought.html')
