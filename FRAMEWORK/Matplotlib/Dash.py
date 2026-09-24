#dash is perfect for data dashboards this is upon the Plotly
from dash import Dash, html, dcc

#Dash --> the main app class(creates my web app)
#dcc--> Dash Core components (interactive widgets like dropdowns, sliders, graphs)
#html--> for building layouts using html tags(Div,H1,etc) inside Python.
app=Dash(__name__)
#this initializes my Dash app
#__name__ tells Dash where to look for resources like (CSS,JS)
app.layout = html.Div([#app.layout defines what the web page looks like
    html.H1("Hello Dash!"),#heading H1 means at the top
    dcc.Graph(#a chart components
        figure={
            "data": [{"x": [1,2,3], "y": [4,1,2], "type": "line", "name": "Test"}],
            #data contains the actual plot(x,y values types of chart)
            "layout": {"title": "Simple Line Chart"}
            #chart settings(title,axis labels, etc)
        }
    )
])

if __name__ == "__main__":#it starts a local web server
    app.run(debug=True)#debug=True means auto-reloads when i change code 
#it runs in local 