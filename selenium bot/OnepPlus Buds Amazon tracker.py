from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\program files (x86)\chromedriver.exe")
driver.get("https://www.amazon.co.uk/")

try:
    cookie_accept = driver.find_element_by_id("sp-cc-accept")
    cookie_accept.click()
except:
    driver.maximize_window()
driver.maximize_window()

query = "OnePlus Buds"
search = driver.find_element_by_id("twotabsearchtextbox")
search.clear()
search.send_keys(query)
search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)


product_selectors = ["#search > div.s-desktop-width-max.s-opposite-dir > div > div.s-matching-dir.sg-col-16-of-20.sg-" \
                     "col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s" \
                     "-search-results.sg-row > div:nth-child(" + str(i) + ")" for i in range(2, 24)]

search_results = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]")
for selector in product_selectors:
    product = search_results.find_element_by_css_selector(selector)
    if "oneplus" in product.text.lower():
        oneplus = product.text.splitlines()

print(oneplus)

for details in oneplus:
    if 'more' in details.lower() or 'sponsored' in details.lower() or "amazon's choice" in details.lower():
        oneplus.remove(details)

oneplus[2] = oneplus[2] + "." + oneplus[3]
del oneplus[3]

print(oneplus)

import pandas as pd

OnePlus_details = pd.DataFrame(oneplus, index=['Name', 'Number of ratings', 'Price', 'Expected delivery', 'Delivery fee', 'More buying options'], columns=['Details'])
OnePlus_details.to_excel("Oneplus Buds Amazon tracker.xlsx")

driver.quit()
