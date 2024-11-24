from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver (make sure to provide the path to your chromedriver)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

try:
    # Step 1: Navigate to FitPeo Homepage
    driver.get("https://fitpeo.com")  # Replace with the actual URL of the FitPeo Homepage
    driver.maximize_window()

    # Step 2: Navigate to the Revenue Calculator Page
    # Locate and click the link/button to navigate to the Revenue Calculator
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator"))).click()

    # Step 3: Scroll Down to the Slider section
    slider_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".slider-section"))
        # Use the actual CSS selector or unique identifier for the slider section
    )
    driver.execute_script("arguments[0].scrollIntoView();", slider_section)

    # Step 4: Adjust the Slider to 820
    slider = driver.find_element(By.XPATH,
                                 "//input[@type='range']")  # Adjust the XPath or selector to locate the slider
    ActionChains(driver).click_and_hold(slider).move_by_offset(200, 0).release().perform()

    # Check i820f the value is updated to
    slider_value = driver.find_element(By.XPATH, "//input[@id='slider-value']")  # Adjust selector if needed
    assert slider_value.get_attribute('value') == "820", "Slider is not set to 820"

    # Step 5: Update the Text Field to 560
    slider_value.click()
    slider_value.clear()
    slider_value.send_keys("560")
    slider_value.send_keys(Keys.RETURN)

    # Step 6: Validate Slider Value is updated to 560
    assert slider.get_attribute('value') == "560", "Slider did not update to 560"

    # Step 7: Select CPT Codes
    cpt_codes = ["99091", "99453", "99454", "99474"]
    for code in cpt_codes:
        checkbox = driver.find_element(By.XPATH,
                                       f"//input[@value='CPT-{code}']")  # Use the correct selector for checkboxes
        if not checkbox.is_selected():
            checkbox.click()

    # Step 8: Validate Total Recurring Reimbursement
    total_reimbursement = driver.find_element(By.XPATH,
                                              "//header[@id='total-reimbursement']")  # Replace with actual selector
    assert total_reimbursement.text == "$110700", "Total Reimbursement does not match the expected value of $110700"

    print("Automation script completed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)
    driver.quit()
