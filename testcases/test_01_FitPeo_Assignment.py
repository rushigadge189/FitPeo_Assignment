import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By


class Test_01_assignment_fitpeo_demo():

    def test_01_assig_demo_fitpeo(self):

        # Initialize WebDriver (make sure to provide the path to your chromedriver)
        driver=webdriver.Chrome();
        time.sleep(1) ;

        # Maximize The Window
        driver.maximize_window();
        time.sleep(1) ;

        # Add Synchronization
        driver.implicitly_wait(5) ;

        # Step 1: Navigate to FitPeo Homepage
        driver.get("https://www.fitpeo.com/") ;
        time.sleep(1) ;
        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step1.png") ;

        # Step 2: Navigate to the Revenue Calculator Page
        # Locate and click the link/button to navigate to the Revenue Calculator
        driver.find_element(By.XPATH, '//div[contains(text(),"Revenue Calculator")]').click() ;
        time.sleep(1) ;
        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step2.png") ;

        # Step 3: Scroll Down to the Slider section
        driver.execute_script("window.scrollBy(0,600)") ;
        time.sleep(1) ;
        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step3.png") ;

        # Step 4: Adjust the Slider to 820
        slider = driver.find_element(By.XPATH,"//input[@type='range']")
        action=ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(94, 0).release().perform()
        time.sleep(1)
        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step4.png") ;

        # Step 5: Update the Text Field to 560
        slider_textb=driver.find_element(By.XPATH, '//input[@aria-invalid="false"]')
        time.sleep(1) ;

        slider_textb.click() ;

        slider_textb.clear() ;

        slider_textb.send_keys('560') ;
        time.sleep(1) ;
        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step5.png") ;

        # Step 6: Validate Slider Value is updated to 560
        assert slider_textb.get_attribute('value') == "823", "Slider did not update to 560" ;
        time.sleep(1) ;
        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step6.png") ;


        driver.execute_script("window.scrollBy(0,300)") ;

        # Step 7: Select CPT Codes
        driver.find_element(By.XPATH, '(//input[@type="checkbox"])[1]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//input[@type="checkbox"])[3]').click() ;
        time.sleep(1) ;


        driver.execute_script("window.scrollBy(0,500)") ;

        driver.find_element(By.XPATH, '(//input[@type="checkbox"])[8]').click() ;
        time.sleep(1) ;

        total_reimbursement=driver.find_element(By.XPATH, '(//p[text()="111105"])[1]').text ;
        time.sleep(1) ;
        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step7.png") ;

        print(total_reimbursement)  ;

        # Step 8: Validate Total Recurring Reimbursement
        if  (total_reimbursement=="$111105") :
            assert True;
        else:
            assert False ;

        driver.save_screenshot("D:\\PYTHON CT15\\FitPeo\\screenshots\\step8.png") ;
        print("Automation script completed successfully!")

        time.sleep(5) ;
        driver.close() ;

