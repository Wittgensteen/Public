#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QApplication, QFileDialog, QStatusBar,QMainWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QIcon, QPalette, QBrush

from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains


class UpdateBase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.object_link = "https://www.cian.ru/realty/add1.aspx?id={}"
        # log = Interface.statusBar(QMainWindow)
        # log().showMessage('test')

    def get_data(self, data_path):
        data = pd.read_excel(data_path)
        print(data)
        self.obj_id = data['ID'].tolist()  # ID объекта
        self.area = data['area'].tolist()  # Площадь
        self.minarea = data['minArea'].tolist()  # Минимальная площадь
        self.floornumber = data['floorNumber'].tolist()  # номер этажа
        self.floorcount = data['floorCount'].tolist()  # колличество этажей
        self.ceilingheight = data['ceilingHeight'].tolist()  # Высота потолков
        self.columngrid = data['columnGrid'].tolist()  # Сетка колонн
        self.floormaterial = data['floorMaterial'].tolist()  # Материал пола
        self.conditiontype = data['conditionType'].tolist()  # Состояние
        self.gatestype = data['gatesType'].tolist()  # Ворота
        self.waterpipescount = data['waterPipesCount'].tolist()  # Кол-во мокрых точек
        self.electricitypower = data['electricityPower'].tolist()  # Электрическая мощность
        self.parkinglocationtype = data['parkingLocationType'].tolist()  # Парковка
        self.parkingtype = data['parkingType'].tolist()  # Типа парковки
        self.placescount = data['placesCount'].tolist()  # Колличество мест на парковке
        self.priceentry = data['priceEntry'].tolist()  # Стоимость въезда на парковку
        self.pricecurrency = data['priceCurrency'].tolist()  # Ставка за кв.м
        self.vattype = data['vatType'].tolist()  # Налог
        self.leasetype = data['leaseType'].tolist()  # Тип аренды
        self.minleaseterm = data['minLeaseTerm'].tolist()  # Минимальный срок ареды от
        self.hasgraceperiod = data['hasGracePeriod'].tolist()  # Арендные каникулы
        self.securitydeposit = data['securityDeposit'].tolist()  # Обеспечительный платёж
        self.prepaytype = data['prepayType'].tolist()


    def login(self):
        print('Start logging in')
        self.driver.get("https://www.cian.ru/#")
        self.driver.find_element_by_id('login-btn').click()

        time.sleep(1)

        login = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Email или ID']")
        login.clear()

        password = self.driver.find_element_by_xpath("//div[@id='login-popup']//input[@placeholder='Пароль']")
        password.clear()

        login.send_keys('****')
        password.send_keys('****')

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
            floorNumber = self.floornumber[i]
            floorCount = self.floorcount[i]
            ceilingHeight = self.ceilingheight[i]
            columnGrid = self.columngrid[i]
            floorMaterial = self.floormaterial[i]
            conditionType = self.conditiontype[i]
            gatesType = self.gatestype[i]
            waterPipesCount = self.waterpipescount[i]
            electricityPower = self.electricitypower[i]
            parkingLocationType = self.parkinglocationtype[i]
            parkingType = self.parkingtype[i]
            placesCount = self.placescount[i]
            priceEntry = self.priceentry[i]
            priceCurrency = self.pricecurrency[i]
            vatType = self.vattype[i]
            leaseType = self.leasetype[i]
            minLeaseTerm = self.minleaseterm[i]
            hasGracePeriod = self.hasgraceperiod[i]
            securityDeposit = self.securitydeposit[i]
            prepayType = self.prepaytype[i]

            print('Star updating object with id', obj_id)

            object_link = self.object_link.format(obj_id)
            self.driver.get(object_link)

            try:
                total_area_input = self.driver.find_element_by_xpath("//input[@name='totalArea']")
                total_area_input.clear()
                total_area_input.send_keys(totalArea)

                print('totalArea ', totalArea, 'send')

                time.sleep(3)

            except Exception as e:
                print('No totalArea', e)

            try:
                min_area_input = self.driver.find_element_by_xpath("//input[@name='minArea']")
                min_area_input.clear()
                min_area_input.send_keys(minArea)
                print('minArea ', minArea, 'send')
                time.sleep(3)

            except Exception as e:
                print('No minArea', e)

            try:
                floor_number_input = self.driver.find_element_by_xpath("//input[@name='floorNumber']")
                floor_number_input.clear()
                floor_number_input.send_keys(floorNumber)
                print('floorNumber ', floorNumber, 'send')
                time.sleep(3)

            except Exception as e:
                print('No floorNumber', e)

            try:
                floor_count_input = self.driver.find_element_by_xpath("//input[@name='floorsCount']")
                floor_count_input.clear()
                floor_count_input.send_keys(floorCount)
                print('floorCount ', floorCount, 'send')
                time.sleep(3)

            except Exception as e:
                print('No floorCount', e)

            try:
                ceiling_height_input = self.driver.find_element_by_xpath("//input[@name='building.ceilingHeight']")
                ceiling_height_input.clear()
                ceiling_height_input.send_keys(ceilingHeight)
                print('ceilingHeight ', ceilingHeight, 'send')

                time.sleep(3)

            except Exception as e:
                print('No ceilingHeight', e)

            try:
                column_grid_input = self.driver.find_element_by_xpath("//input[@name='columnGrid']")
                column_grid_input.clear()
                column_grid_input.send_keys(columnGrid)
                print('columnGrid', columnGrid, 'send')

                time.sleep(3)

            except Exception as  e:
                print('No columnGrid', e)

            try:
                floor_material_select_find = self.driver.find_elements_by_xpath(
                    "//button[@class='cui-button cui-button_look_gray']")
                floor_material_select_find[1].click()

                floor_material_select_from_list = self.driver.find_elements_by_xpath(
                    "//li[contains(@class, 'cui-dropdown__item')]")

                if 'полимерный' in floorMaterial:
                    floor_material_select_from_list[0].click()
                    print('floorMaterial', floorMaterial, 'clicked')
                elif 'бетон' in floorMaterial:
                    floor_material_select_from_list[1].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                elif 'линолеум' in floorMaterial:
                    floor_material_select_from_list[2].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                elif 'асфальт' in floorMaterial:
                    floor_material_select_from_list[3].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                elif 'плитка' in floorMaterial:
                    floor_material_select_from_list[4].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                elif 'наливной' in floorMaterial:
                    floor_material_select_from_list[5].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                elif 'железобетонный' in floorMaterial:
                    floor_material_select_from_list[6].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                elif 'дерево' in floorMaterial:
                    floor_material_select_from_list[7].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                elif 'ламинат' in floorMaterial:
                    floor_material_select_from_list[8].click()
                    print('floorMaterial ', floorMaterial, 'clicked')
                else:
                    print('No floorMaterial')

                time.sleep(3)

            except Exception as  e:
                print('Some floorMaterial Exception', e)

            try:
                condition_type_select_find = self.driver.find_elements_by_xpath(
                    "//button[@class='cui-button cui-button_look_gray']")
                condition_type_select_find[2].click()

                condition_type_select_from_list = self.driver.find_elements_by_xpath(
                    "//li[contains(@class, 'cui-dropdown__item')]")

                if 'Типовой ремонт' in conditionType:
                    condition_type_select_from_list[0].click()
                    print('conditionType', conditionType, 'clicked')
                elif 'Требуется капитальный ремонт' in conditionType:
                    condition_type_select_from_list[1].click()
                    print('conditionType ', conditionType, 'clicked')

                elif 'Требуется косметический ремонт' in conditionType:
                    condition_type_select_from_list[2].click()
                    print('conditionType ', conditionType, 'clicked')

                else:
                    print('No conditionType')

            except Exception as e:
                print('Some conditionType Exception', e)
            time.sleep(3)

            try:
                gates_type_select_find = self.driver.find_elements_by_xpath(
                    "//button[@class='cui-button cui-button_look_gray']")
                gates_type_select_find[3].click()

                gates_type_select_from_list = self.driver.find_elements_by_xpath(
                    "//li[contains(@class, 'cui-dropdown__item')]")

                if 'На пандусе' in gatesType:
                    gates_type_select_from_list[0].click()
                    print('gatesType ', gatesType, 'clicked')
                elif 'Докового типа' in gatesType:
                    gates_type_select_from_list[1].click()
                    print('gatesType ', gatesType, 'clicked')
                elif 'На нулевой отметке' in gatesType:
                    gates_type_select_from_list[2].click()
                    print('gatesType ', gatesType, 'clicked')
                else:
                    print('No gatesType')
                time.sleep(3)
            except Exception as e:
                print('Some gatesType Exception', e)

            try:
                water_pipes_count_select_find = self.driver.find_elements_by_xpath(
                    "//button[@class='cui-button cui-button_look_gray']")
                water_pipes_count_select_find[4].click()

                water_pipes_count_select_from_list = self.driver.find_elements_by_xpath(
                    "//li[contains(@class, 'cui-dropdown__item')]")

                if type(waterPipesCount) is str and 'нет' in waterPipesCount:
                    water_pipes_count_select_from_list[0].click()
                    print('waterPipesCount', waterPipesCount, 'clicked')
                elif 1 == waterPipesCount:
                    water_pipes_count_select_from_list[1].click()
                    print('waterPipesCount', waterPipesCount, 'clicked')
                elif 2 == waterPipesCount:
                    water_pipes_count_select_from_list[2].click()
                    print('waterPipesCount', waterPipesCount, 'clicked')
                elif 3 == waterPipesCount:
                    water_pipes_count_select_from_list[3].click()
                    print('waterPipesCount', waterPipesCount, 'clicked')
                elif 4 == waterPipesCount:
                    water_pipes_count_select_from_list[4].click()
                    print('waterPipesCount', waterPipesCount, 'clicked')
                else:
                    print('No waterPipesCount')
                time.sleep(3)
            except Exception:
                print('Some waterPipesCount Exception')

            try:
                electricity_power_input = self.driver.find_element_by_xpath("//input[@name='electricity.power']")
                electricity_power_input.clear()
                electricity_power_input.send_keys(electricityPower)
                print('electricityPower', electricityPower, 'send')

                time.sleep(3)

            except Exception as e:
                print('No electricityPower', e)

            try:
                parking_location_type_buttons_list = self.driver.find_elements_by_xpath(
                    "//div[@name='building.parking.locationType']//div[contains(@class, 'cui-switcher__part')]")

                if 'На территории объекта' in parkingLocationType:

                    parking_location_type_buttons_list[0].click()
                    print('parkingLocationType ', parkingLocationType, 'send')

                elif 'За территорией объекта' in parkingLocationType:

                    parking_location_type_buttons_list[1].click()
                    print('parkingLocationType ', parkingLocationType, 'send')

                else:
                    print('No parkingLocationType')

                time.sleep(3)

            except Exception as  e:
                print('Some parkingLocationType Expection', e)

            try:
                parking_purpose_type_buttons_list = self.driver.find_elements_by_xpath(
                    "//div[@name='building.parking.purposeType']//div[contains(@class, 'cui-switcher__part')]")

                if 'Для грузового транспорта' in parkingType:

                    parking_purpose_type_buttons_list[0].click()
                    print('parkingType ', parkingType, 'send')

                elif 'Для легковесного транспорта' in parkingType:

                    parking_purpose_type_buttons_list[1].click()
                    print('parkingType ', parkingType, 'send')

                else:
                    print('No parkingType')

                time.sleep(3)

            except Exception as  e:
                print('Some parkingType Expection', e)

            try:
                places_count_input = self.driver.find_element_by_xpath("//input[@name='building.parking.placesCount']")
                places_count_input.clear()
                places_count_input.send_keys(placesCount)
                print('placesCount ', placesCount, 'send')

                time.sleep(3)

            except Exception as e:
                print('No placesCount', e)

            try:
                price_entry_input = self.driver.find_element_by_xpath("//input[@name='building.parking.priceEntry']")
                price_entry_input.clear()
                price_entry_input.send_keys(priceEntry)
                print('priceEntry ', priceEntry, 'send')

                time.sleep(3)

            except Exception as  e:
                print('No priceEntry', e)

            try:
                price_currency_input = self.driver.find_element_by_xpath("//input[@name='bargainTerms.price']")
                price_currency_input.clear()
                price_currency_input.send_keys(priceCurrency)
                print('priceCurrency ', priceCurrency, 'send')
                time.sleep(3)

            except Exception as e:
                print('No priceCurrency', e)

            try:
                vat_type_select_find = self.driver.find_elements_by_xpath(
                    "//button[@class='cui-button cui-button_look_gray']")
                vat_type_select_find[7].click()

                vat_type_select_from_list = self.driver.find_elements_by_xpath(
                    "//li[contains(@class, 'cui-dropdown')]")
                # print(vatType, 'datatype', type(vatType))

                if vatType == 1:
                    vat_type_select_from_list[0].click()
                    print('vatType ', vatType, 'clicked')
                elif vatType == 2:
                    vat_type_select_from_list[1].click()
                    print('vatType ', vatType, 'clicked')
                elif vatType == 3:
                    vat_type_select_from_list[2].click()
                    print('vatType ', vatType, 'clicked')
                else:
                    print('No vatType')
                time.sleep(3)

            except Exception as e:
                print('Some vatType Exception', e)

            try:
                min_lease_term_input = self.driver.find_element_by_xpath("//input[@name='bargainTerms.minLeaseTerm']")
                min_lease_term_input.clear()
                min_lease_term_input.send_keys(minLeaseTerm)
                print('minLeaseTerm ', minLeaseTerm, 'send')

                time.sleep(3)

            except Exception:
                print('No minLeaseTerm')

            try:
                lease_type_type_buttons_list = self.driver.find_elements_by_xpath(
                    "//div[@name='bargainTerms.leaseType']//div[contains(@class, 'cui-switcher__part')]")

                # print(lease_type_type_buttons_list)

                if 'Прямая аренда' in leaseType:

                    lease_type_type_buttons_list[0].click()
                    print('leaseType ', leaseType, 'send')

                elif 'Субаренда' in leaseType:

                    lease_type_type_buttons_list[1].click()
                    print('leaseType ', leaseType, 'send')

                else:
                    print('No leaseType')

            except Exception as e:
                print('Some leaseType Expection', e)

            try:
                security_deposit_input = self.driver.find_element_by_xpath(
                    "//input[@name='bargainTerms.securityDeposit']")
                security_deposit_input.clear()
                security_deposit_input.send_keys(securityDeposit)
                print('securityDeposit ', securityDeposit, 'send')

                time.sleep(3)

            except Exception as e:
                print('No securityDeposit', e)

            try:
                # print('prepayType == ', prepayType)
                prepay_type_select_find = self.driver.find_elements_by_xpath(
                    "//button[@class='cui-button cui-button_look_gray']")
                prepay_type_select_find[8].click()

                time.sleep(2)

                if '10 месяцев' or '11 месяцев' or '1 год' in prepayType:
                    scroll = self.driver.find_element_by_xpath(
                        "//ul[@class='cui-dropdown__menu']")
                    hover = ActionChains(self.driver).move_to_element(scroll)
                    hover.perform()
                    time.sleep(3)

                prepay_type_select_from_list = self.driver.find_elements_by_xpath(
                    "//li[contains(@class, 'cui-dropdown__item')]")
                # prepay_type_select_from_list[10].click()
                print('11 месяцев' in prepayType)

                if '11 месяцев' in prepayType:
                    prepay_type_select_from_list[10].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '1 месяц' in prepayType:
                    prepay_type_select_from_list[0].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '2 месяца' in prepayType:
                    prepay_type_select_from_list[1].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '3 месяца' in prepayType:
                    prepay_type_select_from_list[2].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '4 месяца' in prepayType:
                    prepay_type_select_from_list[3].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '5 месяцев' in prepayType:
                    prepay_type_select_from_list[4].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '6 месяцев' in prepayType:
                    prepay_type_select_from_list[5].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '7 месяцев' in prepayType:
                    prepay_type_select_from_list[6].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '8 месяцев' in prepayType:
                    prepay_type_select_from_list[7].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '9 месяцев' in prepayType:
                    prepay_type_select_from_list[8].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '10 месяцев' in prepayType:
                    prepay_type_select_from_list[9].click()
                    print('prepayType ', prepayType, 'clicked')
                elif '1 год' in prepayType:
                    prepay_type_select_from_list[11].click()
                    print('prepayType ', prepayType, 'clicked')
            except Exception as e:
                print('No prepayType', e)

            time.sleep(3)

            try:
                grace_period_type_buttons_list = self.driver.find_elements_by_xpath(
                    "//div[@name='hasGracePeriod']//div[contains(@class, 'cui-switcher__part')]")
                # print(grace_period_type_buttons_list)

                if 'Да' in hasGracePeriod:

                    grace_period_type_buttons_list[0].click()
                    print('hasGracePeriod ', hasGracePeriod, 'send')

                elif 'Нет' in hasGracePeriod:

                    grace_period_type_buttons_list[1].click()
                    print('hasGracePeriod ', hasGracePeriod, 'send')

                else:
                    print('No hasGracePeriod')

            except Exception as  e:
                print('Some hasGracePeriod Expection', e)

        print('Object', obj_id, ' updated')
        time.sleep(5)

    # def pushUpdate(self):
    #
    #     pushRequest = self.driver.find_element_by_xpath('//button[@button-type="submit"]')
    #     pushRequest.click()


