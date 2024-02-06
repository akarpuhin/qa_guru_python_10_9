from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
import allure


def test_dynamic_steps():
    with allure.step("Открыть главную страницу github"):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com')

    with allure.step('Найти репозиторий'):
        browser.element(".search-input").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step('Перейти по ссылке'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Открыть вкладку issues'):
        browser.element("#issues-tab").click()

    with allure.step('Проверить наличие issue 76'):
        browser.element(by.partial_text("#76")).should(be.visible)
