
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By



# Set up the Chrome driver
driver = webdriver.Chrome()

# Main task
try:
    # Open a web browser at the URL https://www.playtech.ee
    driver.get("https://www.playtech.ee")

    # Click on the internship tab using coordinates
    tab_x_coord = 850
    tab_y_coord = 50
    actions = webdriver.ActionChains(driver)
    actions.move_by_offset(tab_x_coord, tab_y_coord)
    actions.click()
    actions.perform()

    # Verify if the “Development QA Engineer (Intern)” position is shown on the page
    job_title = "Development QA Engineer (Intern)"
    job_title_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{job_title}')]")
    assert job_title_element.is_displayed(), f"Job title '{job_title}' not found on the page"

    # Export main task step 3’s result as .txt file
    output_file = "job_title.txt"
    with open(output_file, "w") as f:
        f.write(job_title)
        f.close()
except:
    output_file = "job_title.txt"
    print('Job title not found')
    with open(output_file, "w") as f:
        f.write(job_title + ' not found on page.')
        f.close()


finally:
    # Close the browser
    driver.quit()