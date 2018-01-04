from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GENIE_PATHNAME = "c:/AutomationTools/genie.crx"
EXPECTED_RESULT = 7.99
chrome_opt = Options()
chrome_opt.add_extension(GENIE_PATHNAME)
driver = webdriver.Chrome(chrome_options=chrome_opt)
driver.implicitly_wait(10)
# driver.get("https://www.kohls.com/product/prd-2994554/")
# # assert "Python" in driver.title
# driver.find_element_by_id("addtobagID").click()
# driver.find_element_by_class_name("checkout-link").click()
# time.sleep(3)

driver.get("https://www.pizzahut.com/index.php#/menu/pizza/popular-pizzas")
# driver.get("https://www.pizzahut.com/index.php#/localize/pizza/")
driver.find_element_by_id("lg-nav-menu").click()
driver.find_element_by_id("lg-nav-pizza").click()
# driver.find_element_by_css_selector("#tile-cheese-pizza > div > div.panel-body.bg-border-color.tile-padding.wrapper > div.product > div.product-buttons > div.productControllers.custom-product-ctrls > div > a.btn.btn-primary.btnModal").click()
driver.find_element_by_id("tile-cheese-pizza").find_element_by_css_selector("div.productControllers.custom-product-ctrls > div > a.btn.btn-primary.btnModal").click()
driver.find_element_by_id("find-occasion-carryout").click()
driver.find_element_by_css_selector(".col-md-12.col-xs-12.col-lg-12.right-inner-addon.ph-padding-left-0.ph-padding-right-0 > input").send_keys("78701")
driver.find_element_by_id("ph-find-store").click()
driver.find_element_by_css_selector("#ph-localization-id > div.row.ph-syo-results > div:nth-child(3) > div.ng-scope.ph-stores-group.ph-scrollbar > div > div:nth-child(1) > div > div > div > div.col-xs-12.ph-margin-top-15 > a").click()
# shops_block_element = driver.find_elements_by_class_name("row ph-font-12 custom-ct-di ng-scope")
# for current_shop_block_element in shops_block_element:
#     if (current_shop_block_element.find_elements_by_class_name("marker_label ng-binding") == "1"):
#         current_shop_block_element.find_element_by_tag_name("a").click()
# driver.find_elements(".col-xs-12.ph-margin-top-15 > a")[0].click()
#
Select(driver.find_element_by_id("size-cheese-pizza")).select_by_visible_text("Large")
# menu_items = driver.find_elements_by_class_name(".img-responsive.ph-img-full-width.img-position")
# pizza_menu_item = None;
# for current_element in menu_items:
#     if (current_element.get_attribute("src").find("New_Pizza")!= -1):
#        current_element.click()
# driver.find_element_by_id("pd-cheese-pizza").find_element_by_css_selector(".productButtons.ng-scope > .btn.btn-primary.btnHome").click()
# # for current_add_buttons in driver.find_elements_by_class_name(".panel-body.bg-border-color.tile-padding wrapper"):
# #     if (current_add_buttons.find_element_by_css_selector("#close-cheese-pizza + .ng-scope > h4").getAttribute("innerHTML") == "")
driver.find_element_by_id("ato-cheese-pizza").click()
# driver.find_element_by_css_selector(".ph-cart-popover-trigger.ph-price.ng-scope.onelinetxt > a").click()
# driver.find_element_by_css_selector("#desktop-header > div > div.col-sm-4.col-lg-4.col-lg-offset-1.cart.hidden-xs.address-border > div > div.pointer-cursor.ph-cart-popover-trigger.ph-price.ng-scope > a").click()
# sum_element = driver.find_element_by_css_selector("span.onelinetxt > a.ph-ghost-link > .price.ph-cart-price.ng-binding")
print (driver.find_elements_by_css_selector("span.onelinetxt > a.ph-ghost-link"))#.click()
driver.find_element_by_css_selector("#desktop-header > div > div.col-sm-4.col-lg-4.col-lg-offset-1.cart.hidden-xs.address-border > div > div.pointer-cursor.ph-cart-popover-trigger.ph-price.ng-scope > a").click()
# print (sum_element.get_attribute('innerHTML'))
# regular_price = ((re.search('[\d.*]'), sum_element.text()).group(0))
# print(regular_price)
# sum_element.find_element_by_xpath("//..").click()

# sum_element = driver.find_element_by_css_selector("h3.ph-no-wrap > .ng-binding")
sum_element = driver.find_element_by_css_selector(".onelinetxt > a > span")
print (sum_element.get_attribute('innerHTML'))
# driver.switch_to.frame("__rmnGeniePopover")
root1 = driver.find_element_by_id('__genie_container')
shadow_root = driver.execute_script('return arguments[0].shadowRoot', root1)
shadow_root.find_element_by_css_selector(".rmnGenie-button.qa-test-codes").click()
shadow_root.find_element_by_css_selector(".qa-go-to-checkout.rmnGenie-button").click()
# WebDriverWait(driver,10).until((EC.new_window_is_opened()))
actual_result = driver.find_element_by_css_selector(".ng-scope > span > h4").get_attribute('innerHTML')
print (float(actual_result.replace("$", "")))

# driver.find_element_by_css_selector(".pointer-cursor.ph-cart-popover-trigger.ph-price.ng-scope > .ph-ghost-link").click()
# driver.find_element_by_id("checkout-top-os").click()

# driver.close()