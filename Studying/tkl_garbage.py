from tkinter import *
import psycopg2 as pg
from tkinter import ttk
import pyexcel

indicators = ['Population, total', 'Population growth (annual %)', 'GDP (current US$)',
              'GNI, Atlas method (current US$)',
              'Energy use (kg of oil equivalent per capita)', 'GDP growth (annual %)', 'Surface area (sq. km)',
              'Inflation, consumer prices (annual %)', 'Agriculture, value added (% of GDP)',
              'Industry, value added (% of GDP)', 'Services, etc., value added (% of GDP)',
              'Exports of goods and services (% of GDP)', 'Inflation, consumer prices (annual %)']
countries = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain',
             'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
             'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei Darussalam',
             'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands',
             'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros',
             'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao',
             'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
             'Egypt, Arab Rep.', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
             'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia, The',
             'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala',
             'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong SAR, China', 'Hungary', 'Iceland',
             'India', 'Indonesia', 'Iran, Islamic Rep.', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy',
             'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, Dem. People’s Rep.',
             'Korea, Rep.', 'Kosovo', 'Kuwait', 'Kyrgyz Republic', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho',
             'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Macedonia, FYR',
             'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
             'Mauritius', 'Mexico', 'Micronesia, Fed. Sts.', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
             'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
             'Nicaragua', 'Niger', 'Nigeria', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
             'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico',
             'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Samoa', 'San Marino', 'Sao Tome and Principe',
             'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
             'Sint Maarten (Dutch part)', 'Slovak Republic', 'Slovenia', 'Solomon Islands', 'Somalia',
             'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts and Nevis', 'St. Lucia',
             'St. Martin (French part)', 'St. Vincent and the Grenadines', 'Sudan', 'Suriname', 'Swaziland',
             'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste',
             'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands',
             'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
             'Uzbekistan', 'Vanuatu', 'Venezuela, RB', 'Vietnam', 'Virgin Islands (U.S.)', 'West Bank and Gaza',
             'Yemen, Rep.', 'Zambia', 'Zimbabwe']

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

constr1type = ['Количество введенных зданий', 'Общий строительный объем зданий', 'Общая площадь зданий']
constr1purp = ['Всего', 'Жилого Назначения', 'Нежилого Назначения']
constr2type = ['Количество введенных нежилых зданий', 'Строительный объем нежилых зданий', 'Общая площадь зданий']
constr2purp = ['Всего', 'Промышленные', 'Сельскохозяйственные', 'Коммерческие', 'Административные', 'Учебные',
               'Системы  здравоохранения', 'Другие']
russia_region = ['Российская Федерация', 'Центральный федеральный округ', 'Северо-Западный федеральный округ',
                 'Южный федеральный округ', 'Северо-Кавказский федеральный округ', 'Приволжский федеральный округ',
                 'Уральский федеральный округ', 'Сибирский федеральный округ']

info_cpmr = ['to end of last month', 'to last year december']

backcolor = '#%02x%02x%02x' % (0, 147, 208)
redcolor = '#%02x%02x%02x' % (238, 49, 36)
saveclr = '#%02x%02x%02x' % (255, 196, 37)
paleblue = '#%02x%02x%02x' % (223, 239, 249)


def clear():
    list = window.grid_slaves()
    for l in list:
        l.destroy()


