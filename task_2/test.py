import inspect
import output
import pytest
import usercode

class TestContactClass:
    def does_method_show_contact_exist(self):
        assert hasattr(usercode.Contact, 'show_contact'), 'Проверьте, что создали метод "show_contact" в классе'
    def does_not_method_print(self):
        assert hasattr(usercode, 'print_contact'), 'Проверьте, что удалили функцию "print_contact() из кода"'
    def test_ouput_show_contact(self):
        mike_output = "Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6"
        vlad_output = "Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12"
        assert mike_output in output, "Проверьте, верно ли выведены контакты mike"
        assert vlad_output in output, "Проверьте, верно ли выведены контакты vlad"
        assert usercode.mike.show_contact() == mike_output, "Проверьте, верно ли выведены контакты mike"
        assert usercode.vlad.show_contact() == vlad_output, "Проверьте, верно ли выведены контакты vlad"


