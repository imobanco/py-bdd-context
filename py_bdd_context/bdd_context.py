import functools

from py_bdd_context.test_file_helper import TestFileHelper


class BDDContextManager:
    def __init__(self, bdd_type: str, bdd_docstring: str):
        """
        Initialize the BDD Context step
        Args:
            bdd_type: BDD step type (given, when, then)
            bdd_docstring: BDD step description
        """
        self.bdd_type = bdd_type
        self.bdd_docstring = "\n".join(
            [
                f"  {line.lstrip().rstrip()}"
                for line in bdd_docstring.split("\n")
                if line.lstrip().rstrip()
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        When exiting the BDD Context, if some exception was raised we need to save info
        abount the execution.

        Those infos are:
            - exception raise file location and number
            - BDD step type
            - BDD step description

        Note:
            these informations are injected on the test instance using the attribute
            _aditional_bdd_description_infos.

        Args:
            exc_type: exception type
            exc_val: exception raised
            exc_tb: exception traceback
        """
        if exc_type is not None:
            tfh = TestFileHelper()

            test = exc_tb.tb_frame.f_locals["self"]
            exc_lineno = tfh.get_exception_line_number_for_test(test, exc_tb)
            test_path = tfh.get_test_path(test)

            test._aditional_bdd_description_infos = [
                f"{exc_lineno} | exceção",
                f"{test_path} | caminho do teste",
                "",
                f"{self.bdd_type}:",
                self.bdd_docstring,
            ]


given = functools.partial(BDDContextManager, "given")
when = functools.partial(BDDContextManager, "when")
then = functools.partial(BDDContextManager, "then")
