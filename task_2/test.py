import inspect
# import output
import pytest
import author
import output

class TestContactClass:
    def test_usercode_has_precode_variables_and_functions(self):
        assert hasattr(author,
                       'Contact'), 'Проверьте, что в коде есть класс "Contact"'
        assert hasattr(author.Contact, 'show_contact'), 'Проверьте, что создали метод "show_contact" в классе'

        assert hasattr(author, 'print_contact'), 'Проверьте, что удалили функцию "print_contact() из кода"'
        assert hasattr(author, 'vlad'), 'Проверьте, что удалили функцию "print_contact() из кода"'
        assert hasattr(author,
                       'mike'), 'Проверьте, что удалили функцию "print_contact() из кода"'
    def test_vars_are_instances_of_class(self):
        assert inspect.isclass(author.Contact), 'Contact не явялется классом'
        assert isinstance(author.vlad, author.Contact), 'переменная vlad ссылается на экземпляр класса Contact'
        assert isinstance(author.mike,
                          author.Contact), 'переменная mike ссылается на экземпляр класса Contact'

    def test_ouput_show_contact(self):
        correct_mike_output = "Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6"
        correct_vlad_output = "Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12"
        assert correct_mike_output in output, "Проверьте, верно ли выведены контакты mike"
        assert correct_vlad_output in output, "Проверьте, верно ли выведены контакты vlad"
        assert author.mike.show_contact() == correct_mike_output, "Проверьте, верно ли выведены контакты mike"
        assert author.vlad.show_contact() == correct_vlad_output, "Проверьте, верно ли выведены контакты vlad"


