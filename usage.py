import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        "https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css"]
options = [{"label": "1", "value": "1"}, {"label": "2", "value": "2"}]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    dcc.LockableDropdown(options=options, id="dd_master"),
    html.Br(),
    dcc.Dropdown(options=options, id="dd_slave")
])


@app.callback(Output("dd_slave", "value"), [Input("dd_master", "value"), Input("dd_master", "locked")])
def update_dd_slave(dd_master_value, dd_master_locked):
    return dd_master_value if dd_master_locked else None


if __name__ == '__main__':
    app.run_server(debug=True)
