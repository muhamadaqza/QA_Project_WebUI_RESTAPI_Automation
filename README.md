\# 🧪 Playwright Python Test Automation Portfolio



Automated E2E test suite built with \*\*Playwright (Python)\*\* and \*\*Pytest\*\* using the \*\*Page Object Model (POM)\*\* design pattern, integrated with \*\*GitHub Actions CI/CD\*\*.



\## 🚀 Features

\- \*\*Framework\*\*: Playwright + Pytest

\- \*\*Pattern\*\*: Page Object Model (POM)

\- \*\*CI/CD\*\*: GitHub Actions (runs automatically on push/PR)

\- \*\*Reporting\*\*: Auto-generated HTML Test Report uploaded as CI artifact



\## 🛠️ Project Structure

```text

.

├── .github/workflows/

│   └── playwright.yml   # CI/CD Pipeline configuration

├── pages/

│   └── login\_page.py    # POM Locators \& Actions

├── tests/

│   └── test\_login.py    # Test Suites (Positive \& Negative scenarios)

├── conftest.py          # Pytest browser fixture setup

├── pytest.ini           # Pytest runner \& HTML report settings

└── requirements.txt     # Python dependencies

