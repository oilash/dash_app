from dash import register_page, html,dcc,Input,Output,State,callback
import dash_bootstrap_components as dbc

import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS

save_folder = "/home/oil/Documents/budgeting_tool/dash_app/pages/support/data"

def dollar_format_func(x):
    if x < 0:
        return f"-${x:,.2f}"
    else:
        return f"${x:,.2f}"

def get_price(crypto):

    url = f"https://www.google.com/search?q={crypto}+price"
    data = requests.get(url)
    soup = BS(data.text,'html.parser')
    ans = soup.find("div",class_="BNeawe iBp4i AP7Wnd").text.replace(" Australian Dollar","").replace(",","")
    
    return float(ans)

def get_price_hist(crypto,days):

    api_key = '5cbbdd476d7be16a7aa55aa3f43f696da9d529c15113646d6ada090f28017e5f'
    url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={crypto}&tsym=USD&limit={days}&api_key={api_key}"
    hist_prices = requests.get(url).json()

    return pd.DataFrame().from_dict(json.loads(hist_prices))


register_page(__name__, path = "/cryptoTool")

cryptos_df = pd.read_feather(os.path.join(save_folder,"cryptos.feather"))

cryptos_lst = []

# for i in range(len(cryptos_df)):
#     crypto = cryptos_df.iloc[i]['crypto']
#     amount = cryptos_df.iloc[i]['amount']

#     value = get_price(crypto)

#     cryptos_lst.append(
#         [
#             dbc.Row([
#                 dbc.Col(html.H3(crypto)),
#                 dbc.Col(dcc.Input(amount,type = "number",id = f"crypto-amount-{i}")),
#                 dbc.Col(html.H5(dollar_format_func(amount*value)))

#     ])
#         ]
#     )

modal = html.Div([
    dbc.Button(html.H5("+"),id = "plus-button",n_clicks = 0),
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Add a Crypto")),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col(dcc.Input("BTC", type = "text",id = "the-crypto")),
                dbc.Col(dcc.Input(1,type = "number",id = "crypto-amount"))
            ])
        ]),
        dbc.ModalFooter([
            dbc.Row([
                dbc.Col(dbc.Button("Add", id = "add", class_name = "ms-auto",n_clicks = 0)),
                dbc.Col(dbc.Button("Cancel",id = "cancel",class_name = "ms-auto",n_clicks = 0))
            ]),
        ])
    ],
    id = "add-crypto-modal",
    is_open = False
    )
])


layout = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([
            modal
        ], id = "crypto-lst", width = {'size' : 4}),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H3("Crypto Holding Value"),

                ])
            )
        ], width = {'size' : 8})

    ])

])

@callback(
    Output("add-crypto-modal","is_open"),
    [Input("plus-button","n_clicks"),Input("cancel","n_clicks")],
    [State("add-crypto-modal","is_open")]
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open


@callback(
    Output("crypto-lst","children"),
    [Input("add","n_clicks"),
    State("the-crypto","value"),
    State("crypto-amount","value"),
    ],
    State("crypto-lst","children"),
    prevent_initial_call=True


)
def update_col(n_clicks,crypto,amount,current_lst):

    value = get_price(crypto)

    update = dbc.Row([
        dbc.Col(html.H3(crypto)),
        dbc.Col(dcc.Input(amount,type = "number",id = f"crypto-amount-{len(current_lst)}")),
        dbc.Col(html.H5(dollar_format_func(amount*value)))

    ])
    current_lst.append(update)

    df = pd.read_feather(path = os.path.join(save_folder, "cryptos.feather"))

    print(df)

    return current_lst
