from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys


def check_exists_by_xpath(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


class Scraper:

    def __init__(self, location_index: int):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome("E:/ChwilowyPulpit/chromedriver.exe", chrome_options=options)
        self.location_index = location_index

    def get_all_property_data(self, count: int, website_link: str):
        try:
            price_list = []
            location_list = []
            area_list = []
            year_list = []
            room_list = []
            level_list = []
            state_list = []
            browser = self.browser
            browser.get(website_link)

            #articles_count = int(input("Type articles count:"))
            articles_count = 72

            browser.implicitly_wait(2)

            counter = 0
            index = 0
            for i in range(count):
                for j in range(articles_count):
                    property_data = self.get_property_data(browser, index)
                    index += 1
                    if type(property_data) == dict:
                        print(property_data)
                        price_list.append(str(property_data['price']))
                        location_list.append(str(property_data['location']))
                        area_list.append(str(property_data['area']))
                        year_list.append(str(property_data['year']))
                        room_list.append(str(property_data['rooms']))
                        level_list.append(str(property_data['level']))
                        state_list.append(str(property_data['state']))
                        counter += 1

                        print(counter)

                        housing_data = {
                            'price': price_list,
                            'location': location_list,
                            'area': area_list,
                            'year': year_list,
                            'rooms': room_list,
                            'level': level_list,
                            'state': state_list,
                        }
                        global df
                        df = pd.DataFrame(housing_data,
                                          columns=['price', 'location', 'area', 'year', 'rooms', 'level', 'state'])
                index = 0
                pager_next = browser.find_element_by_xpath(
                    "/html/body/div[3]/main/section[2]/div/div/div[1]/div/div[5]/div[1]/div[1]/nav/form/ul/li[6]/a")
                browser.get(pager_next.get_attribute("href"))
        except:
            one = random.randint(0, 100)
            two = random.randint(0, 100)
            three = random.randint(0, 100)
            df.to_csv(str(one) + str(two) + str(three) + "-" + str(self.location_index) + ".csv", sep=",", index=False)
            sys.exit()

    def get_property_data(self, driver, index):
        try:
            link = driver.find_element_by_xpath(
                f"/html/body/div[3]/main/section[2]/div/div/div[1]/div/article[{index + 1}]/div[1]/header/h3/a")
            driver.implicitly_wait(2)
            href = link.get_attribute("href")
            driver.get(href)

            area = check_exists_by_xpath("//*[@aria-label='Powierzchnia']", driver)
            year = check_exists_by_xpath("//*[@aria-label='Rok budowy']", driver)
            rooms = check_exists_by_xpath("//*[@aria-label='Liczba pokoi']", driver)
            level = check_exists_by_xpath("//*[@aria-label='Piętro']", driver)
            state = check_exists_by_xpath("//*[@aria-label='Stan wykończenia']", driver)
            if area and year and rooms and level and state:
                property_data = {
                    "price": driver.find_element_by_xpath("//*[@aria-label='Cena']").text,
                    "location": driver.find_element_by_xpath("//*[@aria-label='Adres']").find_element_by_tag_name(
                        "a").text,
                    "area": driver.find_element_by_xpath("//*[@aria-label='Powierzchnia']").find_element_by_class_name(
                        "css-1s5nyln").text,
                    "year": driver.find_element_by_xpath("//*[@aria-label='Rok budowy']").find_element_by_class_name(
                        "css-1s5nyln").text,
                    "rooms": driver.find_element_by_xpath("//*[@aria-label='Liczba pokoi']").find_element_by_class_name(
                        "css-1s5nyln").text,
                    "level": driver.find_element_by_xpath("//*[@aria-label='Piętro']").find_element_by_class_name(
                        "css-1s5nyln").text,
                    "state": driver.find_element_by_xpath(
                        "//*[@aria-label='Stan wykończenia']").find_element_by_class_name("css-1s5nyln").text,
                }
                driver.back()
                driver.implicitly_wait(2)
                return property_data
            else:
                driver.back()
                driver.implicitly_wait(2)
                return 0
        except:
            one = random.randint(0, 100)
            two = random.randint(0, 100)
            three = random.randint(0, 100)
            df.to_csv(str(one) + str(two) + str(three) + "-" + str(self.location_index) + ".csv", sep=",", index=False)
            sys.exit()

# try:
#     my_scraper = Scraper()
#     my_scraper.get_all_property_data(500,)
# except:
#     print('interrupted')
