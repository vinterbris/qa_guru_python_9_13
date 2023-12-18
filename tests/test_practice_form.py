import allure

from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage

@allure.title("demoqa - test practice form")
@allure.tag("Registration", 'QA.GURU')
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sergey Dobrovolskiy")
@allure.parent_suite("demoqa")
@allure.suite("Регистрация пользователя")
@allure.sub_suite("Пользователь успешно регистрируется")
def test_registration():
    registration_page = RegistrationPage()
    with allure.step('Открываем форму регистрации'):
        registration_page.open()
    # WHEN
    with allure.step('Регистрируем пользователя'):
        registration_page.register(users.student)

    # THEN
    with allure.step('Проверка данных пользователя'):
        registration_page.assert_user_info(
            'Sergey Dobrovolskiy', 'dobrovolskiy@qa.ru', 'Male', '1002003040',
            '02 January,2100', 'Maths, Chemistry', 'Sports, Reading, Music', 'nolan.jpg',
            'Test Address', 'NCR Delhi'
        )
        # registration_page.close_modal_window()
