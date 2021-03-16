from pyVies import api
import tkinter as tk


def vies_search(vat_id='317555100', country_code='DE'):
    try:
        vies = api.Vies()
        result = vies.request('317555100', 'DE', extended_info=True)
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
        return result


window = tk.Tk()
window.geometry("540x400")
l1 = tk.Label(text="Please enter the vat ID (with country code):")
e1 = tk.Entry()
button = tk.Button(
    text="Search!",
)
l1.grid(row=0, column=1)
e1.grid(row=0, column=2)
button.grid(row=0, column=3)
window.mainloop()

print(vies_search())