def Q1():
    class app(object):

        def __init__(self, window):
            clear()
            window.wm_title("World Bank data")  # Set the window title
            self.background_image = PhotoImage(file='back.gif')
            self.background_label = Label(window, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            # Logo for fun
            self.log = PhotoImage(file='logo.gif')
            self.logo = Label(window, image=self.log)
            self.logo.grid(row=0, column=0, columnspan=1)
            self.log2 = PhotoImage(file='logo2.gif')
            self.logo2 = Label(window, image=self.log2)
            self.logo2.grid(row=0, column=1, columnspan=1)

            self.current_row = 0
            self.indicator_name_label = Label(window, text='Select indicator', bg=backcolor, width=18, font='Arial 9')
            self.indicator_name_label.grid(row=1, column=0, columnspan=1)
            self.indicator_name_text = StringVar()
            self.current_row += 1

            self.country_name_label = Label(window, text='Select country name', bg=backcolor, width=18, font='Arial 9')
            self.country_name_label.grid(row=2, column=0)
            self.country_name_text = StringVar()
            self.current_row += 1
            # self.query_button = Button(window, text ="Send query")
            # self.query_button.configure(command=self.sendquery)
            # self.query_button.grid (row=self.current_row, column=0, columnspan=2)
            self.current_row += 1

            # Line to separate panels
            # canvas = Canvas(master=window, width=500, height=40)
            # canvas.create_line(0, 20, 1000, 20, fill="black")
            # canvas.grid(row=self.current_row, column=0, columnspan=2)
            self.current_row += 1

            # Label for Entry box
            self.save_label = Label(window, text="Save as: ", bg=backcolor, width=18, font='Arial 9')
            self.save_label.grid(row=3, column=0, columnspan=1)
            self.current_row += 1

            # Label for Version Name
            self.save_label = Label(window, text="Version 0.1", bg=redcolor, width=18, font='Arial 9')
            self.save_label.grid(row=5, column=0, columnspan=1)
            self.current_row += 1

            # Entry box for save location
            self.save_text = StringVar()
            self.save_entry = Entry(window, textvariable=self.save_text, width=37)
            self.save_entry.grid(row=3, column=1, columnspan=1)
            self.current_row += 1

            self.save_button = Button(window, text="Save selected data", bg=saveclr, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery)
            self.save_button.grid(row=5, column=1, columnspan=1)
            self.current_row += 1

            # Entry indicator from box
            self.indicator_name_textbox = StringVar()
            self.combo_ind = ttk.Combobox(window, textvariable=self.indicator_name_textbox, values=indicators, width=34)
            self.combo_ind.grid(row=1, column=1, columnspan=1)

            #  Entry country from box

            self.country_name_textbox = StringVar()
            self.combo_cou = ttk.Combobox(window, textvariable=self.country_name_textbox, values=countries, width=34)
            self.combo_cou.grid(row=2, column=1, columnspan=1)

            # Label for Save All
            self.save_label = Label(window, text="Save all Data", bg=paleblue, width=18, font='Arial 9')
            self.save_label.grid(row=6, column=0, columnspan=1)
            self.current_row += 1

            # Button for Save All
            self.save_button = Button(window, text="Save all Data", bg=paleblue, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery1)
            self.save_button.grid(row=6, column=1, columnspan=1)

            # empty rows
            # self.empty_label = Label(window, text='', bg=paleblue, width=18, font='Arial 9')
            # self.empty_label.grid(row=7, column=1, columnspan=5, sticky=W+E)

        def sendquery(self):
            indicator_name_text = self.indicator_name_textbox.get()  # ЗАМЕНА
            country_name_text = self.country_name_textbox.get()  # ЗАМЕНА

            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT country_name, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 
                     FROM pi
                     WHERE series_name='%s' AND country_name IN ('%s');""" % (indicator_name_text, country_name_text)
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows1 = cur.fetchall()
                tv1 = ttk.Treeview(window, height=10)
                tv1['columns'] = (
                'country', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016')
                tv1.heading("#0", text='', anchor='w')
                tv1.column("#0", stretch=NO, width=5, anchor="w")
                tv1.heading('country', text='country')
                tv1.heading('2007', text='2007')
                tv1.heading('2008', text='2008')
                tv1.heading('2009', text='2009')
                tv1.heading('2010', text='2010')
                tv1.heading('2011', text='2011')
                tv1.heading('2012', text='2012')
                tv1.heading('2013', text='2013')
                tv1.heading('2014', text='2014')
                tv1.heading('2015', text='2015')
                tv1.column('country', anchor='center', width=60)
                tv1.column('2007', anchor='center', width=55)
                tv1.column('2008', anchor='center', width=55)
                tv1.column('2009', anchor='center', width=55)
                tv1.column('2010', anchor='center', width=55)
                tv1.column('2011', anchor='center', width=55)
                tv1.column('2012', anchor='center', width=55)
                tv1.column('2013', anchor='center', width=55)
                tv1.column('2014', anchor='center', width=55)
                tv1.column('2015', anchor='center', width=55)
                tv1.column('2016', anchor='center', width=55)
                tv1.grid(row=0, column=3, columnspan=1, rowspan=7)
                rows11 = list(rows1)
                tv1.insert("", "end", values=rows11[0, 1, 2])

                # print(indicator_name_text, country_name_text)
                # print(colnames)
                # print('____________________________')
                rows1.insert(0, colnames)
                # print(rows1)
                # pyexcel.save_as(array=rows, dest_file_name="testsave.xls")
                filename = self.save_text.get()
                pyexcel.save_as(array=rows1, dest_file_name=filename)

        def sendquery1(self):
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT country_name, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 
                     FROM pi;"""
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows11 = cur.fetchall()
                print(colnames)
                print('____________________________')
                rows11.insert(0, colnames)
                print(rows11)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows11, dest_file_name=filename)

    app(window)


