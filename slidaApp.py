Run this app with `python callbak.py` and
# visit http://127.0.0.1:2050/ in your web browser.

from dash import Dash, dcc, html, callback, Input, Output
import plotly.express as px
import pandas as pd

#connect to the data. 
df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

#initialise the app
app=Dash(__name__)
server=app.server

#define the app layout
app.layout=html.Div([
    html.H1('Slider', style={'color':'red', 'textAlign':'center', 'fontSize':'37px'}),
    html.Hr(),
    dcc.Graph(id='graf'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year):str(year) for year in df['year'].unique()},
        id='sliider')
])

#callback decorator to connect between the output and input components
@callback(
    Output('graf','figure'),
    Input('sliider','value')
)
def updateApp(selection):
    dff=df[df.year==selection]
    fig=px.scatter(dff, x='lifeExp', y='gdpPercap',
                   size='pop',
                   color='continent',
                   hover_name='country',
                   log_x=True, size_max=55)
    fig.update_layout(transition_duration=500)
    return fig

#run the app
if __name__ == '__main__':
    app.run(debug=True, port=4050)