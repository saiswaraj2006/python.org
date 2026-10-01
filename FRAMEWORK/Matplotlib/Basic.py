from dash import Dash,html,dcc
#creating a app to run in server
app=Dash(__name__)
app.layout=html.Div([
html.H1("Hello Matplotlib")])#creating a box of information
#it shows the"Hello Matplotlib" in heading form in big text
if __name__=="__main__":
    app.run(debug=True)