def Q2():
    class app2(object):

        def __init__(self, window):
            clear()
            window.wm_title("Rosstat data")  # Set the window title
            self.background_image = PhotoImage(file='back.gif')
            self.background_label = Label(window, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            # Logo for fun
            self.log = PhotoImage(file='logo.gif')
            self.logo = Label(window, image=self.log)
            self.logo.grid(row=0, column=0)
            self.log2 = PhotoImage(file='logo2.gif')
            self.logo2 = Label(window, image=self.log2)
            self.logo2.grid(row=0, column=1)
            # self.logo.pack(side=RIGHT,padx=5, pady=5)
            window.wm_title("Rosstat data")  # Set the window title
            self.current_row = 0
            self.month_name_label = Label(window, text='Select Month', bg=backcolor, width=18, font='Arial 9')
            self.month_name_label.grid(row=1, column=0)
            self.month_name_text = StringVar()
            self.current_row += 1
            self.period_name_label = Label(window, text='Select period', bg=backcolor, width=18, font='Arial 9')
            self.period_name_label.grid(row=2, column=0)
            self.period_name_text = StringVar()
            self.current_row += 1
            self.current_row += 1
            self.current_row += 1
            # Label for Entry box
            self.save_label = Label(window, text="Save as: ", bg=backcolor, width=18, font='Arial 9')
            self.save_label.grid(row=3, column=0, columnspan=1)
            self.current_row += 1
            # Label for Version Name
            self.save_label = Label(window, text="Version 0.1", bg=redcolor, width=18, font='Arial 9')
            self.save_label.grid(row=5, column=0, columnspan=1)
            self.current_row += 1
            # Entry box for save location
            self.save_text = StringVar()
            self.save_entry = Entry(window, textvariable=self.save_text, width=37)
            self.save_entry.grid(row=3, column=1, columnspan=1)
            self.current_row += 1
            self.save_button = Button(window, text="Save Data", bg=saveclr, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery)
            self.save_button.grid(row=5, column=1, columnspan=1)
            self.current_row += 1
            # Entry indicator from box
            self.month_name_textbox = StringVar()
            self.combo_ind = ttk.Combobox(window, textvariable=self.month_name_textbox, values=months, width=34)
            self.combo_ind.grid(row=1, column=1, columnspan=1)
            #  Entry country from box
            self.period_name_textbox = StringVar()
            self.combo_cou = ttk.Combobox(window, textvariable=self.period_name_textbox, values=info_cpmr, width=34)
            self.combo_cou.grid(row=2, column=1, columnspan=1)

            # Label for Version Name
            self.save_label = Label(window, text="Сохранить всё", bg=paleblue, width=18, font='Arial 9')
            self.save_label.grid(row=6, column=0, columnspan=1)
            self.current_row += 1

            self.save_button = Button(window, text="Сохранить все данные", bg=paleblue, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery1)
            self.save_button.grid(row=6, column=1, columnspan=1)

        def sendquery(self):
            month_name_text = self.month_name_textbox.get()  # ЗАМЕНА
            period_name_text = self.period_name_textbox.get()  # ЗАМЕНА
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT month, info, indicator, yr1991,yr1992,yr1993,yr1994,yr1995,yr1996,
                     yr1997, yr1998, yr1999, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016, yr2017
                     FROM consume_price_by_months_russia
                     WHERE month='%s' AND info IN ('%s');""" % (month_name_text, period_name_text)
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows2 = cur.fetchall()
                print(month_name_text, period_name_text)
                print(colnames)
                print('____________________________')
                rows2.insert(0, colnames)
                print(rows2)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows2, dest_file_name=filename)

        def sendquery1(self):
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT month, info, indicator, yr1991,yr1992,yr1993,yr1994,yr1995,yr1996,
                     yr1997, yr1998, yr1999, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016, yr2017
                     FROM consume_price_by_months_russia ;"""
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows2 = cur.fetchall()
                print(colnames)
                print('____________________________')
                rows2.insert(0, colnames)
                print(rows2)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows2, dest_file_name=filename)

    app2(window)