class Interface(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QWidget.__init__(self)

        self.statusBar()

        self.setGeometry(600, 300, 390, 250)
        self.setWindowTitle('Objects Update')
        self.setWindowIcon(QIcon('colliers.png'))
        self.oImage = QImage("/home/EU/yury.festa/PycharmProjects/COLLIERS/apps/background.png")
        self.sImage = self.oImage.scaled(QSize(390, 250))  # resize Image to widgets size
        self.palette = QPalette()
        self.palette.setBrush(10, QBrush(self.sImage))  # 10 = Windowrole
        self.setPalette(self.palette)

        self.UpdateCian_btn()
        self.UpdateAvito_btn()

        # self.setStatusBar(self.statusBar)

        # self.statusBar.show()

        self.show()

    def UpdateCian_btn(self):
        btn = QPushButton('Update Cian', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(self.openFileNameDialog_for_cian)


    def UpdateAvito_btn(self):
        btn = QPushButton('Update Avito', self)
        btn.resize(btn.sizeHint())
        btn.move(240, 50)
        btn.clicked.connect(self.openFileNameDialog_for_avito)

    def openFileNameDialog_for_cian(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)

        if fileName:
            print(fileName)
            process = UpdateBase()
            process.get_data(fileName)
            process.login()
            process.update(QMainWindow)
            # process.pushUpdate()

        return fileName

    def openFileNameDialog_for_avito(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)

        # data = pd.read_excel(fileName)

        if fileName:
            print(fileName)

        return fileName


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())
