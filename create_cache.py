import pandas as pd
import os

save_folder = "/home/oil/Documents/budgeting_tool/dash_app/pages/support/data"

lst = [
    ['rent',1],
    ['internet',1],
    ['power',1],
    ['water',1],
    ['food',1],
    ['insurance',1],
    ['transport',1],
    ['phone',1],
    ['gas',1],
    ['extra',1],
    ['tax',1],
    ['hecs',1],
    ['super',1],
    ['income',1],
    ['income_freq',1],
    ['interest_rate',1],
    ['initial_savings',1],

]

df = pd.DataFrame(
    data = lst,
    columns = ['name','value']
)

# df.to_feather(os.path.join(save_folder,"expense.feather"))

lst = [
    ['BTC' , 0.00797919],
    ['ETH' , 0.04119883],
    ['MATIC' , 35.2268]
]

df = pd.DataFrame(
    data = lst,
    columns = ['crypto','amount']
)

df.to_feather(os.path.join(save_folder,'cryptos.feather'))
