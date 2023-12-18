import os

import pytest
from selene import browser
from selenium import webdriver

from utils import attach
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        # '--browser',
        # help='Браузер в котором будут запущены тесты',
        # choices=['firefox', 'chrome'],
        # default='chrome'
        '--browser_version', default='100.0'
    )


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
