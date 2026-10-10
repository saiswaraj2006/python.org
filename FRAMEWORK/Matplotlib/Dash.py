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
'''

#example for the loading the iris flower dataset into a pandas
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df=px.data.iris()
print(df.head())#it prints the first five rows of the dataset
#also printing the last five rows of the dataset by using tail
print(df.tail())
'''
''''
     sepal_length  sepal_width  petal_length  petal_width    species  species_id
145           6.7          3.0           5.2          2.3  virginica           3
146           6.3          2.5           5.0          1.9  virginica           3
147           6.5          3.0           5.2          2.0  virginica           3
148           6.2          3.4           5.4          2.3  virginica           3
149           5.9          3.0           5.1          1.8  virginica           3
'''

'''
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load Iris dataset
df = px.data.iris()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Iris Dataset Visualization"),

    # Dropdowns for X and Y axes
    html.Div([
        html.Label("Select X-axis:"),
        dcc.Dropdown(
            id="x-axis-dropdown",
            options=[{"label": col, "value": col} for col in df.columns if col != "species"],
            #df.columns has-> ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'species']
            value="sepal_width"
        ),
        html.Label("Select Y-axis:"),
        dcc.Dropdown(
            id="y-axis-dropdown",
            options=[{"label": col, "value": col} for col in df.columns if col != "species"],
            value="sepal_length"
        )
    ], style={"width": "40%", "display": "inline-block","marginRight":"40px"}),
#Dropdown for chart type
    html.Div([
        html.Label("Select Chart Type:"),
        dcc.Dropdown(
            id="chart-type-dropdown",
            options=[
                {"label":"Scatter Plot","value":"scatter"},
                {"label":"Box Plot","value":"box"},
                {"label":"Histogram","value":"histogram"}
                
            ],
            value="scatter"

        )
    ], style={"width":"40%","display":"inline-block"}),
    # Graph output
    dcc.Graph(id="iris-graph")
])

@app.callback(
    Output("iris-graph", "figure"),
    [Input("x-axis-dropdown", "value"),
     Input("y-axis-dropdown", "value"),
     Input("chart-type-dropdown","value")]
)
def update_graph(x_col, y_col, chart_type):
    if chart_type=="scatter":
        fig=px.scatter(df,x=x_col, y=y_col, color="species",
                       title=f"Scatter Plot: {x_col} vs {y_col}")
    elif chart_type == "box":
        fig=px.box(df, x="species",y=x_col,
                   title=f"Box Plot: {x_col} by species")
    else: #histogram
        fig=px.histogram(df,x=x_col,color="species", barmode="overlay",
                         title=f"Histogram of {x_col}")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
'''
#iris dashboard with the tabs
#for switching between the different views (Scatter, box plot, histograms) 
#without cluttering
'''
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load Iris dataset
df = px.data.iris()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Iris Dataset Explorer with Tabs"),

    # Dropdowns for X and Y axes
    html.Div([
        html.Label("Select X-axis:"),
        dcc.Dropdown(
            id="x-axis-dropdown",
            options=[{"label": col, "value": col} for col in df.columns if col != "species"],
            value="sepal_width"
        ),
        html.Label("Select Y-axis:"),
        dcc.Dropdown(
            id="y-axis-dropdown",
            options=[{"label": col, "value": col} for col in df.columns if col != "species"],
            value="sepal_length"
        )
    ], style={"width": "40%", "marginBottom": "20px"}),

    # Tabs for chart type
    dcc.Tabs(id="tabs", value="scatter", children=[
        dcc.Tab(label="Scatter Plot", value="scatter"),#describing the tab names
        dcc.Tab(label="Box Plot", value="box"),
        dcc.Tab(label="Histogram", value="histogram")
    ]),

    # Graph output
    dcc.Graph(id="iris-graph")
])

@app.callback(
    Output("iris-graph", "figure"),
    [Input("x-axis-dropdown", "value"),
     Input("y-axis-dropdown", "value"),
     Input("tabs", "value")]
)
def update_graph(x_col, y_col, tab_choice):
    if tab_choice == "scatter":
        fig = px.scatter(df, x=x_col, y=y_col, color="species",
                         title=f"Scatter Plot: {x_col} vs {y_col}")
    elif tab_choice == "box":
        fig = px.box(df, x="species", y=x_col,
                     title=f"Box Plot: {x_col} by species")
    else:  # histogram
        fig = px.histogram(df, x=x_col, color="species", barmode="overlay",
                           title=f"Histogram of {x_col}")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
'''
'''
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import io
import base64#base64 string

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Upload Your Dataset Explorer"),

    # File upload component
    dcc.Upload(#this is the upload box it lets user to drag and drop or select a CSV file
        id="upload-data",
        children=html.Div([
            "Drag and Drop or ",
            html.A("Select a CSV File")
        ]),
        style={
            "width": "50%", "height": "60px", "lineHeight": "60px",
            "borderWidth": "1px", "borderStyle": "dashed",
            "borderRadius": "5px", "textAlign": "center", "margin": "10px"
        },
        multiple=False
    ),

    # Dropdowns for X and Y axes
    html.Div([
        dcc.Dropdown(id="x-axis-dropdown", placeholder="Select X-axis"),
        dcc.Dropdown(id="y-axis-dropdown", placeholder="Select Y-axis")
    ], style={"width": "50%", "marginTop": "20px"}),

    # Graph output
    dcc.Graph(id="output-graph")
])

# Helper function to parse uploaded file
def parse_contents(contents):
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)#splits the base64 string into type and actual data.
    #decodes the base64 back into text
    df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))#it reads it as a CSV using pandas.read_csv
    return df
#it returns the clean DataFrame(df) ready for plotting
@app.callback(
    [Output("x-axis-dropdown", "options"),
     Output("y-axis-dropdown", "options"),
     Output("output-graph", "figure")],
    Input("upload-data", "contents"),
    [State("x-axis-dropdown", "value"),#it checks the current dropdown selections(state)
     State("y-axis-dropdown", "value")]
)
def update_output(contents, x_col, y_col):#generates dropdowns options and plots the graph.
    if contents is None:
        return [], [], {}
    df = parse_contents(contents)
    options = [{"label": col, "value": col} for col in df.columns]
    fig={}
    # Default graph if both axes are chosen
    if x_col and y_col:
        #try to convert numeric if possible
        df[x_col]=pd.to_numeric(df[x_col],errors="ignore")
        df[y_col]=pd.to_numeric(df[y_col],errors="ignore")
        #if both numeric->scatter plot
        if pd.api.types.is_numeric_dtype(df[x_col]) and pd.api.types.is_numeric_dtype(df[y_col]):
            fig=px.scatter(df,x=x_col,y=y_col,title=f"{x_col} vs {y_col}")
        else:
            #if one is categorical->box plot
            fig=px.box(df,x=x_col,y=y_col,title=f"Box Plot:{y_col} vs {x_col}")
    return options, options, fig

if __name__ == "__main__":
    app.run(debug=True)
'''

