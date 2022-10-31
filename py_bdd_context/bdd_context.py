import functools

from py_bdd_context.test_file_helper import TestFileHelper


class BDDContextManager:
    def __init__(self, bdd_type: str, bdd_docstring: str):
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
        if exc_type is not None:
            test = exc_tb.tb_frame.f_locals["self"]
            exc_lineno = TestFileHelper().get_exception_line_number_for_test(
                test, exc_tb
            )

            test._aditional_bdd_description_infos = [
                f"{exc_lineno} | exceção",
                "",
                f"{self.bdd_type}:",
                self.bdd_docstring,
            ]


dado = functools.partial(BDDContextManager, "dado")
quando = functools.partial(BDDContextManager, "quando")
entao = functools.partial(BDDContextManager, "então")
