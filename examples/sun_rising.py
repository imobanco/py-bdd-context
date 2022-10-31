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
            - it's 5 am
            """
        ):
            current_hour = 5

        with self.quando(
            """
            - the sun rise
            """
        ):
            result = rise_sun(current_hour)

        with self.entao(
            """
            - the sun must have risen correctly
            """
        ):
            self.assertEqual(result, True)

    def test_rise_sun_after_6(self):
        with self.dado(
            """
            - it's 6 am
            """
        ):
            current_hour = 6

        with self.quando(
            """
            - the sun rise
            """
        ):
            result = rise_sun(current_hour)

        with self.entao(
            """
            - the sun must not have risen
            """
        ):
            self.assertEqual(result, False)
