import allure
from selene import browser, by, be
from allure_commons.types import Severity

@allure.tag('web')
@allure.feature("Задачи в репозитории")
@allure.story("Успешная проверка Issue")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "feoktoster")
@allure.description("Тест для проверки поиска необходимой информации")
@allure.link("https://github.com", name="Testing")
def test_labels_steps():
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

    @allure.step("Проверить Issue с названием {issue}")
    def check_issue(issue):
        browser.element(by.partial_text(issue)).should(be.visible)

    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    check_issue("issue_to_test_allure_report")