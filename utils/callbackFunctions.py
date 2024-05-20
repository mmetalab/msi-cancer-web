# from matplotlib.pyplot import axis
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import pandas as pd
import os
import pickle


def make_MSIFigure(ionimage):
    fig = px.imshow(ionimage,aspect="auto")

    # Customize X axis
    fig.update_xaxes(
        title="X axis"
    )
    # Customize Y axis
    fig.update_yaxes(
        title="Y axis"
    )
    fig.update_layout(
            title={
                'text': "MSI visualization",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
                font=dict(family="Sans-serif"))
    
    return fig

def update_MSIFigure(fig, ionimage):
    # # Convert back the figure in a go object

    fig = px.imshow(ionimage,aspect="auto")
    # Customize X axis
    fig.update_xaxes(
        title="X axis"
    )
    # Customize Y axis
    fig.update_yaxes(
        title="Y axis"
    )
    fig.update_layout(
            title={
                'text': "MSI visualization",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
                font=dict(family="Sans-serif"))
    
    return fig

import dash_bio as dashbio
from dash import dcc, html


def id_factory(page: str):
    def func(_id: str):
        """
        Dash pages require each component in the app to have a totally
        unique id for callbacks. This is easy for small apps, but harder for larger 
        apps where there is overlapping functionality on each page. 
        For example, each page might have a div that acts as a trigger for reloading;
        instead of typing "page1-trigger" every time, this function allows you to 
        just use id('trigger') on every page.
        
        How:
            prepends the page to every id passed to it
        Why:
            saves some typing and lowers mental effort
        **Example**
        # SETUP
        from system.utils.utils import id_factory
        id = id_factory('page1') # create the id function for that page
        
        # LAYOUT
        layout = html.Div(
            id=id('main-div')
        )
        # CALLBACKS
        @app.callback(
            Output(id('main-div'),'children'),
            Input(id('main-div'),'style')
        )
        def funct(this):
            ...
        """
        return f"{page}-{_id}"
    return func