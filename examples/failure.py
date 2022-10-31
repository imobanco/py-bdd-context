from py_bdd_context import BDDContextTestCase


class BDDContext(BDDContextTestCase):
    def test_failure_on_dado(self):
        """
        test description

         with multiple lines
        """
        with self.dado(
            """
            - Any BDD clause
            """
        ):
            raise ValueError("Any Error")

    def test_failure_on_quando(self):
        """
        test description

         with multiple lines
        """
        with self.quando(
            """
            - Any BDD clause
            - Another BDD clause
            """
        ):
            raise ValueError("Any Error")

    def test_failure_on_entao(self):
        """
        test description

         with multiple lines
        """
        with self.entao(
            """
            - Any BDD clause
            - Another BDD clause
            - Another BDD clause 2
            - Another BDD clause 3
            - Another BDD clause 4
            """
        ):
            raise ValueError("Any Error")
