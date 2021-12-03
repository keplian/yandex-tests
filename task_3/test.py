import pytest
import author
import time

class TestDecorator:

    def test_usercode_has_precode_variables_and_functions(self):
        assert hasattr(author, 'time_check'), 'Убедитесь, что код содержит функцию time_check'
        assert hasattr(author, 'cache_args'), 'Убедитесь, что функция time_check содержит функцию cache_args'
        assert hasattr(author, 'cache_args'), 'Убедитесь, что функция time_check содержит функцию long_heavy'

    def test_func__is_decorator(self):
        @author.time_check
        def decorated(var):
            return var
        assert decorated(1) == 1, 'Убедитесь, что функция time_check работает как декоратор'
        @author.cache_args
        def decorated(var):
            return var
        assert decorated(
            1) == 1, 'Убедитесь, что функция cashe args работает как декоратор'

    def test_once_call(self):
        assert author.long_heavy(100) == 200

    def test_time(self):
        start = time.time()
        author.long_heavy(555)
        stop = time.time()
        assert round(stop - start) == 1, 'Время выполнения не равно 1 секунде при первом вызове функции long_heavy'

    def test_few_calls(self):
        start = time.time()
        author.long_heavy(800)
        stop = time.time()
        assert round(
            stop - start) == 1, 'Время выполнения не равно 1 секунде при первом вызове функции long_heavy'
        start1 = time.time()
        author.long_heavy(800)
        stop1 = time.time()
        assert round(
            stop1 - start1) == 0, 'Время выполнения не равно 0 секунд при повторSном вызове функции long_heavy с тем же аргументом'