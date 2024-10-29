<<<<<<< HEAD
# SauceDemo_TEST
=======
# SauceDemo_AutomationPyTest
>>>>>>> 0ece91e23c7f36eaa238eebba6c6c914291062c3

Sauce Demo Test Automation Project Overview This project is an automated testing framework for the Sauce Demo website (https://www.saucedemo.com/) using Selenium WebDriver with Python and pytest. It implements the Page Object Model (POM) design pattern for better maintainability and reusability.
Prerequisites Python 3.x pip (Python package installer) Installation Clone the repository: bash

Verify

Open In Editor Edit Copy code git clone https://github.com/yourusername/sauce-demo-automation.git cd sauce-demo-automation Install required packages: bash

Verify

Open In Editor Edit Copy code pip install -r requirements.txt Required Packages

Verify

Open In Editor Edit Copy code selenium pytest pytest-html webdriver-manager Test Cases Covered Login functionality Successful login with standard user Login attempt with locked-out user Inventory functionality Adding items to cart Verifying cart updates Cart functionality Verifying items in cart Checkout process Complete purchase flow Logout functionality Running Tests Run all tests: bash

Verify

Open In Editor Edit Copy code python run_tests.py Run specific test markers: bash

Verify

Open In Editor Edit Copy code pytest -v -m login pytest -v -m inventory pytest -v -m cart pytest -v -m checkout pytest -v -m logout Generate HTML Report: bash

Verify

Open In Editor Edit Copy code pytest --html=reports/report.html --self-contained-html Test Reports HTML reports are automatically generated in the reports folder Reports include test results, execution time, and failure details Each report is timestamped for better tracking Project Components Pages base_page.py: Contains common methods used across all page objects login_page.py: Login page elements and actions inventory_page.py: Product inventory page elements and actions cart_page.py: Shopping cart page elements and actions checkout_page.py: Checkout process page elements and actions Tests conftest.py: pytest fixtures and test configuration test_sauce_demo.py: Test cases implementation Configuration test_data.py: Test data and constants pytest.ini: pytest configuration and custom markers Contributing Fork the repository Create your feature branch (git checkout -b feature/AmazingFeature) Commit your changes (git commit -m 'Add some AmazingFeature') Push to the branch (git push origin feature/AmazingFeature) Open a Pull Request

Author Rawan Tourky

Acknowledgments Sauce Demo for providing the test website Selenium WebDriver pytest framework Notes Make sure to update the credentials in test_data.py as needed The framework uses Edge WebDriver by default, but can be modified to use other browsers Screenshots on failure can be enabled by adding custom code to the base page class

SauceDemo_TEST
