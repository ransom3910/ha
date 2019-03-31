from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://covanceprod.service-now.com/it_central/home.do")
#assert "Google" in driver.title
elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys("mjransom")
elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("I!lcagvvm008")
elem.send_keys(Keys.RETURN)
time.sleep(5)
#driver.find_element_by_xpath("//Classic UI")
#driver.get("https://covanceprod.service-now.com/navpage.do")
time.sleep(15)
driver.get("https://covanceprod.service-now.com/com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=c6bd7b116485810461f6f0e0ff1ff74f&sysparm_link_parent=90fce3916445810461f6f0e0ff1ff737&sysparm_catalog=e0d08b13c3330100c8b837659bba8fb4")
elem = driver.find_element_by_name("IO")
elem.send_keys("network support")

#driver.findElement(By.cssSelector("a[href*='long']")).click();
#driver.find_element_by_css_selector('''<a id="323bb07bc611227a018aea9eb8f3b35e" href="change_request.do?sys_id=-1&amp;sysparm_stack=change_request_list.do&amp;sysparm_view=changeChange&amp;sysparm_query=active=true" class="menu nav_menu_header" data-placement="bottom" data-cancelable="true" target="gsft_main">Create Normal Change</a>''').click()
#driver.find_element_by_link_text("Create Normal Change").click()
#driver.find_element_by_xpath(u'//a[text()="Create Normal Change"]').click()

#assert "No results found." not in driver.page_source
#driver.close()
