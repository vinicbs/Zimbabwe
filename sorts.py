import random
import time
from random import randint
from tkinter import *
from xml.dom import minidom

country_by_name = None
wht_return = 0
field = 8730
record = 1746

class MyDialog:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Country name").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global country_by_name
        country_by_name = self.e.get()

        self.top.destroy()


class WorldData:
    def __init__(self, country_name, year, gender, life_expectancy):
        self.country_name = country_name
        self.year = year
        self.gender = gender
        self.life_expectancy = life_expectancy

    def parse_list_name(self, i):
        if i == 174:
            print("Lista 10% carregada.")
        if i == 436:
            print("Lista 25% carregada.")
        if i == 872:
            print("Lista 50% carregada.")
        if i == 1310:
            print("Lista 75% carregada.")

        i = i * 5
        country_name = xmldoc.getElementsByTagName("field")[i].firstChild.data
        return country_name

    def parse_list_year(self, i):
        i = (i * 5) + 1
        year = xmldoc.getElementsByTagName("field")[i].firstChild.data
        return year

    def parse_list_gender(self, i):
        i = (i * 5) + 2
        gender = xmldoc.getElementsByTagName("field")[i].firstChild.data
        return gender

    def parse_list_lifeEx(self, i):
        i = (i * 5) + 3
        life_expectancy = xmldoc.getElementsByTagName("field")[i].firstChild.data
        return life_expectancy

    def __getitem__(self, key1):
        global wht_return
        if wht_return == 0:
            return self.country_name
        if wht_return == 1:
            return self.year
        if wht_return == 2:
            return self.gender
        if wht_return == 3:
            return self.life_expectancy


def invert_list():
    global obj_list
    obj_list.reverse()
    print_in_screen()


def order_by_name():
    global wht_return
    global obj_list
    wht_return = 0
    obj_list = sorted(obj_list, key=lambda x: x[0])
    print_in_screen()


def order_by_year():
    global wht_return
    global obj_list
    wht_return = 1
    obj_list = sorted(obj_list, key=lambda x: x[1])
    print_in_screen()


def order_by_gender():
    global wht_return
    global obj_list
    wht_return = 2
    obj_list = sorted(obj_list, key=lambda x: x[2])
    print_in_screen()


def order_by_lf():
    global wht_return
    global obj_list
    wht_return = 3
    obj_list = sorted(obj_list, key=lambda x: x[3])
    print_in_screen()




def print_in_screen():
    t.delete('1.0', END)
    global obj_list, record
    for i in range(record):
        t.insert(END, obj_list[i].country_name + ' '
                 + obj_list[i].year + ' '
                 + obj_list[i].gender + ' '
                 + obj_list[i].life_expectancy + '\n')


def print_year_1990():
    t.delete('1.0', END)
    global obj_list, record
    for i in range(record):
        if obj_list[i].year == '1990':
            t.insert(END, obj_list[i].country_name + ' '
                     + obj_list[i].year + ' '
                     + obj_list[i].gender + ' '
                     + obj_list[i].life_expectancy + '\n')


def print_year_2000():
    t.delete('1.0', END)
    global obj_list, record
    for i in range(record):
        if obj_list[i].year == '2000':
            t.insert(END, obj_list[i].country_name + ' '
                     + obj_list[i].year + ' '
                     + obj_list[i].gender + ' '
                     + obj_list[i].life_expectancy + '\n')


def print_year_2012():
    t.delete('1.0', END)
    global obj_list, record
    for i in range(record):
        if obj_list[i].year == '2012':
            t.insert(END, obj_list[i].country_name + ' '
                     + obj_list[i].year + ' '
                     + obj_list[i].gender + ' '
                     + obj_list[i].life_expectancy + '\n')


def print_gender_male():
    t.delete('1.0', END)
    global obj_list, record
    for i in range(record):
        if obj_list[i].gender == 'Male':
            t.insert(END, obj_list[i].country_name + ' '
                     + obj_list[i].year + ' '
                     + obj_list[i].gender + ' '
                     + obj_list[i].life_expectancy + '\n')


def print_gender_female():
    t.delete('1.0', END)
    global obj_list, record
    for i in range(record):
        if obj_list[i].gender == 'Female':
            t.insert(END, obj_list[i].country_name + ' '
                     + obj_list[i].year + ' '
                     + obj_list[i].gender + ' '
                     + obj_list[i].life_expectancy + '\n')


def print_gender_bothsexes():
    t.delete('1.0', END)
    global obj_list, record
    for i in range(record):
        if obj_list[i].gender == "Both sexes":
            t.insert(END, obj_list[i].country_name + ' '
                     + obj_list[i].year + ' '
                     + obj_list[i].gender + ' '
                     + obj_list[i].life_expectancy + '\n')


def find_country_by_name():
    global country_by_name, record
    d = MyDialog(root)
    root.wait_window(d.top)
    t.delete('1.0', END)
    global obj_list
    for i in range(record):
        if obj_list[i].country_name == country_by_name:
            t.insert(END, obj_list[i].country_name + ' '
                     + obj_list[i].year + ' '
                     + obj_list[i].gender + ' '
                     + obj_list[i].life_expectancy + '\n')

def donothing():
    return 0



obj = WorldData(None, None, None, None)

xmldoc = minidom.parse("ExpectativaVidaMundial.xml")

root = Tk()
root.title('Zimbabwe')
menubar = Menu(root)

t = Text(root, height=15, width=55)
scrollbar = Scrollbar(root)
scrollbar.config(command=t.yview)
t.config(yscrollcommand=scrollbar.set)
t.pack(side=LEFT)
scrollbar.pack(side=RIGHT, fill=Y, expand=False)
t.pack(side="left", fill="both", expand=True)

# cria listas de objetos
print("Carregando lista...")
obj_list = [WorldData(obj.parse_list_name(i),
                      obj.parse_list_year(i),
                      obj.parse_list_gender(i),
                      obj.parse_list_lifeEx(i))for i in range(record)]

print_in_screen()

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Refresh", command=print_in_screen)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

ordermenu = Menu(menubar, tearoff=0)
ordermenu.add_command(label="Invert order", command=invert_list)
ordermenu.add_separator()
ordermenu.add_command(label="Order by name", command=order_by_name)
ordermenu.add_command(label="Order by year", command=order_by_year)
ordermenu.add_command(label="Order by gender", command=order_by_gender)
ordermenu.add_command(label="Order by life expectancy", command=order_by_lf)
menubar.add_cascade(label="Order", menu=ordermenu)


showmenu = Menu(menubar, tearoff=0)
showmenuyear = Menu(showmenu, tearoff=0)
showmenugender = Menu(showmenu, tearoff=0)
showmenu.add_command(label="Show by country name", command=find_country_by_name)
showmenu.add_cascade(label="Choose a year", menu=showmenuyear)
showmenu.add_cascade(label="Choose a gender", menu=showmenugender)
showmenuyear.add_command(label="1990", command=print_year_1990)
showmenuyear.add_command(label="2000", command=print_year_2000)
showmenuyear.add_command(label="2012", command=print_year_2012)
showmenugender.add_command(label="Male", command=print_gender_male)
showmenugender.add_command(label="Female", command=print_gender_female)
showmenugender.add_command(label="Both sexes", command=print_gender_bothsexes)
menubar.add_cascade(label="Show", menu=showmenu)

scrollbar.config(command=t.yview)
root.config(menu=menubar)

root.mainloop()


