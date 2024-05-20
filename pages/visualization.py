from dash import dcc, html, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import base64
import io
from pathlib import Path
import pandas as pd

from utils import dataManager as dm
from utils import layoutFunctions as lf
from utils import callbackFunctions as cf
import pickle

import numpy as np

def mz_to_index(mz,mz_values):
    index = np.argmin(np.abs(mz_values - mz))
    print(f'Index of m/z {mz}: {index}')
    print(f'Closest m/z value: {mz_values[index]}')
    return index

def ion_image(intensity_values, coordinates, mz_values,mz):
    import pandas as pd
    from skimage import exposure

    # Select a specific m/z value (for example, the first m/z value)
    mz_index = mz_to_index(mz,mz_values)
    selected_mz_values = intensity_values[:, mz_index]

    # Create a DataFrame for easier manipulation
    df = pd.DataFrame({
        'x': [coord[0] for coord in coordinates],
        'y': [coord[1] for coord in coordinates],
        'intensity': selected_mz_values
    })

    # Pivot the DataFrame to create a matrix suitable for heatmap
    pivot_table = df.pivot(index='y', columns='x', values='intensity')
    pivot_table.fillna(0, inplace=True)
    # Normalize for visualization
    normalized_image = exposure.equalize_hist(pivot_table.values)

    return normalized_image

# ------------------------------------------------------------------------------
# Initialize utility objects and useful functions
# ------------------------------------------------------------------------------

# id function that helps manage component id names. It pre-pends
# the name of the page to a string so that writing ids specific for each page is easier 
id = cf.id_factory('visualization')          

# Full path of the data folder where to load raw data
dataFolder = Path(__file__).parent.parent.absolute() / 'data'


# ------------------------------------------------------------------------------
# Perform some preprocessing
# ------------------------------------------------------------------------------

genome_dict = {'Control':"Control",
'Case':'Case'}

MSI_data_control = pickle.load(open(dataFolder / 'MSI_data_control.pkl', 'rb'))
MSI_data_case = pickle.load(open(dataFolder / 'MSI_data_case.pkl', 'rb'))

mz = 100
data = MSI_data_case
coordinates, intensity_values_subsampled, mz_values_subsampled = data[0], data[1], data[2]
image = ion_image(intensity_values_subsampled, coordinates, mz_values_subsampled, mz)


# ------------------------------------------------------------------------------
# LAYOUT
# ------------------------------------------------------------------------------


layout = dbc.Container([
    lf.make_CitationOffCanvas(id),
    lf.make_AboutUsOffCanvas(id),
    lf.make_GeneInfoModal(id),
    dbc.Row(lf.make_NavBar()),                           # Navigation Bar
    dbc.Row(lf.make_InteractionHeader(id)),            # Big header
    #
    dbc.Row([lf.make_Subtitle('Molecular Visualization on Spatial Metabolomics Data')]),
    dbc.Row([
        dbc.Col(lf.make_MSISelectionMenu(id, genome_dict),
            xs=12,lg=4, className='mt-5'
        ),
        dbc.Col(
            dbc.Spinner(
                dcc.Graph(
                    figure=cf.make_MSIFigure(image),
                    id=id('mpiPlot'), config={'displaylogo':False}, className='mt-3'),
                color='primary'
            )
        )
    ]),
    html.Br(),
    dbc.Row([lf.make_CC_licenseBanner(id)]),
    dbc.Row([],style={"margin-top": "500px"}),
])


@callback(
    Output(component_id=id('mpiPlot'), component_property='figure'),
    State(component_id=id('mpiPlot'), component_property='figure'),
    Input(component_id=id('submit-button'),component_property='n_clicks'),
    Input(component_id=id('drpD_Sample_Select'),component_property='value'),
    Input(component_id=id('input-mz'),component_property='value'),
)

def update_MSI_Plot(fig,n_clicks,sample,mz):
    if n_clicks > 0:
        if sample == 'Control':
            data = MSI_data_control
        else:
            data = MSI_data_case
        print(mz)
        coordinates, intensity_values_subsampled, mz_values_subsampled = data[0], data[1], data[2]
        image = ion_image(intensity_values_subsampled, coordinates, mz_values_subsampled, mz)
        fig = cf.update_MSIFigure(fig,image)
    return fig

@callback(
    Output(component_id=id('offCanv_cite'), component_property='is_open'),
    Input(component_id=id('btn_citeHeader'),component_property='n_clicks'),
    Input(component_id='citeDropdown', component_property='n_clicks'),
    State(component_id=id('offCanv_cite'), component_property='is_open'),
    prevent_initial_call=True
)
def invertCiteMenuVisibility(n_clicks, n_clicks_dropdown, is_open):
    if n_clicks or n_clicks_dropdown:
        return not is_open
    return is_open


@callback(
    Output(component_id=id('moreInfoCollapse'), component_property='is_open'),
    Input(component_id=id('moreInfoIcon'), component_property='n_clicks'),
    State(component_id=id('moreInfoCollapse'), component_property='is_open'),
    prevent_initial_call=True
)
def invertMoreInfoVisibility(n_clicks, is_open):
    if n_clicks:
            return not is_open
    return is_open


@callback(
    Output(component_id=id('modal_info'), component_property='is_open'),
    Input(component_id=id('btn_info'),component_property='n_clicks'),
    State(component_id=id('modal_info'), component_property='is_open'),
)
def invertModalInfoVisibility(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

@callback(
    Output(component_id=id('offCanv_abtUs'), component_property='is_open'),
    Input(component_id='aboutUsDropdown', component_property='n_clicks'),
    State(component_id=id('offCanv_abtUs'), component_property='is_open'),
    prevent_initial_call=True
)
def invertAboutusMenuVisibility(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open