def Q3():
    class app3(object):

        def __init__(self, window):
            clear()
            window.wm_title("Ввод зданий жилого и нежилого назначения")  # Set the window title
            self.background_image = PhotoImage(file='back.gif')
            self.background_label = Label(window, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            # Logo for fun
            self.log = PhotoImage(file='logo.gif')
            self.logo = Label(window, image=self.log)
            self.logo.grid(row=0, column=0)
            self.log2 = PhotoImage(file='logo2.gif')
            self.logo2 = Label(window, image=self.log2)
            self.logo2.grid(row=0, column=1)
            # self.logo.pack(side=RIGHT,padx=5, pady=5)

            self.current_row = 0
            self.month_name_label = Label(window, text='Выберете данные', bg=backcolor, width=18, font='Arial 9')
            self.month_name_label.grid(row=1, column=0)
            self.month_name_text = StringVar()
            self.current_row += 1
            self.period_name_label = Label(window, text='Выберите назначение', bg=backcolor, width=18, font='Arial 9')
            self.period_name_label.grid(row=2, column=0)
            self.period_name_text = StringVar()
            self.current_row += 1
            self.current_row += 1
            self.current_row += 1
            # Label for Entry box
            self.save_label = Label(window, text="Save as: ", bg=backcolor, width=18, font='Arial 9')
            self.save_label.grid(row=3, column=0, columnspan=1)
            self.current_row += 1
            # Label for Version Name
            self.save_label = Label(window, text="Version 0.1", bg=redcolor, width=18, font='Arial 9')
            self.save_label.grid(row=5, column=0, columnspan=1)
            self.current_row += 1
            # Entry box for save location
            self.save_text = StringVar()
            self.save_entry = Entry(window, textvariable=self.save_text, width=37)
            self.save_entry.grid(row=3, column=1, columnspan=1)
            self.current_row += 1
            self.save_button = Button(window, text="Save Data", bg=saveclr, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery)
            self.save_button.grid(row=5, column=1, columnspan=1)
            self.current_row += 1
            # Entry indicator from box
            self.infoconstr1_name_textbox = StringVar()
            self.combo_ind = ttk.Combobox(window, textvariable=self.infoconstr1_name_textbox, values=constr1type,
                                          width=34)
            self.combo_ind.grid(row=1, column=1, columnspan=1)
            #  Entry country from box
            self.addinfoconstr1_name_textbox = StringVar()
            self.combo_cou = ttk.Combobox(window, textvariable=self.addinfoconstr1_name_textbox, values=constr1purp,
                                          width=34)
            self.combo_cou.grid(row=2, column=1, columnspan=1)

            # Label for Version Name
            self.save_label = Label(window, text="Сохранить всё", bg=paleblue, width=18, font='Arial 9')
            self.save_label.grid(row=6, column=0, columnspan=1)
            self.current_row += 1

            self.save_button = Button(window, text="Сохранить все данные", bg=paleblue, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery1)
            self.save_button.grid(row=6, column=1, columnspan=1)

        def sendquery(self):
            infoconstr1_name_text = self.infoconstr1_name_textbox.get()  # ЗАМЕНА
            addinfoconstr1_name_text = self.addinfoconstr1_name_textbox.get()  # ЗАМЕНА
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT info, add_info, index, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016, yr2017
                     FROM construction_1
                     WHERE info='%s' AND add_info IN ('%s');""" % (infoconstr1_name_text, addinfoconstr1_name_text)
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows3 = cur.fetchall()
                print(infoconstr1_name_text, addinfoconstr1_name_text)
                print(colnames)
                print('____________________________')
                rows3.insert(0, colnames)
                print(rows3)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows3, dest_file_name=filename)

        def sendquery1(self):
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT info, add_info, index, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016, yr2017
                     FROM construction_1 ;"""
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows3 = cur.fetchall()
                print(colnames)
                print('____________________________')
                rows3.insert(0, colnames)
                print(rows3)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows3, dest_file_name=filename)

    app3(window)


