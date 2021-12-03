import output
from inspect import isfunction
import author


class TestDivideMaker:

    def test_code_has_precode_variables_and_methods(self):
        assert hasattr(author,
                       'make_divider_of'), 'Проверьте, что в коде написана функция "make_divder_of"'
        assert hasattr(author,
                       'div2'), 'Проверьте, что в коде присутсвует  переменная div2'
        assert hasattr(author,
                       'div5'), 'Проверьте, что в коде присутсвует  переменная div5'

    def test_return_type_is_func(self):
        div2 = author.make_divider_of(2)
        assert isfunction(
            div2), 'Убедитесь, что вызов функции make_divider_of возвращает функцию'

    def test_result_of_division(self):
        div2 = author.make_divider_of(2)
        assert div2(10) == 5, 'Функция div2(10) возвращает неверный результат'

    def test_output(self):
        assert '5.0' in output, 'Убедитесь, что print(div2(10)) печатает "5.0"'
        assert '4.0' in output, 'Убедитесь, что print(div5(20)) печатает "4.0"'
        assert '2.0' in output, 'Убедитесь, что print(div5(div2(20))) печатает "2.0"'
