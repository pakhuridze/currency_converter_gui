import tkinter as tk

exchange_rates = {
    'GEL_TO_USD': 1 / 2.5,
    'GEL_TO_EUR': 1 / 3.1,
    'EUR_TO_GEL': 3.1,
    'EUR_TO_USD': 3.1 / 2.5,
    'USD_TO_GEL': 2.5,
    'USD_TO_EUR': 2.5 / 3.1
}

# კონვერტაციის ფუნქცია
def convert_currency(amount, from_currency, to_currency):
    key = f'{from_currency}_TO_{to_currency}'
    if key in exchange_rates:
        rate = exchange_rates[key]
        return amount * rate
    else:
        return None

# კონვერტაციის ფუნქცია
def perform_conversion():
    # რადიოდან მიღებული პარამეტრების დაჭერა

    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    try:
        amount = float(amount_entry.get())
        error_label.config(text="")  # შეცდომის ფილდი იყოს ცარიელი თუ კი არ გავიდა ValueError ზე
    except ValueError:
        error_label.config(text="გთხოვთ შეიყვანოთ რიცხვითი მნიშვნელობა.")
        return
    # თუ კონვერტაცია არ ხდება იგივე ვალუტაზე
    if from_currency != to_currency:
        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            result_label.config(text=f'{amount} {from_currency} is equal to {result:.2f} {to_currency}')
        else:
            result_label.config(text="ასეთი კონვერტაცია შეუძლებელია.") # არ არსებული ვალუტის დროს შეცდომა
    else:
        result_label.config(text=f'{amount} {from_currency} is equal to {amount} {to_currency}') # გამოტანა ვალუტის კონვერტაციის

def clear_fields():
    from_currency_var.set("")
    to_currency_var.set("")
    amount_entry.delete(0, tk.END)
    result_label.config(text="")
    error_label.config(text="")

root = tk.Tk()

# კომპიუტერის ეკრანის ზომის გამოთვლა
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# აპლიკაციამ დაიკავოს ეკრანის 1/2 (50%)

window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)

root.geometry('%dx%d+0+0' % (window_width, window_height))

root.configure(background='#2c3e50')
root.title("ვალუტის კონვერტერი")

# ჩამოსაშლელი მენიუ და ცვლადების დასეტვა
from_currency_var = tk.StringVar(root)
to_currency_var = tk.StringVar(root)

# ფერებისა და სტილის განსაზღვრა
label_font = ('Helvetica', 12, 'bold')
entry_font = ('Helvetica', 12)
button_font = ('Helvetica', 12, 'bold')
label_fg = '#ecf0f1'
button_bg = '#3498db'
button_fg = '#ecf0f1'

# ვალუტის არჩევის ლეიბლები
from_currency_label = tk.Label(root, text="From:", fg=label_fg, bg='#2c3e50', font=label_font)
from_currency_label.pack(pady=5)

from_currency_menu = tk.OptionMenu(root, from_currency_var, "GEL", "USD", "EUR")
from_currency_menu.config(font=entry_font)
from_currency_menu.pack(pady=5)

to_currency_label = tk.Label(root, text="To:", fg=label_fg, bg='#2c3e50', font=label_font)
to_currency_label.pack(pady=5)

to_currency_menu = tk.OptionMenu(root, to_currency_var, "GEL", "USD", "EUR")
to_currency_menu.config(font=entry_font)
to_currency_menu.pack(pady=5)

# თანხის ბლოკი
amount_label = tk.Label(root, text="თანხის რაოდენობა:", fg=label_fg, bg='#2c3e50', font=label_font)
amount_label.pack(pady=5)

# თანხის ფილდი
amount_entry = tk.Entry(root, font=entry_font)
amount_entry.pack(pady=5)

# კონვერტაციის ღილაკი
convert_button = tk.Button(root, text="კონვერტაცია", font=button_font, bg=button_bg, fg=button_fg, command=perform_conversion)
convert_button.pack(pady=10)

# გასუფთავების ღილაკი
clear_button = tk.Button(root, text="გასუფთავება", font=button_font, bg='#e74c3c', fg=button_fg, command=clear_fields)
clear_button.pack(pady=5)

# შეცდომის გამოტანის ბლოკი
error_label = tk.Label(root, text="", fg="#e74c3c", bg='#2c3e50', font=label_font)
error_label.pack(pady=5)

# მნიშვნელობის გამოტანის ბლოკი
result_label = tk.Label(root, text="", fg=label_fg, bg='#2c3e50', font=label_font)
result_label.pack(pady=10)

root.mainloop()
