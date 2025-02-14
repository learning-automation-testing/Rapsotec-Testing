from playwright.sync_api import Page, expect
from test_canevas import test_login
import re
import pytest


@pytest.fixture
def run_before_every_test(page:Page):
    """Fixture to execute test_login before test is run"""
    test_login(page)
    yield page

def test_search_by_name(run_before_every_test):
    page = run_before_every_test
    search_input = 'NANTES - Axis - Attestation PMR' 
    page.get_by_label("Nom du projet").fill(search_input)
    expect(page.locator(".v-data-table__tbody tr td")).not_to_contain_text("Aucun élément")
    number_of_responses = page.locator(".v-data-table__tbody tr td").count()
    assert number_of_responses >= 1
    text_contents = page.locator(".v-data-table__tbody tr td span.project-name").all_text_contents()
    words = search_input.split()
    for text in text_contents:
        if not any(re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE) for word in words):
            all_matched = False
            break  
        assert all_matched == True

def test_search_by_number(run_before_every_test):
    page = run_before_every_test
    number_affaire = '250111350000064'
    page.get_by_label("Numéro de l'affaire").fill(number_affaire)
    expect(page.locator(".v-data-table__tbody tr td")).not_to_contain_text("Aucun élément")
    number_of_responses = page.locator(".v-data-table__tbody tr td").count()
    assert number_of_responses >= 1
    text_contents = page.locator(".v-data-table__tbody tr td:nth-child(3)").all_text_contents()
    for text in text_contents:
        if re.search(r'\b250111350000064\b') not in text:
            all_matched = False
            break
        assert all_matched == True

def test_search_by_Client(run_before_every_test):
    page = run_before_every_test
    search_input = 'AB Land'
    page.get_by_label("Client").fill(search_input)
    expect(page.locator(".v-data-table__tbody tr td")).not_to_contain_text("Aucun élément")
    number_of_responses = page.locator(".v-data-table__tbody tr td").count()
    assert number_of_responses >= 1
    texts = page.locator(".v-data-table__tbody tr td:nth-child(4)").all_text_contents()
    words = search_input.split()
    for text in texts:
        if not any(re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE) for word in words):
            all_matched = False
            break  
        assert all_matched == True
        

def test_search_by_City(run_before_every_test):
    page = run_before_every_test
    city = "LANDERNEAU"
    page.get_by_label("Ville").fill(city)
    expect(page.locator(".v-data-table__tbody tr td")).not_to_contain_text("Aucun élément")
    results= page.locator(".v-data-table__tbody tr td").count()
    assert results >= 1
    texts = page.locator(".v-data-table__tbody tr td:nth-child(5)").all_text_contents()
    words = city.split()
    for text in texts:
        if not any(re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE) for word in words):
            all_matched = False
            break
        assert all_matched == True


def test_search_by_Pilote(run_before_every_test):
    page = run_before_every_test
    pilote = 'LOUIS'
    page.locator(".v-field--center-affix > div.v-field__field > label.v-field-label", has_text="Pilote").fill(pilote)
    expect(page.locator(".v-data-table__tbody tr td")).not_to_contain_text("Aucun élément")
    results = page.locator(".v-data-table__tbody tr td").count()
    assert results >= 1
    texts = page.locator(".v-data-table__tbody tr td:nth-child(7)").all_text_contents()
    words = pilote.split()
    for text in texts:
        if not any(re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE) for word in words):
            all_matched = False
            break
        assert all_matched == True

