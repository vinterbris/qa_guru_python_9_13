from selene import browser, be, have, command

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.subjects = browser.element('#subjectsContainer')
        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.all('[for^=hobbies-checkbox]')
        self.upload_picture = browser.element("#uploadPicture")
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.select_state_or_city = browser.all('[id^=react-select][id*=option]')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    def _fill_first_name(self, value):
        self.first_name.should(be.blank).with_(type_by_js=True).type(value)

    def _fill_last_name(self, value):
        self.last_name.should(be.blank).with_(type_by_js=True).type(value)

    def _fill_email(self, value):
        self.email.should(be.blank).with_(type_by_js=True).type(value)

    def _check_box_gender(self, gender):
        self.gender.element_by(have.value(gender)).element('..').click()

    def _fill_phone_number(self, value):
        self.phone_number.should(be.blank).with_(type_by_js=True).type(value)

    def _fill_date_of_birth(self, day, month, year):
        self.date_of_birth.click()
        self.month_of_birth.type(month)
        self.year_of_birth.type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def _pick_subjects(self, subject1, subject2):
        self.subjects.click()
        self.subjects_input.type(subject1).press_enter()
        self.subjects_input.type(subject2).press_enter()

    def _check_box_hobbies(self, hobbie1, hobbie2, hobbie3):
        self.hobbies.element_by(have.text(hobbie1)).click()
        self.hobbies.element_by(have.text(hobbie2)).click()
        self.hobbies.element_by(have.text(hobbie3)).click()

    def _upload_picture(self, value):
        self.upload_picture.set_value(resource.path(value))

    def _fill_current_address(self, value):
        self.current_address.should(be.blank).with_(type_by_js=True).type(value)

    def _pick_state_and_city(self, state, city):
        self.state.perform(command.js.scroll_into_view).click()
        self.select_state_or_city.element_by(have.text(state)).click()
        self.city.click()
        self.select_state_or_city.element_by(have.text(city)).click()

    def _submit_form(self):
        self.submit.perform(command.js.click)

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._check_box_gender(user.gender)
        self._fill_phone_number(user.phone_number)
        self._fill_date_of_birth(user.day_of_birth, user.month_of_birth, user.year_of_birth)
        self._pick_subjects(user.subjects[0], user.subjects[1])
        self._check_box_hobbies(user.hobbies[0], user.hobbies[1], user.hobbies[2])
        self._upload_picture(user.picture)
        self._fill_current_address(user.current_address)
        self._pick_state_and_city(user.state, user.city)
        self._submit_form()

    def assert_user_info(
            self, full_name, email, gender, phone_number, date_of_birth, subjects, hobbies,
            picture, current_address, city_and_state
    ):
        browser.element('.table').all('td:last-child').should(have.exact_texts(
            full_name, email, gender, phone_number, date_of_birth, subjects, hobbies,
            picture, current_address, city_and_state)
        )

    def close_modal_window(self):
        browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()
