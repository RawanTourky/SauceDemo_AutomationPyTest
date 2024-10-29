class TestData:
    BASE_URL = "https://www.saucedemo.com"
    VALID_PASSWORD = "secret_sauce"

    USERS = {
        "standard_user": {
            "expected_result": "success",
            "description": "Standard user with full access"
        },
        "locked_out_user": {
            "expected_result": "error",
            "description": "Locked out user"
        },
        "problem_user": {
            "expected_result": "success",
            "description": "User with intentional bugs"
        },
        "performance_glitch_user": {
            "expected_result": "success",
            "description": "User with slow performance"
        },
        "error_user": {
            "expected_result": "success",
            "description": "User with error states"
        },
        "visual_user": {
            "expected_result": "success",
            "description": "User with visual glitches"
        }
    }

    CUSTOMER_INFO = {
        "firstname": "John",
        "lastname": "Doe",
        "postal_code": "12345"
    }

    INVENTORY_ITEMS = {
        "backpack": "Sauce Labs Backpack",
        "bike_light": "Sauce Labs Bike Light",
        "bolt_shirt": "Sauce Labs Bolt T-Shirt"
    }

    CHECKOUT_INFO = {
        "success_message": "Thank you for your order!",
        "error_firstname": "Error: First Name is required",
        "error_lastname": "Error: Last Name is required",
        "error_postal": "Error: Postal Code is required"
    }

    ERROR_MESSAGES = {
        "locked_out": "Epic sadface: Sorry, this user has been locked out.",
        "invalid_credentials": "Epic sadface: Username and password do not match any user in this service",
        "empty_username": "Epic sadface: Username is required",
        "empty_password": "Epic sadface: Password is required"
    }