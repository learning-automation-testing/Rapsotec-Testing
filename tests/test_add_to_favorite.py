from playwright.sync_api import Page, expect
from test_canevas import test_login
import pytest

@pytest.fixture
def run_before_every_test(page:Page):
    """Fixture to execute test_login before test is run"""
    test_login(page)
    yield page

def test_add_to_favorite(run_before_every_test):
    page = run_before_every_test
    search_input = '17_ROYAN_MEDIS_CARA_RENOVATION BATIMENT AERODROME_CT' 
    page.get_by_label("Nom du projet").fill(search_input)
    expect(page.locator(".v-data-table__tbody tr:nth-child(1) td:nth-child(1) span.v-btn__content i.mdi-star")).to_have_css("color", "rgb(158, 158, 158)")
    page.locator(".v-data-table__tbody tr:nth-child(1) td:nth-child(1)").click()
    expect(page.locator(".v-data-table__tbody tr:nth-child(1) td:nth-child(1) span.v-btn__content i.mdi-star")).to_have_css("color", "rgb(252, 185, 2)")
    expect(page.locator("//label[text()='Favoris']/preceding-sibling::div//div[@class='v-switch__track']")).to_have_css("background-color", "rgb(66, 66, 66)")
    page.wait_for_selector("//label[text()='Favoris']/preceding-sibling::div//input[@type='checkbox']").check()
    expect(page.locator("//label[text()='Favoris']/preceding-sibling::div//input[@type='checkbox']")).to_be_checked()
    page.get_by_label("Nom du projet").fill(search_input)
    expect(page.locator('.v-data-table__tbody tr:nth-child(1) td:nth-child(2) span.project-name')).to_contain_text(search_input)


def test_remove_to_favorite(run_before_every_test):
    page = run_before_every_test
    search_input = '17_ROYAN_MEDIS_CARA_RENOVATION BATIMENT AERODROME_CT' 
    expect(page.locator("//label[text()='Favoris']/preceding-sibling::div//div[@class='v-switch__track']")).to_have_css("background-color", "rgb(66, 66, 66)")
    page.wait_for_selector("//label[text()='Favoris']/preceding-sibling::div//input[@type='checkbox']").check()
    expect(page.locator("//label[text()='Favoris']/preceding-sibling::div//input[@type='checkbox']")).to_be_checked()
    page.get_by_label("Nom du projet").fill(search_input)
    page.wait_for_selector(".v-data-table__tbody tr:nth-child(1) td:nth-child(1) span.v-btn__content i.mdi-star")
    expect(page.locator(".v-data-table__tbody tr:nth-child(1) td:nth-child(1) span.v-btn__content i.mdi-star")).to_have_css("color", "rgb(252, 185, 2)")
    page.locator(".v-data-table__tbody tr:nth-child(1) td:nth-child(1)").click()
    expect(page.locator(".v-data-table__tbody tr:nth-child(1) td:nth-child(1) span.v-btn__content i.mdi-star")).to_have_css("color", "rgb(158, 158, 158)")














    