def Q4():
    class app4(object):

        def __init__(self, window):
            clear()
            window.wm_title("Ввод зданий жилого и нежилого назначения")  # Set the window title
            self.background_image = PhotoImage(file='back.gif')
            self.background_label = Label(window, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            # Logo for fun
            self.log = PhotoImage(file='logo.gif')
            self.logo = Label(window, image=self.log)
            self.logo.grid(row=0, column=0)
            self.log2 = PhotoImage(file='logo2.gif')
            self.logo2 = Label(window, image=self.log2)
            self.logo2.grid(row=0, column=1)
            # self.logo.pack(side=RIGHT,padx=5, pady=5)

            self.current_row = 0
            self.month_name_label = Label(window, text='Выберете данные', bg=backcolor, width=18, font='Arial 9')
            self.month_name_label.grid(row=1, column=0)
            self.month_name_text = StringVar()
            self.current_row += 1
            self.period_name_label = Label(window, text='Выберите назначение', bg=backcolor, width=18, font='Arial 9')
            self.period_name_label.grid(row=2, column=0)
            self.period_name_text = StringVar()
            self.current_row += 1
            self.current_row += 1
            self.current_row += 1
            # Label for Entry box
            self.save_label = Label(window, text="Save as: ", bg=backcolor, width=18, font='Arial 9')
            self.save_label.grid(row=3, column=0, columnspan=1)
            self.current_row += 1
            # Label for Version Name
            self.save_label = Label(window, text="Version 0.1", bg=redcolor, width=18, font='Arial 9')
            self.save_label.grid(row=5, column=0, columnspan=1)
            self.current_row += 1
            # Entry box for save location
            self.save_text = StringVar()
            self.save_entry = Entry(window, textvariable=self.save_text, width=37)
            self.save_entry.grid(row=3, column=1, columnspan=1)
            self.current_row += 1
            self.save_button = Button(window, text="Save Data", bg=saveclr, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery)
            self.save_button.grid(row=5, column=1, columnspan=1)
            self.current_row += 1
            # Entry indicator from box
            self.infoconstr2_name_textbox = StringVar()
            self.combo_ind = ttk.Combobox(window, textvariable=self.infoconstr2_name_textbox, values=constr2type,
                                          width=34)
            self.combo_ind.grid(row=1, column=1, columnspan=1)
            #  Entry country from box
            self.addinfoconstr2_name_textbox = StringVar()
            self.combo_cou = ttk.Combobox(window, textvariable=self.addinfoconstr2_name_textbox, values=constr2purp,
                                          width=34)
            self.combo_cou.grid(row=2, column=1, columnspan=1)

            # Label for Version Name
            self.save_label = Label(window, text="Сохранить всё", bg=paleblue, width=18, font='Arial 9')
            self.save_label.grid(row=6, column=0, columnspan=1)
            self.current_row += 1

            self.save_button = Button(window, text="Сохранить все данные", bg=paleblue, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery1)
            self.save_button.grid(row=6, column=1, columnspan=1)

        def sendquery(self):
            infoconstr2_name_text = self.infoconstr2_name_textbox.get()  # ЗАМЕНА
            addinfoconstr2_name_text = self.addinfoconstr2_name_textbox.get()  # ЗАМЕНА
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT info, add_info, index, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016, yr2017
                     FROM construction_nez
                     WHERE info='%s' AND add_info IN ('%s');""" % (infoconstr2_name_text, addinfoconstr2_name_text)
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows4 = cur.fetchall()
                print(infoconstr2_name_text, addinfoconstr2_name_text)
                print(colnames)
                print('____________________________')
                rows4.insert(0, colnames)
                print(rows4)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows4, dest_file_name=filename)

        def sendquery1(self):
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT info, add_info, index, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016, yr2017
                     FROM construction_nez;"""
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows4 = cur.fetchall()
                print(colnames)
                print('____________________________')
                rows4.insert(0, colnames)
                print(rows4)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows4, dest_file_name=filename)

    app4(window)


