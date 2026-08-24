import base64
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

# Hook otomatis untuk mengambil screenshot jika ada tes yang FAILED
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page')
        if page:
            # Ambil screenshot dan konversi ke Base64 String
            screenshot_bytes = page.screenshot()
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')

            if pytest_html:
                extra.append(pytest_html.extras.image(screenshot_base64, 'Screenshot on Failure'))
    report.extra = extra