from dash import Dash,html
import dash_bootstrap_components as dbc
import dash

external_stylesheets = [dbc.themes.COSMO]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    use_pages=True
    )

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Budget Tool", href="/budgetTool")),
        ],
        brand="Finances Baby",
        brand_href="/",
        color="primary",
        dark=True,
    ),
    dash.page_container
])

if __name__== "__main__":
    print("App is running!")
    app.run_server(debug = True)

