# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import sys
import locale


# driver = webdriver.Chrome()
#
# driver.get("https://www.cian.ru/#")
#
# login_btn = driver.find_element_by_id('login-btn').click()
#
# time.sleep(1)
#
# login = driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Email или ID']")
# login.clear()
#
# password = driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Пароль']")
# password.clear()
#
# login.send_keys('15075273')
# password.send_keys('Colliers2019')
#
# enter_button = driver.find_element_by_xpath("//button[@class='button_component-button-gHcb1jHXKSo"
#                                             " button_component-M-4M1VnolQXYs button_component-default-2YMSqUd1jOi"
#                                             " button_component-primary-9zK1M8zBN62 login-form_submit']").click()
#
#
# time.sleep(3)
#
#
# edit_page = driver.get("https://www.cian.ru/cat.php?id_user=15075273&deal_type=1&offices=yes&engine_version=2")
#
# driver.find_element_by_xpath("//div[@id='offer_170303364']"
#                                 "//a[@href='/realty/add1.aspx?id=170303364']").click()
#
#
# id = 170303364
# area = 1253
# object_link = "https://www.cian.ru/realty/add1.aspx?id={}".format(id)
# totalArea = '{}'.format(area)
#
#
# driver.get(object_link)
#
# #time.sleep(4)
#
# total_area = driver.find_element_by_xpath("//input[@name='totalArea']")
# print('before clear')
# total_area.clear()
#
# total_area.send_keys(totalArea)


# class UpdateBase():
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.id = 0
#         self.area = 0
#         self.object_link = "https://www.cian.ru/realty/add1.aspx?id={}".format(id)
#
#     def login(self):
#         self.driver.get("https://www.cian.ru/#")
#         self.driver.find_element_by_id('login-btn').click()
#         time.sleep(1)
#
#         login = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Email или ID']")
#         login.clear()
#
#         password = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Пароль']")
#         password.clear()
#
#         login.send_keys('15075273')
#         password.send_keys('Colliers2019')
#
#         self.driver.find_element_by_xpath("//button[@class='button_component-button-gHcb1jHXKSo"
#                                           " button_component-M-4M1VnolQXYs button_component-default-2YMSqUd1jOi"
#                                           " button_component-primary-9zK1M8zBN62 login-form_submit']").click()
#
#         time.sleep(3)
#
#     def update(self):
#         self.id = 170303364
#         self.area = 1253
#         totalArea = '{}'.format(self.area)
#
#         object_link = self.object_link.format(self.id)
#         self.driver.get(object_link)
#         total_area = self.driver.find_element_by_xpath("//input[@name='totalArea']")
#         total_area.clear()
#         total_area.send_keys(totalArea)


# class UpdateBase():
#     def __init__(self):
#         data = pd.read_excel('/home/EU/yury.festa/PycharmProjects/COLLIERS/industrial.xlsx')
#         print(data)
#         self.driver = webdriver.Chrome()
#         self.id = [170303364, 188523997]
#         self.area = [2222, 3333]
#         self.object_link = "https://www.cian.ru/realty/add1.aspx?id={}"
#
#     def login(self):
#         self.driver.get("https://www.cian.ru/#")
#         self.driver.find_element_by_id('login-btn').click()
#         time.sleep(1)
#
#         login = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Email или ID']")
#         login.clear()
#
#         password = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Пароль']")
#         password.clear()
#
#         login.send_keys('15075273')
#         password.send_keys('Colliers2019')
#
#         self.driver.find_element_by_xpath("//button[@class='button_component-button-gHcb1jHXKSo"
#                                           " button_component-M-4M1VnolQXYs button_component-default-2YMSqUd1jOi"
#                                           " button_component-primary-9zK1M8zBN62 login-form_submit']").click()
#
#         print('Login finished')
#         time.sleep(3)
#
#     def update(self):
#         for i in range(data.id.unique()):
#             obj_id = self.id[i]
#             area = self.area[i]
#             print('id', obj_id)
#             print('i', i)
#             totalArea = '{}'.format(area)
#
#             print(totalArea)
#             object_link = self.object_link.format(obj_id)
#             self.driver.get(object_link)
#             total_area = self.driver.find_element_by_xpath("//input[@name='totalArea']")
#             total_area.clear()
#             total_area.send_keys(totalArea)
#             print('Updated Object', obj_id)
#             time.sleep(5)


