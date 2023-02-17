# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

colors = {
    'background' : '#111111',
    'text':'#7FDBFF'
}


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Date": ["11/30/2022", "12/01/2022", "12/02/2022", "12/03/2022", "12/05/2022", "12/08/2022"],
    "Duration": [4.85, 15.25, 25.45, 50.23, 30.48, 5.98],
    "Distance": [.5, 2.1, 3.1, 5.8, 4, .90]
})
df['Pace']=df['Distance']/df['Duration']

userName='Alex'
desc_of_view='Tuta Atua'

fig = px.bar(df, x="Date", y="Duration", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[html.H1(children=f'{userName}-Workout Analytics',
                     style={
                         'textAlign':'center',
                         'color':colors['text']
                     }),

    html.Div(children=f'''{desc_of_view}:Just Some Sample Text ''',
            style={
                'textAlign':'center',
                'color':colors['text']
            }),
              
#     html.Div(children=[
#         html.Label('Dropdown'),
#         dcc.Dropdown(['Duration','Distance','Pace'],'Duration',id='comparison-metric')
#     ]),

    dcc.Graph(id='example-graph'),
    dcc.Dropdown(['Duration','Distance','Pace'],'Duration',id='comparison-metric')
])

# @app.callback(
#     Output('example-graph','figure'),
#     Input('comparison-metric','value'))

@app.callback(
    Output('example-graph', 'figure'),
    Input('comparison-metric', 'value'))
def update_metric_graph(comparison_metric):
    fig = px.bar(df, x="Date", y=comparison_metric, barmode="group")
    fig.update_yaxes(title=comparison_metric,type='linear')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
