#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State


# Connect to main app.py file
from main import app
from main import server

# Connect to your app pages
from app import textbox, upload


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "color": "#f5f0ed",
    "background-color": "#8A8783"}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "1rem 1rem"
}

sidebar = html.Div([
        html.Img(src='./assets/exxonmobil_black_logo.png', style={"max-width": "200px", "margin-left": "0.5rem"}),
        html.Hr(),
        html.H4("Risk Assessment ", style={'textAlign': 'center'}),      
        html.P("Machine Learning Tool", className="lead", style={'textAlign': 'center'}),
        html.Br(),
        dbc.Nav([
        dbc.NavLink("User Input", href="/app/textbox", className="page-link",
                   style = {"color": "#f5f0ed", "background-color": "#73706c", "height": "40px"}),
        html.Br(style={"margin-top": "5px"}),
        dbc.NavLink("Batch Prediction", href="/app/upload", className="page-link",
                   style = {"color": "#f5f0ed", "background-color": "#73706c",  "height": "40px"})],
        vertical=True,
        pills=True,
        )],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

#app layout

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
    html.Div(id='output-data-upload'),],
    style = {"body-bg": "#f5f0ed"}
    )

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app/textbox':
        return textbox.layout
    if pathname == '/app/upload':
        return upload.layout
    else:
        return textbox.layout    
    
if __name__=='__main__':
    app.run_server(debug=False, use_reloader=False, port = 8030)


# In[ ]:




