from dash import Dash,html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    use_pages=True
    )

# app.layout = html.Div([
#     dbc.NavbarSimple([

#     ]),
    
# ])

if __name__== "__main__":
    print("App is running!")
    app.run_server(debug = True)

