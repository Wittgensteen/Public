from tkinter import *
import psycopg2 as pg
from tkinter import messagebox
import os
import pandas


class App(object):
    def __init__(self, window):
        window.wm_title("Popular macroeconomic indicators from WB")
        self.current_row = 0
        self.indicator_name_label = Label(window, text='Insert indicators')
        self.indicator_name_label.grid(row=self.current_row, column=0)
        self.indicator_name_text = StringVar()
        self.indicator_name_entry = Entry(window, textvariable=self.indicator_name_text)
        self.indicator_name_entry.grid(row=self.current_row, column=1)
        self.current_row += 1

        self.country_name_label = Label(window, text='Insert country name')
        self.country_name_label.grid(row=self.current_row, column=0)
        self.country_name_text = StringVar()
        self.country_name_entry = Entry(window, textvariable=self.country_name_text)
        self.country_name_entry.grid(row=self.current_row, column=1)
        self.current_row += 1

        self.query_button = Button(window, text="Send query")
        self.query_button.configure(command=self.sendquery)
        self.query_button.grid(row=self.current_row, column=0, columnspan=2)
        self.current_row += 1

        # Line to separate panels
        canvas = Canvas(master=window, width=500, height=40)
        canvas.create_line(0, 20, 500, 20, fill="black")
        canvas.grid(row=self.current_row, column=0, columnspan=2)
        self.current_row += 1

        # Label for Entry box
        self.save_label = Label(window, text="Save Location: ")
        self.save_label.grid(row=self.current_row, column=0, columnspan=2)
        self.current_row += 1

        # Entry box for save location
        self.save_text = StringVar()
        self.save_entry = Entry(window, textvariable=self.save_text)
        self.save_entry.grid(row=self.current_row, column=0, columnspan=2)
        self.current_row += 1

        self.save_button = Button(window, text="Save Data")
        self.save_button.configure(command=self.save_to_csv)
        self.save_button.grid(row=self.current_row, column=0, columnspan=2)
        self.current_row += 1

    def sendquery(self):
        indicator_name_text = self.indicator_name_text.get()
        country_name_text = self.country_name_text.get()
        conn = pg.connect('dbname=test host=localhost user=postgres password=ffgtr64')
        sql = "SELECT country_name, yr2000, yr2001, yr2002,yr2003, yr2004, yr2005, yr2006, yr2007," \
              " yr2008, yr2009,yr2010, yr2011,yr2012, yr2013, yr2014, yr2015 from pi WHERE" \
              " series_name='%s' AND country_name IN ('%s');" % (indicator_name_text, country_name_text)
        with conn:
            cur = conn.cursor()
            cur.execute(sql)
            print(indicator_name_text, country_name_text)
            row = cur.fetchall()
            self.df = cur.fetchall()
            print(row)
            # print('heeeey, im here now')
            conn.commit()
            cur.close()
            # print('heeeey, im here now')

    def save_to_csv(self):
        self.save_loc = self.save_text.get()
        self.save_dir = os.sep.join(self.save_loc.split(os.sep)[:-1])
        if os.path.isdir(self.save_dir):

            # Verify that the filename is more than just '.csv'
            if len(self.save_loc.split(os.sep)[-1]) < 5:
                messagebox.showinfo('Save Error', 'Error: Path should end in filename.csv')
            elif self.save_loc.split(os.sep)[-1][-4:] != '.csv':
                messagebox.showinfo('Save Error', 'Error: File should end in filename.csv')
            else:
                self.df.to_csv(self.save_loc)
                print('and finally we are here')
        else:
            messagebox.showinfo('Save Error', 'Error: File directory does not exist')


def main():
    window = Tk()
    start = App(window)
    window.mainloop()


if __name__ == "__main__":
    main()
