import time

import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открыть github"):
        browser.open("https://github.com")

    with allure.step("Найти репозиторий {repo} через поиск"):
        s('.header-search-button').should(be.visible).click()

        s("#query-builder-test").should(be.visible).send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").should(be.visible).submit()

    with allure.step("Перейти в репозиторий"):
        s(by.link_text("eroshenkoam/allure-example")).should(be.visible).click()

    with allure.step("Открыть таб Issues"):
        s("#issues-tab").should(be.visible).click()

    time.sleep(20)

    with allure.step("Проверить Issue с названием {name}"):
        s(by.partial_text("issue_to_test_allure_report")).should(be.visible)