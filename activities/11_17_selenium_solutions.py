print('''PRACTICE B

Write a script to get http://reynoldsnlp.com/scrape/aa.html and
save the source html to a local file.''')

input('Press [return] to run code for PRACTICE B.\n\n\n')

from selenium import webdriver  # noqa: E402

driver = webdriver.Chrome()
driver.get("http://reynoldsnlp.com/scrape/aa.html")
with open('rnlp_aa.html', 'w') as f:
    print(driver.page_source, file=f)
    print(driver.page_source)
driver.close()

input('Press [return] to continue.\n\n\n')


print('''PRACTICE C

Write a script to open https://www.google.com and search for
`selenium-python tutorial`. Print the contents of each <cite> tag.''')

input('Press [return] to run code for PRACTICE C.\n\n\n')

from selenium import webdriver  # noqa: E402
from selenium.webdriver.common.keys import Keys  # noqa: E402
from selenium.webdriver.support.ui import WebDriverWait  # noqa: E402


driver = webdriver.Chrome()
driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("selenium-python tutorial")
elem.send_keys(Keys.RETURN)

# Waiting might be necessary for AJAX updates
# WebDriverWait(driver, 10).until(lambda x: x.find_element_by_tag_name('cite'))

for result in driver.find_elements_by_tag_name('cite'):
    print(result.text)

input('Press [return] to close Chrome driver.')
driver.close()
