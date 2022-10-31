from py_bdd_context import BDDContextTestCase


class BDDContext(BDDContextTestCase):
    def test_failure_on_dado(self):
        """
        descrição do teste

        com várias linhas
        """
        with self.dado(
            """
            - Alguma cláusula BDD
            """
        ):
            raise ValueError("Algum erro qualquer")

    def test_failure_on_quando(self):
        """
        descrição do teste

        com várias linhas
        """
        with self.quando(
            """
            - Alguma cláusula BDD
            - uma outra cláusula BDD
            """
        ):
            raise ValueError("Algum erro qualquer")

    def test_failure_on_entao(self):
        """
        descrição do teste

        com várias linhas
        """
        with self.quando(
            """
            - Alguma cláusula BDD
            - uma outra cláusula BDD
            - uma outra cláusula BDD 2
            - uma outra cláusula BDD 3
            - uma outra cláusula BDD 4
            """
        ):
            raise ValueError("Algum erro qualquer")
