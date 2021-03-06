import dash_components
import dash
from dash.dependencies import Input, Output
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_components.MyCustomComponent(
        id='input',
        value='my-value',
        label='my-label'
    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
