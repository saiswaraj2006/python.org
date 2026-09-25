#dash is perfect for data dashboards this is upon the Plotly
'''
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
'''
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
# Sample data
x = np.linspace(0, 10, 100)
df = pd.DataFrame({
    "x": x,
    "sin(x)": np.sin(x),
    "cos(x)": np.cos(x),
    "category": np.random.choice(["A", "B", "C"], size=100),
    "values": np.random.randint(1, 10, size=100)
})
# Create app
app = Dash(__name__)
# Layout with multiple charts
app.layout = html.Div([
    html.H1("Multi‑Chart Dashboard"),
    # Line chart
    dcc.Graph(
        id="line-chart",
        figure=px.line(df, x="x", y=["sin(x)", "cos(x)"], title="Sine & Cosine")
    ),
    # Bar chart
    dcc.Graph(
        id="bar-chart",
        figure=px.bar(df, x="category", y="values", title="Category Values")
    ),
    # Histogram
    dcc.Graph(
        id="histogram",
        figure=px.histogram(df, x="values", nbins=10, title="Value Distribution")
    )
])
if __name__ == "__main__":
    app.run(debug=True)
