import inspect
import os


class TestFileHelper:
    def get_file_path_for_test(self, test):
        """
        Args:
            test: test method instance

        Returns:
            file path where the test method was declared
        """
        test_class = test.__class__
        path = os.path.relpath(inspect.getfile(test_class))

        return f"{path}"

    def get_test_path(self, test):
        """
        Args:
            test: test method instance

        Returns:
            test path
        """
        test_class = str(test.__class__)
        test_class = test_class[8:-2]

        test_method = str(test)
        index = test_method.find(" ")
        test_method = test_method[:index]

        path = test_class + "." + test_method

        return f"{path}"

    def get_test_method_line_number_for_test(self, test, test_method_name):
        """
        Args:
            test: test method instance
            test_method_name: test method name

        Returns:
            file path and line number where the the test method was declared
        """
        test_path = self.get_file_path_for_test(test)

        test_class = test.__class__
        source = inspect.findsource(test_class)

        lineno = source[1] + 1
        for index, line in enumerate(source[0]):
            if test_method_name in line:
                lineno = index + 1
                break

        return f"{test_path}:{lineno}"

    def get_exception_line_number_for_test(self, test, exc_tb):
        """
        Args:
            test: test method instance
            exc_tb: exception traceback

        Returns:
            file path and line number where the exception was raised
        """
        test_path = self.get_file_path_for_test(test)
        lineno = exc_tb.tb_lineno
        return f"{test_path}:{lineno}"
