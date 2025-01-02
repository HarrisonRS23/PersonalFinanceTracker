import tkinter as tk 

import plaid
from plaid.api import plaid_api

# Window Setup 

root = tk.Tk()
root.title("Personal Finance Tracker")
root.mainloop()




# Available environments are
# 'Production'
# 'Sandbox'
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)