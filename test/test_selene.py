import time
from selene import by, be, browser
from selene.support.shared.jquery_style import s

REPO_NAME = "eroshenkoam/allure-example"


def test_selene(browser_management):
    browser.open('https://github.com')
    s('[class="search-input"]').click()
    time.sleep(3)
    s('[id="query-builder-test"]').send_keys(REPO_NAME).submit()
    time.sleep(3)
    s(by.link_text(REPO_NAME)).click()
    time.sleep(3)
    s("#issues-tab").click()
    time.sleep(3)
    s(by.partial_text("issue_to_test_allure_report")).should(be.visible)