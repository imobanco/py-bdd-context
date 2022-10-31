from unittest import TestCase

from py_bdd_context.bdd_context import dado, entao, quando


class BDDContextTestCase(TestCase):
    dado = dado
    quando = quando
    entao = entao

    def bddDescriptionInfo(self):
        return getattr(self, '_aditional_bdd_description_infos', [])

    def shortDescription(self):
        original_description = super().shortDescription()

        if not isinstance(original_description, str):
            original_description = ""

        infos = [*self.bddDescriptionInfo()]

        return original_description + '\n'.join(infos)
