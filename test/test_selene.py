from selene import by, be, browser
from selene.support.shared.jquery_style import s

repos = "eroshenkoam/allure-example"


def test_selene(browser_management):
    browser.open('https://github.com')
    s('[class="search-input"]').click()
    s('[id="query-builder-test"]').send_keys(repos).submit()
    s(by.link_text(repos)).click()
    s("#issues-tab").click()
    s(by.partial_text("issue_to_test_allure_report")).should(be.visible)