import requests
import tkinter as tk
from tkinter import messagebox

def get_conversion_rate():
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"]["USD"]
    else:
        return None

def convert_currency():
    try:
        amount_inr = float(entry_inr.get())
        conversion_rate = get_conversion_rate()
        if conversion_rate:
            amount_usd = amount_inr * conversion_rate
            label_result.config(text=f"USD: ${amount_usd:.2f}")
        else:
            messagebox.showerror("Error", "Error fetching conversion rate.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


root = tk.Tk()
root.title("Rupees to Dollar Converter")


tk.Label(root, text="Enter amount in INR:").grid(row=0, column=0, padx=10, pady=10)
entry_inr = tk.Entry(root)
entry_inr.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Convert to USD", command=convert_currency).grid(row=1, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="USD: $0.00")
label_result.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
