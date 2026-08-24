# QA Playwright & Pytest Automation Framework

Repositori ini berisi framework *End-to-End (E2E) Test Automation* dan *REST API Testing* menggunakan **Python**, **Playwright**, dan **Pytest**.

## 🛠️ Tech Stack & Features
- **Language & Framework**: Python 3.x, Playwright, Pytest
- **Design Pattern**: Page Object Model (POM)
- **Testing Types**:
  - **UI Automation**: Login Authentication, Data-Driven Testing, E2E Checkout Flow.
  - **API Automation**: REST API GET & POST Endpoints Validation (`/posts`).
- **Reporting**: Pytest-HTML dengan fitur *Auto-Screenshot on Failure*.
- **CI/CD Pipeline**: GitHub Actions otomatis mengeksekusi *test suite* pada setiap `git push`.

## 🚀 Cara Menjalankan Tes Lokal
```bash
pytest