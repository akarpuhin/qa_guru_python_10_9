from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
import allure


@allure.step("Открыть главную страницу github")
def open_git_main_page():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://github.com")


@allure.step("Найти репозиторий {repo}")
def search_repository(repo):
    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").submit()


@allure.step("Перейти по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открыть вкладку Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверить наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text("#76")).should(be.visible)