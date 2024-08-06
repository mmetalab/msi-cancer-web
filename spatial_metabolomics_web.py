from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from pages import introduction, about, database, blankPage, visualization


app = Dash(__name__,
    title="Spatial Metabolomics Visualization Web",
    external_stylesheets=[dbc.icons.FONT_AWESOME]
)

indexLayout = html.Div([
    dcc.Location(id='url', pathname='/introduction', refresh=False),
    html.Div(id='page-content')
])

# Create a "complete" layout for validating all callbacks. Otherwise when dash tries
# to validate them, most of them will thorw an error since they are linked to
# components that are not currently on the displayed page and so are not part of the 
# current layout
app.validation_layout = html.Div([
    indexLayout,
    introduction.layout,
    database.layout,
    visualization.layout,
    blankPage.layout
])

# This is the actual layout of the app
app.layout = indexLayout

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/introduction':
        return introduction.layout
    elif pathname == '/about':
        return about.layout
    elif pathname == '/database':
        return database.layout
    elif pathname == '/visualization':
        return visualization.layout
    else:
        return blankPage.layout


# This server object will be loaded by the WSGI script to be served as a webapp
# in a production server
server = app.server

# This will only be executed during debug when run locally, since WSGI does not 
# run this as __main__ but only takes the "server" variable
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080)
    # app.run_server(debug=True)

# gunicorn spatial_metabolomics_web:server