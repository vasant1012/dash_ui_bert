import dash
from dash.dependencies import Input, Output, State
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
from main import app
#import joblib
import random
#import torch
#import config
#import dataset_predict
#from model_predict import EntityModel
import warnings
warnings.filterwarnings('ignore')

# get relative data folder
PATH = pathlib.Path(__file__).parent


layout= html.Div([html.H2("User Input Prediction", className="display-5", style={'textAlign': 'center'}),
            html.Div([html.Br(),
            dbc.Textarea(id='textarea-state-example-title', placeholder = "Title",
            value=''.format(),
            style={'width': '100%', 'height': 80}),
            html.Br(),
            dbc.Textarea(id='textarea-state-example-scenario', placeholder = "Scenario Description",
            value=''.format(),
            style={'width': '100%', 'height': 80}),
            html.Br(),
            dbc.Button('Predict Risk Scenario', id='textarea-state-example-button', n_clicks=0, 
                       style={"background-color" : "#73706c", "height": "40px"})]),
             html.Br(),
            html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})],
            )


@app.callback(
    Output('textarea-state-example-output', 'children'),
    [Input('textarea-state-example-button', 'n_clicks')],
    [State('textarea-state-example-title', 'value'), State('textarea-state-example-scenario', 'value')],
)

def update_output(n_clicks, title, scenario):
    if n_clicks > 0:
        if not title and scenario:
            return "No text entered in text area. Please enter the text in above box."
        else:
#             meta_data = joblib.load('./trained model/meta.bin')
#             enc_target1 = meta_data["enc_target1"]
#             enc_target2 = meta_data["enc_target2"]
#             enc_target3 = meta_data["enc_target3"]

#             num_target1 = len(list(enc_target1.classes_))
#             num_target2 = len(list(enc_target2.classes_))
#             num_target3 = len(list(enc_target3.classes_))

#             data = [[value]]
#             df = pd.DataFrame(data, columns = ['Text'])
#             sentences = df["Text"].values
#             test_dataset = dataset_predict.Dataset(texts=sentences)

#             device = torch.device("cpu")
#             model = EntityModel(num_target1=num_target1, num_target2=num_target2, num_target3=num_target3)
#             model.load_state_dict(torch.load(config.MODEL_PATH))
#             model.to(device)

#             with torch.no_grad():
#                 pred_target1 = []
#                 pred_target2 = []
#                 pred_target3 = []
#                 for data in test_dataset:
#                     for k, v in data.items():
#                         data[k] = v.to(device).unsqueeze(0)
#                     target1, target2, target3 = model(**data)
#                     prob = target1.argmax().cpu().numpy().reshape(-1)
#                     prob = enc_target1.inverse_transform(prob)[0]
#                     pred_target1.append(prob)
#                     cons = target2.argmax().cpu().numpy().reshape(-1)
#                     cons = enc_target2.inverse_transform(cons)[0]
#                     pred_target2.append(cons)
#                     ipc = target3.argmax().cpu().numpy().reshape(-1)
#                     ipc = enc_target3.inverse_transform(ipc)[0]
#                     pred_target3.append(ipc)
 
#########################################################################################################
            data = [[title, scenario]]
            df = pd.DataFrame(data, columns = ['Title', 'Scenario'])
            probs = ["A", "B", "C", "D", "E"]
            cons = ["I", "II", "III", "IV"]
            ipc = ["df", "pi", "go"]
#             df["Probs"] = random.choices(probs, k = 1)
#             df["Cons"] =  random.choices(cons, k = 1)
#             df["IPC"] =  random.choices(ipc, k = 1)
            df["Predicted Probs"] = random.choices(probs, k = 1)
            df["Predicted Cons"] = random.choices(cons, k = 1)
            df["Predicted IPC"] = random.choices(ipc, k = 1) 
            table = dbc.Table.from_dataframe(df, bordered=True, 
                                             style={'textAlign': 'center', "background-color" : "#DBDBDA"})
            return table
#     else:
#         return "Enter the text in text area and click on submit button!"   