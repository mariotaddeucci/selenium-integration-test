from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def test_unauthorized_create_customer_group():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    def find_visible_element(by, value):
        return wait.until(EC.visibility_of_element_located((by, value)))

    # Access Admin Page
    driver.get("https://demo.opencart.com/admin/")
    driver.find_element(By.XPATH, '//button[text()=" Login"]').submit()

    # Add new customer group
    for link_text in ["Customers", "Customer Groups"]:
        find_visible_element(By.LINK_TEXT, link_text).click()
    find_visible_element(By.XPATH, '//a[@data-original-title="Add New"]').click()

    # Fill in form
    find_visible_element(
        By.XPATH, '//input[@placeholder="Customer Group Name"]'
    ).send_keys("Test Group")

    # Save
    find_visible_element(By.XPATH, '//button[@data-original-title="Save"]').click()

    alert_message = find_visible_element(By.CSS_SELECTOR, ".alert-danger").text

    # Check if unauthorized alert is displayed
    assert "invalid message" in alert_message, "Unauthorized alert is not displayed"

    driver.close()
