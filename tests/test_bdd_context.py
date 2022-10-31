from unittest import skip

from py_bdd_context import BDDContextTestCase


class TestBDDContext(BDDContextTestCase):
    @skip("esse teste serve apenas para visualizar a descrição da falha do teste")
    def test_print_info(self):
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
