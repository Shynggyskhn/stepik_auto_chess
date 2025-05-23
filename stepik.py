from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math,time



try:
    
    def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = browser.find_element(By.ID, "price").text
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    book = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "book"))
        )
    book.click()
    
    san = browser.find_element(By.ID, "input_value").text
    convert = int(san)
    
    y = calc(convert)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    



finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
