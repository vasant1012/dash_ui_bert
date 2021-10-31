import base64
from datetime import datetime
import io
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import pathlib
from main import app
import random
#import joblib
#import torch
#import config
#import dataset_predict
# from model_predict import EntityModel
import warnings
warnings.filterwarnings('ignore')

# get relative data folder
PATH = pathlib.Path(__file__).parent

layout = html.Div([html.H2("Batch Prediction", className="display-5", style={'textAlign': 'top-center'}), html.Br(),
    dcc.Upload(
        id='upload-data',
        children=html.Div('Click to select file Or Drag and Drop'),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '55px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            "background-color" : "#73716D",
            "color": "white",
            'font-weight': 'bold'},
        multiple=True), # Allow multiple files to be uploaded
        html.Div(id='output-data-upload'),
                  ])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)        
    if '.csv' in filename:
        # Assume that the user uploaded a CSV file
        df = pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
#         meta_data = joblib.load('./trained model/meta.bin')
#         enc_target1 = meta_data["enc_target1"]
#         enc_target2 = meta_data["enc_target2"]
#         enc_target3 = meta_data["enc_target3"]

#         num_target1 = len(list(enc_target1.classes_))
#         num_target2 = len(list(enc_target2.classes_))
#         num_target3 = len(list(enc_target3.classes_))
        
#         probs = ["A", "B", "C", "D", "E"]
#         cons = ["I", "II", "III", "IV"]
#         ipc = ["df", "pi", "go"]
#         df["Probs"] = random.choices(probs, k = 1)
#         df["Cons"] =  random.choices(cons, k = 1)
#         df["IPC"] =  random.choices(ipc, k = 1)
        
#         sentences = df.values
#         test_dataset = dataset_predict.Dataset(texts=sentences)

#         device = torch.device("cpu")
#         model = EntityModel(num_target1=num_target1, num_target2=num_target2, num_target3=num_target3)
#         model.load_state_dict(torch.load(config.MODEL_PATH))
#         model.to(device)

#         with torch.no_grad():
#             pred_target1 = []
#             pred_target2 = []
#             pred_target3 = []
#             for data in test_dataset:
#                 for k, v in data.items():
#                     data[k] = v.to(device).unsqueeze(0)
#                 target1, target2, target3 = model(**data)
#                 prob = target1.argmax().cpu().numpy().reshape(-1)
#                 prob = enc_target1.inverse_transform(prob)[0]
#                 pred_target1.append(prob)
#                 cons = target2.argmax().cpu().numpy().reshape(-1)
#                 cons = enc_target2.inverse_transform(cons)[0]
#                 pred_target2.append(cons)
#                 ipc = target3.argmax().cpu().numpy().reshape(-1)
#                 ipc = enc_target3.inverse_transform(ipc)[0]
#                 pred_target3.append(ipc)

################################################################################################
        probs = ["A", "B", "C", "D", "E"]
        cons = ["I", "II", "III", "IV"]
        ipc = ["df", "pi", "go"]   
        df["Predicted Probs"] = random.choices(probs, k = len(df.values))
        df["Predicted Cons"] =  random.choices(cons, k = len(df.values))
        df["Predicted IPC"] =  random.choices(cons, k = len(df.values))
        return  html.Div([html.Hr(style={"height":"2px"}),
                html.H5(filename),
                html.H6(datetime.now()),
                html.Hr(),
                dbc.Table.from_dataframe(df, bordered=True, style={'textAlign': 'center', "background-color" : "#DBDBDA"}),
                html.Hr(style={"height":"2px"}),
                html.Div([dbc.Button("Download",
                            download=df.to_csv("Batch Prediction Results.csv"),
                            external_link=True,
                            style={"background-color" : "#73706c", "height": "40px"})]),
                         ],style= {"padding": "2rem 1rem"})
                

    elif '.xls' in filename:
        # Assume that the user uploaded an excel file
        df = pd.read_excel(io.BytesIO(decoded))
#         meta_data = joblib.load('./trained model/meta.bin')
#         enc_target1 = meta_data["enc_target1"]
#         enc_target2 = meta_data["enc_target2"]
#         enc_target3 = meta_data["enc_target3"]

#         num_target1 = len(list(enc_target1.classes_))
#         num_target2 = len(list(enc_target2.classes_))
#         num_target3 = len(list(enc_target3.classes_))
        
#         sentences = df.values
#         test_dataset = dataset_predict.Dataset(texts=sentences)
        
#         probs = ["A", "B", "C", "D", "E"]
#         cons = ["I", "II", "III", "IV"]
#         ipc = ["df", "pi", "go"]
#         df["Probs"] = random.choices(probs, k = 1)
#         df["Cons"] =  random.choices(cons, k = 1)
#         df["IPC"] =  random.choices(ipc, k = 1)

#         device = torch.device("cpu")
#         model = EntityModel(num_target1=num_target1, num_target2=num_target2, num_target3=num_target3)
#         model.load_state_dict(torch.load(config.MODEL_PATH))
#         model.to(device)

#         with torch.no_grad():
#             pred_target1 = []
#             pred_target2 = []
#             pred_target3 = []
#             for data in test_dataset:
#                 for k, v in data.items():
#                     data[k] = v.to(device).unsqueeze(0)
#                 target1, target2, target3 = model(**data)
#                 prob = target1.argmax().cpu().numpy().reshape(-1)
#                 prob = enc_target1.inverse_transform(prob)[0]
#                 pred_target1.append(prob)
#                 cons = target2.argmax().cpu().numpy().reshape(-1)
#                 cons = enc_target2.inverse_transform(cons)[0]
#                 pred_target2.append(cons)
#                 ipc = target3.argmax().cpu().numpy().reshape(-1)
#                 ipc = enc_target3.inverse_transform(ipc)[0]
#                 pred_target3.append(ipc)

######################################################################################################
        probs = ["A", "B", "C", "D", "E"]
        cons = ["I", "II", "III", "IV"]
        ipc = ["df", "pi", "go"]   
        df["Predicted Probs"] = random.choices(probs, k = len(df.values))
        df["Predicted Cons"] =  random.choices(cons, k = len(df.values))
        df["Predicted IPC"] =  random.choices(cons, k = len(df.values))
        return  html.Div([
                html.H5(filename),
                html.H6(datetime.now()),
                html.Hr(),
                dbc.Table.from_dataframe(df, bordered=True, color="success", style={'textAlign': 'center', "background-color" : "#EBE4E1"}),
                html.Hr(),
                html.Div([dbc.Button("Download",
                            download=df.to_csv("Batch Prediction Results.csv"),
                            external_link=True,
                            style={"background-color" : "#73706c", "height": "40px"})]),
                ],style= {"padding": "2rem 1rem"})
                
    else :
        return html.Div([html.Br(), html.Hr(), html.Br() ,html.Br(),
                         html.H2('Please provide file in either ".csv" or ".xls" format.', 
                                 style={'textAlign': 'center', "background-color" : "#DBDBDA"}),
                         html.Br(),html.Hr()])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'), 
              State('upload-data', 'last_modified'))


def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
