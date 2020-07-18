import dash
import dash_core_components as dcc
import dash_html_components as html 
import pandas_datareader.data as web
from dash.dependencies import Input, Output
import datetime

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
       Enter Stock Code:
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')

])

@app.callback (
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def upddate_graph(input_data):
    start = datetime.datetime(2019, 7, 16)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
    return html.Div(dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )
    )

if __name__ == '__main__':
    app.run_server(debug=True)
