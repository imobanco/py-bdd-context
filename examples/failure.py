from py_bdd_context import BDDContextTestCase


class BDDContext(BDDContextTestCase):
    def test_failure_on_given(self):
        """
        test description

         with multiple lines
        """
        with self.given(
            """
            - Any BDD clause
            """
        ):
            raise ValueError("Any Error")

    def test_failure_on_when(self):
        """
        test description

         with multiple lines
        """
        with self.when(
            """
            - Any BDD clause
            - Another BDD clause
            """
        ):
            raise ValueError("Any Error")

    def test_failure_on_then(self):
        """
        test description

         with multiple lines
        """
        with self.then(
            """
            - Any BDD clause
            - Another BDD clause
            - Another BDD clause 2
            - Another BDD clause 3
            - Another BDD clause 4
            """
        ):
            raise ValueError("Any Error")
