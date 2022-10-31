from unittest import TestCase

from py_bdd_context.bdd_context import dado, entao, quando
from py_bdd_context.test_file_helper import TestFileHelper


class BDDContextTestCase(TestCase):
    dado = dado
    quando = quando
    entao = entao

    def testDescriptionInfo(self):
        test_lineno = TestFileHelper().get_test_method_line_number_for_test(
            self, self._testMethodName
        )
        return ["", f"{test_lineno} | teste"]

    def bddDescriptionInfo(self):
        return getattr(self, "_aditional_bdd_description_infos", [])

    def shortDescription(self):
        original_description = super().shortDescription()

        if not isinstance(original_description, str):
            original_description = ""

        infos = ["", *self.testDescriptionInfo(), *self.bddDescriptionInfo()]

        return original_description + "\n".join(infos)
