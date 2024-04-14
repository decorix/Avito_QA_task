from playwright.sync_api import expect
from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        page.close()
        browser.close()

def test_visible_value(page):
    page.goto('https://www.avito.ru/avito-care/eco-impact', timeout=60000)
    expect(page.get_by_text("0").first).to_be_visible()
    expect(page.get_by_text("0").nth(1)).to_be_visible()
    expect(page.get_by_text("0").nth(2)).to_be_visible()

    location = page.locator(".desktop-wrapper-OutiE")
    location.screenshot(path="output/test_visible_value.png")

def test_visible_unit_measurement(page):
    page.goto('https://www.avito.ru/avito-care/eco-impact', timeout=60000)
    expect(page.get_by_text("кг CO₂", exact=True)).to_be_visible()
    expect(page.get_by_text("л воды")).to_be_visible()
    expect(page.get_by_text("кВт⋅ч энергии")).to_be_visible()

    location = page.locator(".desktop-wrapper-OutiE")
    location.screenshot(path="output/test_visible_unit_measurement.png")

def test_check_value(page):
    page.goto('https://www.avito.ru/avito-care/eco-impact', timeout=60000)
    elements = []
    element = page.locator('.desktop-value-Nd1tR').nth(0)
    element1 = page.locator('.desktop-value-Nd1tR').nth(1)
    element2 = page.locator('.desktop-value-Nd1tR').nth(2)
    elements.append(element)
    elements.append(element1)
    elements.append(element2)

    for elem in elements:
        text_content = elem.inner_text()

        value = float(text_content)

        assert value >= 0

    location = page.locator(".desktop-wrapper-OutiE")
    location.screenshot(path="output/test_check_value.png")

def test_check_unit_measurement(page):
    try:
        page.goto('https://www.avito.ru/avito-care/eco-impact', timeout=60000)
    except TimeoutError:
        print("Ошибка: Превышено время ожидания")
        return

    elements = []

    for i in range(3):
        elements.append(page.locator('.desktop-unit-puWVS').nth(i))

    text_content1 = elements[0].inner_text()
    text_content2 = elements[1].inner_text()
    text_content3 = elements[2].inner_text()

    assert text_content1 == 'кг\xa0CO₂'
    assert text_content2 == 'л\xa0воды'
    assert text_content3 == 'кВт⋅ч\xa0энергии'

    location = page.locator(".desktop-wrapper-OutiE")
    location.screenshot(path="output/test_check_unit_measurement.png")

def test_set_value(page):
    try:
        page.goto('https://www.avito.ru/avito-care/eco-impact', timeout=60000)
    except TimeoutError:
        print("Ошибка: Превышено время ожидания")
        return

    element = page.wait_for_selector('.desktop-value-Nd1tR')
    if not element:
        print("Элемент не найден")
        return

    value = "1000"
    page.eval_on_selector('.desktop-value-Nd1tR', f'(element, value) => element.innerText = value', value)

    counter = page.locator(".desktop-wrapper-OutiE")
    counter.screenshot(path="output/test_set_value.png")