#***rename to app.py inorder to run***

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv("hotel_bookings.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
                html.Label('Enter number of rooms: '),
                dcc.Input(id='input-1-submit', type='text', placeholder='Enter a number'),
                html.Br(),
                html.Label('Enter the nightly fee: '),
                dcc.Input(id='input-2-submit', type='text', placeholder='Enter a number'),
                html.Br(),html.Br(),
                html.Button('Submit', id='btn-submit'),
                html.Br(),
                html.Hr(),
                html.Label('Recommended spending (per month): '),
                html.Div(id='output-submit'),
                html.Br(), html.Hr()
            ])

@app.callback(Output('output-submit', 'children'),
                [Input('btn-submit', 'n_clicks')],
                [State('input-1-submit', 'value'),State('input-2-submit', 'value')])
def update_output(clicked, input1, input2):
    if clicked:
        #return bills, supplies, maintenance, totalLabor, totalSpending
        a, b, c, d, e = calculator(int(input1), int(input2))
        return 'Bills: ' + str(a) + ', Supplies: ' + str(b) + ', Maintenance: ' + str(c) + ', Total labor: ' + str(d) + ', Total spending: ' + str(e)

def calculator(numRooms, nightlyRate):
    revenue = nightlyRate * numRooms * 30 * .65  # average of 65% capacity - 30 days

    # ---spending---
    # labor, maintenance, bills, supplies

    housekeepers = 0
    housekeeperWage = 13
    clerks = 0
    clerkWage = 12
    managers = 0
    managerWage = 28
    supervisors = 0
    supervisorWage = 21
    security = 0
    securityWage = 16
    kitchen = 0
    kitchenWage = 11
    misc = 0
    miscWage = 15

    bills = 0
    supplies = 0
    maintenance = 0

    if numRooms < 10:
        housekeepers = 2
        clerks = 2
        managers = 1
        supervisors = 1
        security = 0
        kitchen = 2
        misc = 0
        bills = 2000
        supplies = 1000
        maintenance = 2000

    elif numRooms < 25 and numRooms >= 10:
        housekeepers = 5
        clerks = 2
        managers = 1
        supervisors = 1
        security = 0
        kitchen = 4
        misc = 1
        bills = 4000
        supplies = 2000
        maintenance = 4000
    elif numRooms < 50 and numRooms >= 25:
        housekeepers = 10
        clerks = 4
        managers = 1
        supervisors = 1
        security = 1
        kitchen = 4
        misc = 3
        bills = 8000
        supplies = 4000
        maintenance = 8000
    elif numRooms < 75 and numRooms >= 50:
        housekeepers = 15
        clerks = 5
        managers = 1
        supervisors = 2
        security = 2
        kitchen = 8
        misc = 5
        bills = 16000
        supplies = 8000
        maintenance = 16000
    elif numRooms >= 75:
        housekeepers = 20
        clerks = 5
        managers = 2
        supervisors = 3
        security = 4
        kitchen = 10
        misc = 10
        bills = 32000
        supplies = 16000
        maintenance = 32000

    # spending outputs
    hkCost = housekeepers * housekeeperWage * 160
    clerkCost = clerks * clerkWage * 160
    mngrCost = managers * managerWage * 160
    spCost = supervisors * supervisorWage * 160
    secCost = security * securityWage * 160
    kitchenCost = kitchen * kitchenWage * 160
    miscCost = misc * miscWage * 160
    totalLabor = hkCost + clerkCost + mngrCost + spCost + secCost + kitchenCost + miscCost
    totalSpending = totalLabor + bills + supplies + maintenance

    return bills, supplies, maintenance, totalLabor, totalSpending


if __name__ == '__main__':
    app.run_server(debug=True)