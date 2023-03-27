from django.test import TestCase
from django.urls import reverse, resolve
from chairs.views import index, detail, sell, confirm, buy


class UrlsTesting(TestCase):

    # Assertions for url testing check that the correct views are called for a given url

    def test_index_resolve(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_sell_resolve(self):
        url = reverse('sell')
        self.assertEqual(resolve(url).func, sell)

    def test_confirm_resolve(self):
        url = reverse('confirm')
        self.assertEqual(resolve(url).func, confirm)

    def test_detail_resolve(self):
        url = reverse('detail', args=['1'])
        self.assertEqual(resolve(url).func, detail)

    def test_buy_resolve(self):
        url = reverse('buy', args=['1'])
        self.assertEqual(resolve(url).func, buy)

    # Only testing the url and not the view so the given argument does not matter for detail and buy
    # (as long as it is a valid integer)
