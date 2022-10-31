from unittest import TestCase

from py_bdd_context.bdd_context import given, then, when
from py_bdd_context.test_file_helper import TestFileHelper


class BDDContextTestCase(TestCase):
    given = given
    when = when
    then = then

    def testDescriptionInfo(self):
        """
        Returns:
            list with infos about the test path and line number
        """
        test_lineno = TestFileHelper().get_test_method_line_number_for_test(
            self, self._testMethodName
        )
        return ["", f"{test_lineno} | teste"]

    def bddDescriptionInfo(self):
        """
        Note:
            this method trusts on the injection of the attribute _aditional_bdd_description_infos in # noqa
            the test instance.

        Returns:
            list with infos about the BDD step
        """
        return getattr(self, "_aditional_bdd_description_infos", [])

    def shortDescription(self):
        """
        Returns:
            test description with additional infos
        """
        original_description = super().shortDescription()

        if not isinstance(original_description, str):
            original_description = ""

        infos = ["", *self.testDescriptionInfo(), *self.bddDescriptionInfo()]

        return original_description + "\n".join(infos)
