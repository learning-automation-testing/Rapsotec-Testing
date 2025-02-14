from playwright.sync_api import Page, expect
from test_canevas import test_login
import pytest 

@pytest.fixture
def run_before_every_test(page:Page):
    """Fixture to execute test_login before test is run"""
    test_login(page)
    yield page

def test_filter_by_favorite(run_before_every_test):
    page = run_before_every_test
    expect(page.locator("//label[text()='Favoris']/preceding-sibling::div//div[@class='v-switch__track']")).to_have_css("background-color", "rgb(66, 66, 66)")
    page.wait_for_selector("//label[text()='Favoris']/preceding-sibling::div//input[@type='checkbox']").check()
    expect(page.locator("//label[text()='Favoris']/preceding-sibling::div//input[@type='checkbox']")).to_be_checked()
    expect(page.locator("//label[text()='Favoris']/preceding-sibling::div//div[@class='v-switch__track']")).to_have_css("background-color", "rgb(252, 185, 2)")
    results = page.locator('.v-data-table__tbody tr td:nth-child(1)').all_text_contents()

def test_filter_by_pilote(run_before_every_test):
    page = run_before_every_test
    expect(page.locator("//label[text()= 'Voir les canevas où je suis intervenant et/ou pilote']/preceding-sibling::div//div[@class='v-switch__track']")).to_have_css("background-color", "rgb(66, 66, 66)")
    page.locator("//label[text()='Voir les canevas où je suis intervenant et/ou pilote']/preceding-sibling::div//input[@type='checkbox']").check()
    expect(page.locator("//label[text()='Voir les canevas où je suis intervenant et/ou pilote']/preceding-sibling::div//input[@type='checkbox']")).to_be_checked()
    expect(page.locator("//label[text()='Voir les canevas où je suis intervenant et/ou pilote']/preceding-sibling::div//div[@class='v-switch__track']")).to_have_css("background-color", "rgb(252, 185, 2)")

def test_filter_by_en_attente(run_before_every_test):
    page = run_before_every_test
    page.locator(".v-field__append-inner > .mdi-menu-down").first.click()
    page.get_by_text("En attente", exact=True).click()
    results = page.locator(".v-data-table__tbody tr td:nth-child(6) div.v-col p").all_text_contents()
    for result in results : 
        if result != "En attente":
            all_matched = False
            break
        all_matched = True
        assert all_matched == True

def test_filter_by_commandée(run_before_every_test):
    page = run_before_every_test
    page.locator(".v-field__append-inner > .mdi-menu-down").first.click()
    page.get_by_text("Commandée", exact=True).click()
    results = page.locator(".v-data-table__tbody tr td:nth-child(6) div.v-col p").all_text_contents()
    for result in results : 
        if result != "Commandée":
            all_matched = False
            break
        all_matched = True
        assert all_matched == True


def test_filter_by_closed(run_before_every_test):
    page = run_before_every_test
    page.locator(".v-field__append-inner > .mdi-menu-down").first.click()
    page.get_by_text("Clôturée", exact=True).click()
    results = page.locator(".v-data-table__tbody tr td:nth-child(6) div.v-col p").all_text_contents()
    for result in results : 
        if result != "Clôturée":
            all_matched = False
            break
        all_matched = True
        assert all_matched == True

def test_archive(run_before_every_test):
    page = run_before_every_test
    page.locator("div:nth-child(7) > .v-input > .v-input__control > .v-field > .v-field__append-inner > .mdi-menu-down").click()
    page.get_by_text("Archivé", exact=True).click()
    results = page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i").all()
    for result in results:
        check_class = result.get_attribute("class")
        if check_class == 'mdi-archive mdi v-icon notranslate v-theme--light':
            is_archived = True
        is_archived = False
        assert is_archived == True

def test_unarchive(run_before_every_test):
    page = run_before_every_test
    page.locator("div:nth-child(7) > .v-input > .v-input__control > .v-field > .v-field__append-inner > .mdi-menu-down").click()
    page.get_by_role("option", name="Non archivé").click()
    results = page.locator("tbody.v-data-table__tbody tr.v-data-table__tr td:nth-child(9)  span.v-btn__content i").all()
    for result in results:
        check_class = result.get_attribute("class")
        if check_class == 'mdi-folder-download mdi v-icon notranslate v-theme--light':
            is_archived = True
        is_archived = False
        assert is_archived == True




    
