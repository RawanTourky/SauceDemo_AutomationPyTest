# File: tests/test_sauce_demo.py

import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data import TestData


class TestLogin:
    @pytest.mark.parametrize("username", TestData.USERS.keys())
    @pytest.mark.login
    def test_all_users_login(self, driver, username):
        """Test login functionality for all available users"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.navigate()
        start_time = time.time()
        login_page.login(username, TestData.VALID_PASSWORD)
        end_time = time.time()
        login_duration = end_time - start_time

        expected_result = TestData.USERS[username]["expected_result"]

        if expected_result == "success":
            assert inventory_page.is_visible(inventory_page.SHOPPING_CART), \
                f"Login failed for user: {username}"

            if username == "performance_glitch_user":
                assert login_duration > 2, \
                    f"Login duration ({login_duration:.2f}s) shorter than expected for performance_glitch_user"

            elif username == "problem_user":
                assert inventory_page.verify_problem_user_behavior(), \
                    "Problem user specific behavior not detected"


class TestCartFunctionality:
    @pytest.mark.cart
    def test_cart_functionality(self, driver):
        """Test cart functionality"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        # Login and add items to cart
        login_page.navigate()
        login_page.login("standard_user", TestData.VALID_PASSWORD)

        # Add multiple items and verify cart
        items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
        for item in items_to_add:
            inventory_page.add_to_cart(item)

        inventory_page.click_cart()

        # Verify cart contents
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == len(items_to_add), "Cart item count mismatch"
        for item in items_to_add:
            assert cart_page.is_item_in_cart(item), f"Item {item} not found in cart"

    @pytest.mark.cart
    def test_add_and_remove_all_items(self, driver):
        """Test adding all items to the cart and removing them"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        # Login as a standard user
        login_page.navigate()
        login_page.login("standard_user", TestData.VALID_PASSWORD)

        # Add all items to the cart
        inventory_page.add_all_items_to_cart()

        # Verify that all items are in the cart
        inventory_page.click_cart()
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) > 0, "Cart should not be empty after adding items."

        # Remove all items from the cart
        cart_page.remove_all_items()

        # Verify that the cart is empty
        cart_page.click_cart()  # Click on the cart to view items
        cart_items_after_removal = cart_page.get_cart_items()
        assert len(cart_items_after_removal) == 0, "Cart should be empty after removing all items."

class TestCheckoutProcess:
    @pytest.mark.checkout
    def test_checkout_process(self, driver):
        """Test complete checkout process"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Step 1: Login and add item to cart
        login_page.navigate()
        login_page.login("standard_user", TestData.VALID_PASSWORD)
        inventory_page.add_to_cart("Sauce Labs Backpack")

        # Step 2: Navigate to the cart
        inventory_page.click_cart()

        # Step 3: Proceed to checkout
        cart_page.click_checkout()

        # Step 4: Fill in checkout information
        checkout_page.fill_checkout_information("John", "Doe", "12345")  # Example: first name, last name, zip code
        checkout_page.click_continue()  # Assuming there's a method to continue to the next step

        # Step 5: Complete the checkout process
        checkout_page.click_finish()  # Assuming there's a method to finish the checkout

        # Step 6: Verify that the order is confirmed and marked as "on delivery"
        confirmation_message = checkout_page.get_confirmation_message()  # Assuming this method retrieves the confirmation message
        assert "Thank you for your order!" in confirmation_message, "Order should be confirmed and dispatched."