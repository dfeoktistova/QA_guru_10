import allure
from selene import browser, by, be


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    check_issue("issue_to_test_allure_report")


@allure.step("Открыть github")
def open_main_page():
    browser.open('https://github.com')


@allure.step("Найти репозиторий {repo} через поиск")
def search_for_repository(repo):
    browser.element('.header-search-button').should(be.visible).click()

    browser.element('#query-builder-test').should(be.visible).send_keys(repo)
    browser.element('#query-builder-test').should(be.visible).submit()


@allure.step("Перейти в репозиторий")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).should(be.visible).click()


@allure.step("Открыть таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").should(be.visible).click()


@allure.step("Проверить Issue с названием {name}")
def check_issue(name):
    browser.element(by.partial_text(name)).should(be.visible).click()