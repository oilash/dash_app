from dash import html,dcc,register_page,Input,Output,callback
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

import plotly.graph_objects as go
import datetime as dt
import pandas as pd
import os

from pages.support.useful_funcs import tax,hecs

register_page(__name__,path='/budgetTool')

save_folder = "/home/oil/Documents/budgeting_tool/dash_app/pages/support/data"

df = pd.read_feather(path = os.path.join(save_folder,"expense.feather")).set_index("name")
# incomes = pd.read_feather(path = os.path.join(save_folder,"incomes")).set_index("name")

# incomes = pd.DataFrame(
#     data = [
#         ['income',1],
#         ['income_freq',"Yearly"],
#         ['initial_savings',1],
#         ['interest_rate',0.04]
#     ],
#     columns = ['name','value']
# ).set_index("name")

# print(incomes)

income_freqs = {
    0 : 'Yearly',
    1 : 'Quarterly',
    2 : 'Monthly',
    3 : 'Fortnightly',
    4 : 'Weekly'
}

income_freqs_index = 0

layout = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H3("Income"),
            dbc.Row([
                dbc.Col(html.H5("Income")),
                dbc.Col(dcc.Input(id = "income",type="number",value = df.loc['income']['value']))
            ]),
            dbc.Row([
                dbc.Col(html.H5("Income Frequency")),
                dbc.Col(dcc.Dropdown(
                    ['Yearly','Quarterly','Monthly','Fortnightly','Weekly'],
                    income_freqs[df.loc['income_freq']['value']],
                    id = "income-frequency-dd"
                    ))
            ]),
            dbc.Row([
                dbc.Col(html.H5("Initial Savings")),
                dbc.Col(dcc.Input(id="initial-savings",type = "number",value = df.loc['initial_savings']['value']))
            ]),
            dbc.Row([
                dbc.Col(html.H5("Interest Rate")),
                dbc.Col(dcc.Input(id = "interest-rate",type = "number",value = df.loc['interest_rate']['value']))
            ])
        ]),
        dbc.Col([
            html.H3("Expenses"),
            dbc.Row([
                    dbc.Col(html.H5("Rent")),
                    dbc.Col(dcc.Input(id = "rent",type = "number",value = df.loc['rent']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Internet")),
                    dbc.Col(dcc.Input(id = "internet",type = "number",value = df.loc['internet']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Power")),
                    dbc.Col(dcc.Input(id = "power",type = "number",value = df.loc['power']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Water")),
                    dbc.Col(dcc.Input(id = "water",type = "number",value = df.loc['water']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Food")),
                    dbc.Col(dcc.Input(id = "food",type = "number",value = df.loc['food']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Insurance")),
                    dbc.Col(dcc.Input(id = "insurance",type = "number",value = df.loc['insurance']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Transport")),
                    dbc.Col(dcc.Input(id = "transport",type = "number",value = df.loc['transport']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Phone")),
                    dbc.Col(dcc.Input(id = "phone",type = "number",value = df.loc['phone']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Gas")),
                    dbc.Col(dcc.Input(id = "gas",type = "number",value = df.loc['gas']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Extra")),
                    dbc.Col(dcc.Input(id = "extra",type = "number",value = df.loc['extra']['value']))
                ]),
                dbc.Row([
                    dbc.Col(html.H5("Saved")),
                    dbc.Col(dcc.Input(id = "saving",type = "number"))
                ])
        ]),
        dbc.Col([
            html.H3("Corporate Pay outs & Government Theft"),
            dbc.Row([
                dbc.Col(html.H5("Tax")),
                dbc.Col(html.H5(id = "tax-val")),
                dbc.Col(dbc.Checkbox(id = "tax-check",value = True))
            ]),
            dbc.Row([
                dbc.Col(html.H5("HELP-HECS")),
                dbc.Col(html.H5(id = "hecs-val")),
                dbc.Col(dbc.Checkbox(id = "hecs-check",value = True))

            ]),
            dbc.Row([
                dbc.Col(html.H5("Super")),
                dbc.Col(html.H5(id = "super")),
                dbc.Col(dbc.Checkbox(id = "super-check",value = True))
            ])
        ])
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = "pie-chart",),
            width = {"size":6}
        ),
        dbc.Col(
            dcc.Graph(id = "bar-graph",),
            width = {"size":6}
        )
    ])
])

@callback(
    Output("pie-chart","figure"),
    Output("bar-graph","figure"),
    Output("saving",'value'),
    Output("tax-val","children"),
    Output("hecs-val","children"),
    Output("super","children"),
    [
        Input("income","value"),
        Input("income-frequency-dd","value"),
        Input("interest-rate","value"),
        Input("initial-savings","value"),

        Input("tax-check","value"),
        Input("hecs-check","value"),
        Input("super-check","value"),

        Input("rent","value"),
        Input("internet","value"),
        Input("power","value"),
        Input("water","value"),
        Input("food","value"),
        Input("insurance","value"),
        Input("transport","value"),
        Input("phone","value"),
        Input("gas","value"),
        Input("extra","value"),

    ]
)
def table_update(income,income_freq,interest_rate,initial_savings,tax_inc,hecs_inc,super_inc,rent,internet,power,water,food,insurance,transport,phone,gas,extra):

    if income == 0 or income == None:
        raise PreventUpdate

    income_freqs = {
        'Yearly' : 0,
        'Quarterly' : 1,
        'Monthly' : 2,
        'Fortnightly': 3,
        'Weekly': 4
    }

    if income_freq == 'Yearly':
        freq = 12
    elif income_freq == 'Quarterly':
        freq = 4
    elif income_freq == 'Monthly':
        freq = 1
    elif income_freq == 'Fortnightly':
        freq = 0.5
    elif income_freq == 'Weekly':
        freq = 0.25
    
    monthly_income = income/freq

    if tax_inc:
        tax_val = tax(income)/freq
    else:
        tax_val = 0

    if hecs_inc:
        hecs_val = hecs(income)/freq
    else:
        hecs_val = 0
    
    if super_inc:
        super_val = monthly_income*0.1
    else:
        super_val = 0

    income_lst = [
        'income',
        'income_freq',
        'interest_rate',
        'initial_savings'
    ]

    income_val = [
        income,
        income_freqs[income_freq],
        interest_rate,
        initial_savings
    ]

    for i in range(len(income_lst)):
        if income_val[i] == (0 or None):
            income_lst[i] = [income_lst[i],0]
        else:
            income_lst[i] = [income_lst[i],income_val[i]]

    # pd.DataFrame(
    #     data = income_lst,
    #     columns=['name','value']
    # ).to_feather(os.path.join(save_folder,"incomes"))

    expenses = [
        'rent',
        'internet',
        'power',
        'water',
        'food',
        'insurance',
        'transport',
        'phone',
        'gas',
        'extra',
        'tax',
        'hecs',
        'super'
    ]

    expenses_val = [
        rent,
        internet,
        power,
        water,
        food,
        insurance,
        transport,
        phone,
        gas,
        extra,
        tax_val,
        hecs_val,
        super_val
    ]


    for i in range(len(expenses)):
        if expenses_val[i] == None:
            expenses[i] = [expenses[i],0]
        else:
            expenses[i] = [expenses[i],expenses_val[i]]

    update_cache = expenses + income_lst
    print(update_cache)
    df = pd.DataFrame(
        data = expenses,
        columns = ['name','value']
    )
    print(df)
    pd.DataFrame(
        data = update_cache,
        columns = ['name','value']
    ).to_feather(path = os.path.join(save_folder,"expense.feather"))



    df['percent'] = df['value'].apply(lambda x: 100 * x/monthly_income)
    tot_expense = df['value'].sum()
    saved = monthly_income - tot_expense
    f_saved = saved+initial_savings

    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels = df['name'],
        values = df['percent']
    ))

    fig.update_layout(
        title = "Expenses Breakdown"
    )
    forecast = []
    c_month = dt.datetime.today()
    for i in range(12):
        forecast.append([c_month.strftime("%b '%y"),tot_expense,f_saved])
        c_month = c_month + dt.timedelta(days = 31)
        f_saved += saved+interest_rate*f_saved/12
    forecast = pd.DataFrame(
        data = forecast,
        columns = ['month','expenses','saved']
    )
    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        x = forecast['month'],
        y = forecast['saved'],
        name = "Savings"
    ))
    fig_bar.add_trace(go.Bar(
        x = forecast['month'],
        y = forecast['expenses'],
        name = 'Expenses'
    ))

    fig_bar.update_layout(
        barmode = "stack",
        xaxis_title = "Month",
        title = "12 Month Forecast",
        yaxis_tickformat = "$~s"
    )
    return fig,fig_bar,saved,tax_val,hecs_val,super_val

