from dash import Dash,html
import dash_bootstrap_components as dbc
import dash
import pyfiglet

external_stylesheets = [dbc.themes.COSMO]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True
    )

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Budget Tool", href = "/budgetTool")),
            dbc.NavItem(dbc.NavLink("Crypto Tool", href = "/cryptoTool"))
        ],
        brand="Finances Baby",
        brand_href="/",
        color="primary",
        dark=True,
    ),
    dash.page_container
])

if __name__== "__main__":
    print(pyfiglet.figlet_format("App is Running!"))
    app.run_server(debug = True)

