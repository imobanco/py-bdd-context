from unittest import TestCase
from py_bdd_context import BDDContextTestCase


def rise_sun(hour: int):
    if hour >= 6:
        return False
    return True


class RiseSunTestCase(BDDContextTestCase, TestCase):
    def test_rise_sun_before_6(self):
        with self.dado(
            """
            - são 5h da manhã
            """
        ):
            current_hour = 5

        with self.quando(
            """
            - o sol nascer
            """
        ):
            result = rise_sun(current_hour)

        with self.entao(
            """
            - o sol deve ter nascido corretamente
            """
        ):
            self.assertEqual(result, True)

    def test_rise_sun_after_6(self):
        with self.dado(
            """
            - são 6h da manhã
            """
        ):
            current_hour = 6

        with self.quando(
            """
            - o sol nascer
            """
        ):
            result = rise_sun(current_hour)

        with self.entao(
            """
            - o sol não deve ter nascido
            """
        ):
            self.assertEqual(result, False)
