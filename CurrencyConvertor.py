
import tkinter as tk
import requests

# Defining allowed currencies
common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'NZD']

# Creating a CurrencyConverter class
class CurrencyConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Currency Converter")
        self.root.geometry("200x200")

        self.from_var = tk.StringVar(self.root)
        self.from_var.set("USD")
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=10)

        self.to_var = tk.StringVar(self.root)
        self.to_var.set("EUR")
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=10)

        self.amount_label = tk.Label(self.root, text="Amount: ")
        self.amount_label.pack(pady=1)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=1)

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=1)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=1)

        self.root.mainloop()

    def convert_currency(self):
        try:
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()
            amount = float(self.amount_entry.get())

            # Fetching the exchange rate
            response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
            data = response.json()
            
            if response.status_code == 200:
                rate = data['rates'].get(to_currency)
                if rate:
                    converted_amount = amount * rate
                    self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
                else:
                    self.result_label.config(text="Conversion rate not available")
            else:
                self.result_label.config(text="Failed to retrieve data")

        except ValueError:
            self.result_label.config(text="Please enter a valid number")
        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Error occurred: {e}")
        except Exception as e:
            self.result_label.config(text=f"Unexpected error: {e}")

# Running the converter if the script is executed
if __name__ == "__main__":
    CurrencyConverter()



