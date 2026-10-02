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
'''
'''
from dash import Dash, dcc, html , Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample training data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])  # y = 2x
model = LinearRegression().fit(X, y)
app = Dash(__name__)

app.layout = html.Div([
    html.H1("ML Prediction Dashboard"),

    # Slider for input value
    dcc.Slider(
        id="input-slider",
        min=0, max=10, step=1, value=5,
        marks={i: str(i) for i in range(0, 11)}
    ),

    # Output prediction
    html.Div(id="prediction-output", style={"fontSize": 24, "marginTop": 20})
])

# Callback: predict based on slider
@app.callback(
    Output("prediction-output", "children"),
    [Input("input-slider", "value")]
)
def update_prediction(x_value):
    prediction = model.predict([[x_value]])[0]
    return f"Prediction for x={x_value}: y={prediction:.2f}"
if __name__ == "__main__":
    app.run(debug=True)
'''
'''
#Dash+ML Visualization Example
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression
#Training data(y=2x)
X=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([2,4,6,8,10])
model=LinearRegression().fit(X,y)
app=Dash(__name__)
app.layout=html.Div([
    html.H1("ML Prediction Visualization"),
    dcc.Slider(
        id="input_slider",
        min=0,max=10,step=1,value=5,
        marks={i:str(i) for i in range(0,11)}
    ),
    #graph
    dcc.Graph(id="Prediction-graph")
])
@app.callback(
    Output("Prediction-graph","figure"),
    Input("input_slider","value")
)
def update_chart(x_value):
    x_range=np.linspace(0,10,100).reshape(-1,1)
    y_pred=model.predict(x_range)
    #prediction point
    y_point=model.predict([[x_value]])[0]
    fig=go.Figure()
    #training data points
    fig.add_trace(go.Scatter(x=X.flatten(), y=y, mode="markers", name="Training Data"))
    # Regression line
    fig.add_trace(go.Scatter(x=x_range.flatten(), y=y_pred, mode="lines", name="Regression Line"))
    # Predicted point
    fig.add_trace(go.Scatter(x=[x_value], y=[y_point], mode="markers", 
                             marker=dict(color="red", size=12), name="Prediction"))
    fig.update_layout(title=f"Prediction for x={x_value}: y={y_point:.2f}",
                      xaxis_title="X", yaxis_title="Y")
    return fig
if __name__ == "__main__":
    app.run(debug=True)
#the linear model predicts the output by training data it predicts
'''
'''
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor#adding the decision regression

# Training data (y = 2x + noise)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2.2, 3.9, 6.1, 7.8, 10.2])  # slightly noisy
# Models
linear_model = LinearRegression().fit(X, y)
poly_model = make_pipeline(PolynomialFeatures(2), LinearRegression()).fit(X, y)
tree_model=DecisionTreeRegressor(max_depth=3).fit(X,y)
# Create app
app = Dash(__name__)
app.layout = html.Div([
    html.H1("ML Model Comparison Dashboard"),#heading
    # Dropdown to select model
    dcc.Dropdown(
        id="model-dropdown",
        options=[
            {"label": "Linear Regression", "value": "linear"},
            {"label": "Polynomial Regression (degree=2)", "value": "poly"},
            {"label": "Decision Tree Regression","value":"tree"}
        ],
        value="linear"
    ),
    # Slider for prediction input
    dcc.Slider(
        id="input-slider",#id is a string used to connect inputs and outputs in callbacks
        #above id="input-slider" matches the slider's id
        min=0, max=10, step=1, value=5,
        marks={i: str(i) for i in range(0, 11)}
    ),
    html.Div(id="prediction-text",style={"fontSize":22,"marginTop":20}),
    #div is a container element from dash.html its basically the Dash version of the HTML<div> tag
    # use it to group content together or display text    
    # # Graph output
    dcc.Graph(id="prediction-graph")#matches the graphs's id
])
@app.callback(
    [Output("prediction-text","children"),
     Output("prediction-graph", "figure")],
    [Input("model-dropdown", "value"),
     Input("input-slider", "value")]
)
def update_chart(selected_model, x_value):
    x_range = np.linspace(0, 10, 100).reshape(-1, 1)

    if selected_model == "linear":
        y_pred = linear_model.predict(x_range)
        y_point = linear_model.predict([[x_value]])[0]
        model_name = "Linear Regression"
    elif selected_model == "poly":
        y_pred = poly_model.predict(x_range)
        y_point = poly_model.predict([[x_value]])[0]
        model_name = "Polynomial Regression (degree=2)"
    else:
        y_pred = tree_model.predict(x_range)
        y_point = tree_model.predict([[x_value]])[0]
        model_name = "Decision Tree Regression"
    text_output=f"{model_name}-> Prediction for x={x_value}: y={y_point:.2f}"
    fig = go.Figure()

    # Training data points
    fig.add_trace(go.Scatter(x=X.flatten(), y=y, mode="markers", name="Training Data"))
    # Regression line/curve
    fig.add_trace(go.Scatter(x=x_range.flatten(), y=y_pred, mode="lines", name=model_name))
    # Predicted point
    fig.add_trace(go.Scatter(x=[x_value], y=[y_point], mode="markers",
                             marker=dict(color="red", size=12), name="Prediction"))
    fig.update_layout(xaxis_title="X", yaxis_title="Y")

    return text_output,fig

if __name__ == "__main__":
    app.run(debug=True)
'''
'''
from dash import Dash, html, dcc
import plotly.express as px
# Sample data
df = px.data.iris()#it is a built in dataset 
#the iris dataset is a famous dataset in machine learning and statistics
'''
'''
it contains measurements of iris flowers
sepal_length
sepal_width
sepal_length
petal_width
species(setosa,versicolor,virginica)
'''
'''
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Simple Graph Example"),
    dcc.Graph(#this displays a plotly chart.
        id="my-graph",#gives the graph name so that i can reference it later.
        figure=px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    )
])
if __name__ == "__main__":
    app.run(debug=True)
'''

#example for the loading the iris flower dataset into a pandas
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df=px.data.iris()
print(df.head())#it prints the first five rows of the dataset
#also printing the last five rows of the dataset by using tail
print(df.tail())