from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import io
import base64#base64 string
from dash import dash_table

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Upload Your Dataset Explorer"),

    dcc.Upload(
        id="upload-data",
        children=html.Div(["Drag and Drop or ", html.A("Select a CSV File")]),
        style={
            "width": "50%", "height": "60px", "lineHeight": "60px",
            "borderWidth": "1px", "borderStyle": "dashed",
            "borderRadius": "5px", "textAlign": "center", "margin": "10px"
        },
        multiple=False
    ),
    html.Div([
    dcc.Input(
        id="filter-input",
        type="text",
        placeholder="Enter filter (e.g., Department=='HR')",
        style={"width": "50%", "marginTop": "10px"}
        )
    ]),


    html.Div([
        dcc.Dropdown(id="x-axis-dropdown", placeholder="Select X-axis"),
        dcc.Dropdown(id="y-axis-dropdown", placeholder="Select Y-axis"),
        dcc.Dropdown(
            id="chart-type-dropdown",
            options=[
                {"label": "Scatter Plot", "value": "scatter"},
                {"label": "Box Plot", "value": "box"},
                {"label": "Bar Chart", "value": "bar"},
                {"label": "Histogram", "value": "histogram"}
            ],
            value="scatter",
            placeholder="Select Chart Type"
        )
    ], style={"width": "50%", "marginTop": "20px"}),
    dash_table.DataTable(id="preview-table"),  
    dcc.Graph(id="output-graph")

])
# Helper function to parse uploaded file
def parse_contents(contents):
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    try:
        # Try reading as CSV
        df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
    except Exception as e:
        print("Error reading CSV:", e)
        # If CSV fails, try Excel
        try:
            df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e2:
            print("Error reading Excel:", e2)
            df = pd.DataFrame()  # fallback empty dataframe

    return df

@app.callback(
    [Output("x-axis-dropdown", "options"),
     Output("y-axis-dropdown", "options"),
     Output("preview-table", "data"),
     Output("preview-table", "columns"),
     Output("output-graph", "figure")],
    [Input("upload-data", "contents"),
     Input("x-axis-dropdown", "value"),
     Input("y-axis-dropdown", "value"),
     Input("chart-type-dropdown", "value"),
     Input("filter-input", "value")]
)
def update_output(contents, x_col, y_col, chart_type, filter_value):
    if contents is None:
        return [], [],[],[], {}

    df = parse_contents(contents)
    options = [{"label": col, "value": col} for col in df.columns]
        # Apply filter if provided
    if filter_value:
        try:
            df = df.query(filter_value)
        except Exception as e:
            print("Invalid filter:", e)
    #preview of first 5 rows
    preview_data = df.head().to_dict("records")
    preview_columns = [{"name": i, "id": i} for i in df.columns]
    fig = {}
    if x_col and y_col:
        df[x_col] = pd.to_numeric(df[x_col], errors="coerce")
        df[y_col] = pd.to_numeric(df[y_col], errors="coerce")

        if chart_type == "scatter":
            fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
        elif chart_type == "box":
            fig = px.box(df, x=x_col, y=y_col, title=f"Box Plot: {y_col} vs {x_col}")
        elif chart_type == "bar":
            fig = px.bar(df, x=x_col, y=y_col, title=f"Bar Chart: {y_col} vs {x_col}")
        elif chart_type == "histogram":
            fig = px.histogram(df, x=x_col, title=f"Histogram of {x_col}")

    return options, options, preview_data,preview_columns ,fig
if __name__ == "__main__":
    app.run(debug=True)
