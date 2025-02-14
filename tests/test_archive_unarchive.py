from playwright.sync_api import Page, expect
from test_canevas import test_login
import pytest

@pytest.fixture
def run_before_every_test(page:Page):
    """Fixture to execute test_login before test is run"""
    test_login(page)
    yield page


def test_archive(run_before_every_test):
    page = run_before_every_test
    search_input = "13_ALLAUCH_AIRES MICHAEL_AMENAGEMENT D'UN RESTAURANT 250 ROUTE DES 4 SAISONS 13190 ALLAUCH"
    page.get_by_label("Nom du projet").fill(search_input)
    page.wait_for_selector("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i")
    expect(page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i")).to_have_class('mdi-folder-download mdi v-icon notranslate v-theme--light')
    page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i").click()
    expect(page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i")).to_have_class('mdi-archive mdi v-icon notranslate v-theme--light')
    page.locator("div:nth-child(7) > .v-input > .v-input__control > .v-field > .v-field__append-inner > .mdi-menu-down").click()
    page.get_by_text("Archivé", exact=True).click()
    page.get_by_label("Nom du projet").fill(search_input)
    expect(page.locator(".v-data-table__tbody tr.v-data-table__tr:nth-child(1) td:nth-child(2) span.project-name")).to_have_text(search_input)


def test_unarchive(run_before_every_test):
    page = run_before_every_test
    page.locator("div:nth-child(7) > .v-input > .v-input__control > .v-field > .v-field__append-inner > .mdi-menu-down").click()
    page.get_by_text("Archivé", exact=True).click()
    search_input = "13_ALLAUCH_AIRES MICHAEL_AMENAGEMENT D'UN RESTAURANT 250 ROUTE DES 4 SAISONS 13190 ALLAUCH"
    page.get_by_label("Nom du projet").fill(search_input)
    page.wait_for_selector("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i")
    expect(page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i")).to_have_class('mdi-archive mdi v-icon notranslate v-theme--light')
    page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i").click()
    expect(page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i")).to_have_class('mdi-folder-download mdi v-icon notranslate v-theme--light')
    page.reload()
    expect(page.locator('.v-data-table__tbody tr:nth-child(1) td:nth-child(2) span.project-name')).not_to_be_visible()












