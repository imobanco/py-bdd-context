import inspect
import os


class TestFileHelper:
    def get_file_path_for_test(self, test):
        """
        :param test:
        :return:file path for test
        """
        test_class = test.__class__
        path = os.path.relpath(inspect.getfile(test_class))

        return f"{path}"

    def get_test_method_line_number_for_test(self, test, test_method_name):
        """
        :param test:
        :param test_method_name:
        :return: test path and line
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
        :param test:
        :param exc_tb:
        :return: exception path and line
        """
        test_path = self.get_file_path_for_test(test)
        lineno = exc_tb.tb_lineno
        return f"{test_path}:{lineno}"
