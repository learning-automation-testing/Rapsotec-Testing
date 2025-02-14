from playwright.async_api import Page, expect
import re
from dotenv import load_dotenv
import os

load_dotenv()


def test_login(page:Page):
    usernaame = os.getenv("EMAIL_Rapso")
    PASSWORD = os.getenv("PASSWORD_Rapso")
    page.goto('https://front.staging.infra-rapsotec.com')
    page.wait_for_load_state("load")
    page.get_by_test_id('connectWithUsernameAndPassword').click()
    page.wait_for_selector("//input[@id='username']")
    page.wait_for_selector("//input[@id='password']")
    page.locator("//input[@id='username']").fill(usernaame)
    page.locator("//input[@id='password']").fill(PASSWORD)
    page.locator("//button[@id='kc-login']").click()
    page.evaluate("localStorage.getItem('oidc.user:https://sso.staging.infra-socotec.net/auth/realms/socotec-user:rapsotec-front')")
    page.locator("//a[normalize-space()='CANEVAS']").click(timeout=60000)
    page.wait_for_url("https://front.staging.infra-rapsotec.com/projects")

    # locqtor for project name
    # page.get_by_label("Nom du projet").fill('test App Center 2025')
    # # locator for number
    # page.get_by_label("Numéro de l'affaire").fill('xxx')
    # # Locator for client 
    # page.get_by_label("Client").fill('xxx')
    # # locator for city 
    # page.get_by_label("Ville").fill('xxx')
    # # locator for commandée/cloturée : aka open the dropwown
    # page.locator("//span[normalize-space()='Commandée / Clôturée']").click()
    # # click on en attente
    # page.locator("div.v-list-item__content >> text=En attente").click()
    # # click on Commandée
    # page.locator("//span[normalize-space()='En attente']").click()
    # page.locator("div.v-list-item__content >> text=Commandée").click()

    # click on Clôturée
    # page.locator("//span[normalize-space()='En attente']").click()
    # page.locator("div.v-list-item_content >> text=Clôturée").click()