class UpdateBase(object):
    def __init__(self):
        data = pd.read_excel('/home/EU/yury.festa/Рабочий стол/testnew.xlsx')
        # data = pd.read_excel(input('Paste path to ".xlsx" file: '))
        print(data)
        self.driver = webdriver.Chrome()
        self.obj_id = data['ID'].tolist()
        self.area = data['area'].tolist()
        self.minarea = data['minArea'].tolist()
        self.ceilingheight = data['ceilingHeight'].tolist()
        self.columngrid = data['columnGrid'].tolist()
        self.floormaterial = data['floorMaterial'].tolist()

        print('Objects id`s', self.obj_id)
        print('Objects area', self.area)
        self.object_link = "https://www.cian.ru/realty/add1.aspx?id={}"

    def login(self):
        print('Start logging in')
        self.driver.get("https://www.cian.ru/#")
        self.driver.find_element_by_id('login-btn').click()

        time.sleep(1)

        login = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Email или ID']")
        login.clear()

        password = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Пароль']")
        password.clear()

        login.send_keys('***')
        password.send_keys('***')

        self.driver.find_element_by_xpath("//button[@class='button_component-button-gHcb1jHXKSo"
                                          " button_component-M-4M1VnolQXYs button_component-default-2YMSqUd1jOi"
                                          " button_component-primary-9zK1M8zBN62 login-form_submit']").click()

        print('Login finished')
        time.sleep(3)

    def update(self):
        for i in range(len(self.obj_id)):
            obj_id = self.obj_id[i]
            totalArea = self.area[i]
            minArea = self.minarea[i]
            ceilingHeight = self.ceilingheight[i]
            columnGrid = self.columngrid[i]
            floorMaterial = self.floormaterial[i]

            print('Star updating object with id', obj_id)

            object_link = self.object_link.format(obj_id)
            self.driver.get(object_link)

            total_area_input = self.driver.find_element_by_xpath("//input[@name='totalArea']")
            total_area_input.clear()
            total_area_input.send_keys(totalArea)

            try:
                min_area_input = self.driver.find_element_by_xpath("//input[@name='minArea']")
                min_area_input.clear()
                min_area_input.send_keys(minArea)

            except Exception:
                print('No minArea')

            ceiling_height_input = self.driver.find_element_by_xpath("//input[@name='building.ceilingHeight']")
            ceiling_height_input.clear()
            ceiling_height_input.send_keys(ceilingHeight)

            column_grid_input = self.driver.find_element_by_xpath("//input[@name='columnGrid']")
            column_grid_input.clear()
            column_grid_input.send_keys(columnGrid)

            floor_material_select_find = self.driver.find_elements_by_xpath(
                "//button[@class='cui-button cui-button_look_gray']")
            floor_material_select_find[1].click()

            floor_material_select_from_list = self.driver.find_elements_by_xpath("//li[@class='cui-dropdown__item']")
            print(floorMaterial)
            for i in range(8):
                print('type of floor',floor_material_select_from_list[i])

            if 'полимерный' in floorMaterial:
                floor_material_select_from_list[0].click()
            elif 'бетон' in floorMaterial:
                floor_material_select_from_list[1].click()
            elif 'линолеум' in floorMaterial:
                floor_material_select_from_list[2].click()
            elif 'асфальт' in floorMaterial:
                floor_material_select_from_list[3].click()
            elif 'плитка' in floorMaterial:
                floor_material_select_from_list[4].click()
            elif 'наливной' in floorMaterial:
                floor_material_select_from_list[5].click()
            elif 'железобетонный' in floorMaterial:
                floor_material_select_from_list[6].click()
            elif 'дерево' in floorMaterial:
                floor_material_select_from_list[7].click()
            elif 'ламинат' in floorMaterial:
                floor_material_select_from_list[8].click()

            print('Object', obj_id, ' updated')
            time.sleep(5)


process = UpdateBase()
process.login()
process.update()
