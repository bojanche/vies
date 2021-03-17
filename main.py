from pyVies import api
import tkinter as tk
from tkinter import ttk


def vies_search(vat_id='317555100', country_code='DE'):
    vat_id = e1_value.get()
    country_code = l2["text"]
    try:
        vies = api.Vies()
        result = vies.request(vat_id, country_code, extended_info=True)
        # '17890798564', 'FR'
        # works as well
        # result = vies.request('RO2785503')
        # result = vies.request('RO2785503', 'RO')

    except api.ViesValidationError as e:
        print(e)
    except api.ViesHTTPError as e:
        print(e)
    except api.ViesError as e:
        print(e)
    else:
        t1.insert(tk.END, result)
        return result


def callback(event):
    selected = event.widget.get()
    l2['text'] = country_list[selected]


window = tk.Tk()
window.geometry("540x400")
country_list = {'Austria': 'AT', 'Belgium': 'BE', 'Bulgaria': 'BG', 'Cyprus': 'CY', 'Czech Republic': 'CZ',
                'Germany': 'DE', 'Denmark': 'DK', 'Estonia': 'EE', 'Greece': 'EL', 'Spain': 'ES',
                'Finland': 'FI', 'France': 'FR', 'Croatia': 'HR', 'Hungary': 'HU', 'Ireland': 'IE',
                'Italy': 'IT', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Latvia': 'LV', 'Malta': 'MT',
                'The Netherlands': 'NL', 'Poland': 'PL', 'Portugal': 'PT', 'Romania': 'RO', 'Sweden': 'SE',
                'Slovenia': 'SI', 'Slovakia': 'SK', 'Northern Ireland': 'XI'}

l1 = tk.Label(text="Please select the country:")
combobox_values = list(country_list)
d1 = ttk.Combobox(window, values=combobox_values)
d1.current(5)
l2 = tk.Label(text='Country code')
l3 = tk.Label(text='Please enter VAT ID:')

e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.insert(0, "317555100")

button = tk.Button(text="Search!", command=vies_search)
t1 = tk.Text(window,height=15, width=40)
l1.grid(row=0, column=0)
d1.grid(row=0, column=1)
l2.grid(row=0, column=2)
l3.grid(row=1, column=0)
e1.grid(row=1, column=1)
button.grid(row=1, column=3)
t1.grid(row=2, column=0, columnspan=4)

d1.bind("<<ComboboxSelected>>", callback)

window.mainloop()
