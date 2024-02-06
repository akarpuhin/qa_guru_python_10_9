from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
import allure
from utils.dec_steps import open_git_main_page, open_issue_tab, search_repository, go_to_repository, \
    should_see_issue_with_number


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


def test_decorator_steps():
    open_git_main_page()
    search_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")
