from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os 



try: 
    

    
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  
    print(current_dir)# получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'qanotes.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)
    first_name = browser.find_element(By.TAG_NAME, "input")
    first_name.send_keys("1")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("1")
    
    email = browser.find_element(By.NAME, "email")
    email.send_keys("1")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()