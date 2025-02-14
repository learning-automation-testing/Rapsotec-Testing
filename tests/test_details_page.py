from playwright.sync_api import expect, Page
from test_canevas import test_login
import pytest

@pytest.fixture
def run_before_every_test(page:Page):
    """Fixture to execute test_login before test is run"""
    test_login(page)
    yield page

def test_details_page(run_before_every_test):
    page=run_before_every_test
    page.get_by_label("Nom du projet").fill('NANTES - Axis - Attestation PMR')
    page.locator("span[class='project-name']").click()
    page.wait_for_url("https://front.staging.infra-rapsotec.com/projects/389277")
    page.wait_for_timeout(5000)
    expect(page.locator("//span[normalize-space()='Voir fiche identité']")).to_be_visible()