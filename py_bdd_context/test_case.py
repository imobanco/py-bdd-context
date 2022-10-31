from unittest import TestCase

from bdd_context import dado, entao, quando


class BDDContextTestCase(TestCase):
    dado = dado
    quando = quando
    entao = entao
