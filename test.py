from selenium import webdriver


url = "https://wis.hufs.ac.kr/src08/jsp/index.jsp"

driver = webdriver.Chrome("/Users/0417taehyun/Documents/Mini Project/hufs-web-test/file/chromedriver")

driver.get(url = url)

user_id  = driver.find_element_by_xpath("/html/body/div[1]/form[3]/div[2]/div/div[2]/div/input[1]")
password = driver.find_element_by_xpath('//*[@id="password"]')

user_id.send_keys("")
password.send_keys("")

login_btn = driver.find_element_by_xpath("/html/body/div[1]/form[3]/div[2]/div/div[2]/div/a")

login_btn.click()

left = driver.find_element_by_name("left")

driver.switch_to.frame(left)

menu_frame = driver.find_element_by_name("MenuFrame")

driver.switch_to.frame(menu_frame)

major_menu_btn = driver.find_element_by_css_selector("body > div > a:nth-child(3)")

major_menu_btn.click()

major_btn = driver.find_element_by_xpath('//*[@id="div7"]/a[1]')

major_btn.click()

driver.switch_to.default_content()

body = driver.find_element_by_name("body")

driver.switch_to.frame(body)

first_major = driver.find_element_by_xpath("/html/body/div[1]/form/div/table/tbody/tr[2]/td[3]").text
second_major = driver.find_element_by_xpath("/html/body/div/form/div/table/tbody/tr[3]/td[3]").text

driver.close()

first_major = first_major.split()[0]
second_major = second_major.split()[0]

print("제 1전공: ", first_major)
print("이중 전공: ", second_major)