def Q5():
    class app5(object):

        def __init__(self, window):
            clear()
            window.wm_title("Оборот розничной торговли по субъектам РФ")  # Set the window title
            self.background_image = PhotoImage(file='back.gif')
            self.background_label = Label(window, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            # Logo for fun
            self.log = PhotoImage(file='logo.gif')
            self.logo = Label(window, image=self.log)
            self.logo.grid(row=0, column=0)
            self.log2 = PhotoImage(file='logo2.gif')
            self.logo2 = Label(window, image=self.log2)
            self.logo2.grid(row=0, column=1)
            # self.logo.pack(side=RIGHT,padx=5, pady=5)

            self.current_row = 0
            self.month_name_label = Label(window, text='Выберете округ', bg=backcolor, width=18, font='Arial 9')
            self.month_name_label.grid(row=1, column=0)
            self.month_name_text = StringVar()
            self.current_row += 1
            # self.period_name_label = Label(window, text='Выберите субъект', bg=backcolor, width=18, font='Arial 9')
            # self.period_name_label.grid(row=2, column=0)
            # self.period_name_text = StringVar()
            self.current_row += 1
            self.current_row += 1
            self.current_row += 1
            # Label for Entry box
            self.save_label = Label(window, text="Save as: ", bg=backcolor, width=18, font='Arial 9')
            self.save_label.grid(row=3, column=0, columnspan=1)
            self.current_row += 1
            # Label for Version Name
            self.save_label = Label(window, text="Version 0.1", bg=redcolor, width=18, font='Arial 9')
            self.save_label.grid(row=5, column=0, columnspan=1)
            self.current_row += 1
            # Entry box for save location
            self.save_text = StringVar()
            self.save_entry = Entry(window, textvariable=self.save_text, width=37)
            self.save_entry.grid(row=3, column=1, columnspan=1)
            self.current_row += 1
            self.save_button = Button(window, text="Save Data", bg=saveclr, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery)
            self.save_button.grid(row=5, column=1, columnspan=1)
            self.current_row += 1
            # Entry indicator from box
            self.region_name_textbox = StringVar()
            self.combo_ind = ttk.Combobox(window, textvariable=self.region_name_textbox, values=russia_region, width=34)
            self.combo_ind.grid(row=1, column=1, columnspan=1)
            #  Entry country from box
            # self.addinfoconstr2_name_textbox = StringVar()
            # self.combo_cou = ttk.Combobox(window, textvariable=self.addinfoconstr2_name_textbox, values=constr2purp, width=34)
            # self.combo_cou.grid(row=2, column=1, columnspan=1)

            # Label for Version Name
            self.save_label = Label(window, text="Сохранить всё", bg=paleblue, width=18, font='Arial 9')
            self.save_label.grid(row=6, column=0, columnspan=1)
            self.current_row += 1

            self.save_button = Button(window, text="Сохранить все данные", bg=paleblue, width=31, font='Arial 9')
            self.save_button.configure(command=self.sendquery1)
            self.save_button.grid(row=6, column=1, columnspan=1)

        def sendquery(self):
            region_name_text = self.region_name_textbox.get()  # ЗАМЕНА
            # addinfoconstr2_name_text = self.addinfoconstr2_name_textbox.get()  # ЗАМЕНА
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT region, info, index, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016
                     FROM oborot_rozn_torg
                     WHERE region='%s' ;""" % (region_name_text)
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows5 = cur.fetchall()
                print(region_name_text)
                print(colnames)
                print('____________________________')
                rows5.insert(0, colnames)
                print(rows5)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows5, dest_file_name=filename)

        def sendquery1(self):
            conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
            query = """SELECT region, info, index, yr2000, yr2001, yr2002, yr2003, yr2004, yr2005, yr2006, yr2007, 
                     yr2008, yr2009, yr2010, yr2011, yr2012, yr2013, yr2014, yr2015 , yr2016
                     FROM oborot_rozn_torg ;"""
            with conn:
                cur = conn.cursor()
                cur.execute(query)
                colnames = [column[0] for column in cur.description]
                rows5 = cur.fetchall()
                print(colnames)
                print('____________________________')
                rows5.insert(0, colnames)
                print(rows5)
                filename = self.save_text.get()
                pyexcel.save_as(array=rows5, dest_file_name=filename)

    app5(window)


window = Tk()
window.wm_title("Colliers International Data Base")  # Set the window title
window.geometry('800x600')
back_image = PhotoImage(file='back.gif')
back_label = Label(window, image=back_image)
back_label.place(x=0, y=0, relwidth=1, relheight=1)
main_logo = PhotoImage(file='logo_main.gif')
main_logo_label = Label(window, image=main_logo)
main_logo_label.place(x=400, y=300, anchor='center')

m = Menu(window)  # создание полоски меню
window.config(menu=m)

world_menu = Menu(m)  # создание пункта меню
m.add_cascade(label="Данные World Bank", menu=world_menu)
world_menu.add_command(label="World Bank macro indicators", command=Q1)
# world_menu.add_command(label='Consumer price indices for goods and services in Russia', command=Q2)

russia_menu = Menu(m)
m.add_cascade(label="Данные Росстат", menu=russia_menu)
# russia_menu.add_command(label="World Bank macro indicators", command=Q1)
russia_menu.add_command(label='Индекс потребительских цен на товары и услуги', command=Q2)
russia_menu.add_command(label='Оборот розничной торговли по субъектам РФ', command=Q5)

russia_menu_constr = Menu(russia_menu)  # создание вложенного меню
russia_menu.add_cascade(label='Строительство', menu=russia_menu_constr)
russia_menu_constr.add_command(label='Ввод зданий жилого и нежилого назначения', command=Q3)
russia_menu_constr.add_command(label='Ввод зданий нежилого назначения по типам ', command=Q4)
sm = Menu(m)
window.mainloop()
