from cProfile import label
from pydoc import classname
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import Dash, dash_table, Input, Output, callback
import dash_bio as dashbio

# ------------------------------------------------------------------------------
# make_ FUNCTIONS
# These functions are callse only once to create the backbone of the graphical 
# plots and elements. Then each element is updated based on callbacks that call 
# "update_" functions. 
# ------------------------------------------------------------------------------

def make_Subtitle(string):
    """
    Makes a subtitle with a line underneath to divide sections
    """
    subtitle = html.Div([
        html.H2(string,
            className="mt-2 mb-0 fw-bolder"),
        html.Hr(className="my-0")   
    ])
    return subtitle

def make_NavBar():
    """
    Makes the navigation bar
    """
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink('About', href='/about')),
            dbc.NavItem(dbc.NavLink('Introduction', href='/introduction')),
            dbc.NavItem(dbc.NavLink('Database', href='/database')),
            dbc.NavItem(dbc.NavLink('Visualization', href='/visualization')),
        ],
        brand='Spatial Metabolomics Visualization Web',
        brand_href='/about',
        color='primary',
        fixed='top',
        dark=True,
        style={'height':'40px'},
        className=''
    )
    return navbar

def make_IntroHeader(idFunc):
    """
    Makes the header for the WFA page
    """
    # Main Title
    header = html.Div(
        dbc.Container([
            html.Div([
                html.H2("Spatial Metabolomics for Gastric Cancer", className="display-4"),
            ], className='d-flex justify-content-between align-items-center mb-0'),
            
            html.Hr(className="mt-0 mb-1"),
            html.Div([
                html.P("Metabolic biomarker discovery for gastric cancer using mass spectrometry imaging."),
                html.H4(id=idFunc('moreInfoIcon'), className="fa-solid fa-book-open ms-3 mt-1 primary")
            ], className='d-flex mb-0'),
            dbc.Collapse(
                html.Div([
                    "This page shows introduction to the project: ",
                    "metabolic biomarker discovery by MSI.",
                    # html.Br(),"For detailed information of the procedure, see ",
                    # html.A("here", href="https://academic.oup.com/bib/article/24/4/bbad189/7176311", target="_blank")
                ]),
                id=idFunc("moreInfoCollapse"),
                is_open=False,
            ),
            dbc.Tooltip("More info.", target=idFunc("moreInfoIcon"), className='ms-1')
            ],
            fluid=True,
            className="py-1 bg-light rounded-3",
        ),
        className="p-0 my-1",
    )
    return header

def make_AboutHeader(idFunc):
    """
    Makes the header for the WFA page
    """
    # Main Title
    header = html.Div(
        dbc.Container([
            html.Div([
                html.H2("Welcome to Spatial Metabolomics Visualization Web",         
                        style={'fontSize': '48px'} , # Change the font size here
                        className="display-4"),
            ], className='d-flex justify-content-between align-items-center mb-0'),
            html.Hr(className="mt-0 mb-1"),
            html.Div([
                html.P("Introduction to the project and author."),
                html.H4(id=idFunc('moreInfoIcon'), className="fa-solid fa-book-open ms-3 mt-1 primary")
            ], className='d-flex mb-0'),
            # dbc.Collapse(
            #     html.Div([
            #         "This page shows introduction to the project: ",
            #         "metabolic biomarker discovery by MSI.",
            #         # html.Br(),"For detailed information of the procedure, see ",
            #         # html.A("here", href="https://academic.oup.com/bib/article/24/4/bbad189/7176311", target="_blank")
            #     ]),
            #     id=idFunc("moreInfoCollapse"),
            #     is_open=False,
            # ),
            # dbc.Tooltip("More info.", target=idFunc("moreInfoIcon"), className='ms-1')
            ],
            fluid=True,
            className="py-1 bg-light rounded-3",
        ),
        className="p-0 my-1",
    )
    return header

def make_MPIDBHeader(idFunc):
    """
    Makes the header for the PV page
    """
    # Main Title
    header = html.Div(
        dbc.Container([
            html.Div([
                html.H2("Metabolite-protein-disease association database", className="display-4"),
                # dbc.Button("Cite", id=idFunc("btn_citeHeader"),color="success", outline=True)
            ], className='d-flex justify-content-between align-items-center mb-0'),
            
            html.Hr(className="mt-0 mb-1"),
            html.Div([
                html.P("An atlas for metabolite-protein-disease association."),
                html.H4(id=idFunc('moreInfoIcon'), className="fa-solid fa-book-open ms-3 mt-1 primary")
            ], className='d-flex mb-0'),
            dbc.Collapse(
                html.Div([
                    "This page shows the details of metabolite and protein information that are associated with gastric cancer.",
                    html.Br(),"For detailed information of the procedure, see ",
                    html.A("here", href="", target="_blank")
                ]),
                id=idFunc("moreInfoCollapse"),
                is_open=False,
            ),
            dbc.Tooltip("More info.", target=idFunc("moreInfoIcon"), className='ms-1')
            ],
            fluid=True,
            className="py-1 bg-light rounded-3",
        ),
        className="p-0 my-1",
    )
    return header

def make_DockingHeader(idFunc):
    """
    Makes the header for the Genes page
    """
    # Main Title
    header = html.Div(
        dbc.Container([
            html.Div([
                html.H2("Visualization of MPI Prediction by Molecular Docking", className="display-4"),
                dbc.Button("Cite", id=idFunc("btn_citeHeader"),color="success", outline=True)
            ], className='d-flex justify-content-between align-items-center mb-0'),
            
            html.Hr(className="mt-0 mb-1"),
            html.Div([
                html.P("Explore MPI results by molecular docking"),
                html.H4(id=idFunc('moreInfoIcon'), className="fa-solid fa-book-open ms-3 mt-1 primary")
            ], className='d-flex mb-0'),
            dbc.Collapse(
                html.Div([
                    "This page shows interactive visualizations of MPI results.",
                    html.Br(), 
                    html.Br(),"For detailed information of the procedure, see ",
                    html.A("here", href="https://academic.oup.com/bib/article/24/4/bbad189/7176311", target="_blank")
                ]),
                id=idFunc("moreInfoCollapse"),
                is_open=False,
            ),
            dbc.Tooltip("More info.", target=idFunc("moreInfoIcon"), className='ms-1')
            ],
            fluid=True,
            className="py-1 bg-light rounded-3",
        ),
        className="p-0 my-1",
    )
    return header

def make_introductionText():
    """
    Makes the introduction text for the introduction page
    """
    text = html.Div([
        html.P("Gastric cancer, commonly referred to as stomach cancer, is a significant global health concern and one of the leading causes of cancer-related mortality worldwide. "
            "The disease is notorious for its late diagnosis due to the vagueness of early symptoms, which frequently leads to poor prognosis and high mortality rates. Current therapeutic strategies include surgical resection, chemotherapy, and radiation therapy, but outcomes remain suboptimal, especially in advanced stages. Thus, there is a critical need for early detection and effective therapeutic targets. "
            "Spatial metabolomics is an emerging field that combines traditional metabolomic techniques with spatially resolved analysis to map the distribution and concentration of metabolites directly within tissue samples. This approach is particularly powerful in cancer research, where tumor heterogeneity plays a crucial role in disease progression and response to treatment. In gastric cancer, spatial metabolomics allows for the detailed examination of metabolic alterations at both the macroscopic level (across different regions of the tumor and surrounding tissues) and microscopic level (within specific cell types or microenvironments). "
               ),
        dbc.Card(
        [
            dbc.CardImg(src="/assets/workflow.png", top=True),
            dbc.CardBody(
                html.P("Gastric cancer and spatial metabolomics", className="card-text")
            ),
        ],
        style={"txt_align": "justify"},
        ),
    ],        
    style={"txt_align": "justify",
         },)
    return text


def make_aboutText():
    """
    Makes the introduction text for the introduction page
    """
    text = html.Div([
        html.P(
            "Hi! I’m Flora Wang, a high school student in Vancouver passionate about cancer research. This website is a part of my research project: mass spectrometry imaging metabolomics reveals the spatial heterogeneity in gastric cancer. "
            "I am interested in gastric cancer in particular because of my Asian heritage, as I discovered that Asian countries are affected by GC by a disproportionately high amount as compared to western countries. As well, many relatives on my mom’s side of the family, including my mom, have been diagnosed with gastrointestinal illnesses such as intestinal metaplasia which are precursors of gastric cancer. "
            "Here in Canada, I’ve witnessed with first-hand experience how time-consuming the healthcare process can be. My mom took more than a year, from start to finish, to get diagnosed with intestinal metaplasia. This made me concerned for the status quo of gastric patients, as a year of time could mean the difference between life and death for early-stage gastric cancer patients. "
            "Moreover, cancer has been depicted by the media as this insurmountable obstacle that is almost equivalent to death. I, as an avid consumer of TV shows since a young age, was also influenced by this stereotype. However, as I grew up to become interested in biomedical sciences, I slowly realized that this stereotype isn’t true, and that there has been significant progress made on the journey of combating cancer. "
            "Because of this and my wish to help gastric patients to reach a diagnosis with better efficiency, I became determined to learn more and innovate new perspectives about this illness, hence this project."
        ),
        html.P(
            "My research uses mass spectrometry imaging of metabolites, a newly emerging field of study, to shed light on novel biomarker discoveries that could aid in understanding the underlying mechanisms of GC, therefore leading to pivotal early diagnosis and targeted drug discovery as well. "
            "This quick, unsupervised computational pipeline that I developed which processes mass spectrometry imaging data provides fast results from blood samples, speeding up the timeframe needed between sample collection and confirming diagnosis. "
            "I hope that my own efforts and passion into this project can maximize the efficient utilization of public resources and spread to everyone in need."
        ),
        html.Video(
            controls=True,
            id='my-video',
            src='/assets/demo.MOV',  # Path to your video file
            autoPlay=False,
            loop=False,
            width='100%'
        ),
        html.P("Navigate this website:"),
        html.Ul([
            html.Li([
                html.I(className='fas fa-info-circle', style={'margin-right': '10px'}),
                html.P([
                    html.Strong("This Web Server"), 
                    " aims to inform and spread awareness about the new field of spatial metabolomics, and how it can be used to enhance diagnosis and treatment of gastric cancer."
                ])
            ], style={'display': 'flex', 'align-items': 'center'}),
            html.Li([
                html.I(className='fas fa-book-open', style={'margin-right': '10px'}),
                html.P([
                    html.Strong("The Introduction"), 
                    " page provides background information on gastric cancer, the caveats of current treatment methods, as well as an introduction to the role metabolomics play in cancer research. It also includes a flowchart of the methodology of my research project."
                ])
            ], style={'display': 'flex', 'align-items': 'center'}),
            html.Li([
                html.I(className='fas fa-database', style={'margin-right': '10px'}),
                html.P([
                    html.Strong("The Database"), 
                    " page is an atlas that shows the metabolites and proteins that are associated with gastric cancer."
                ])
            ], style={'display': 'flex', 'align-items': 'center'}),
            html.Li([
                html.I(className='fas fa-chart-pie', style={'margin-right': '10px'}),
                html.P([
                    html.Strong("The Visualization"), 
                    " page demonstrates the distribution of metabolites with respect to the tumoral space in gastric cancer. Users can input the m/z value of any metabolite within the database, and the visualization webpage can provide real-time visualization feedback of that particular metabolite's spatial and density distribution within the tumor."
                ])
            ], style={'display': 'flex', 'align-items': 'center'})
        ])
    ],
        style={"txt_align": "justify",
        },)
    return text

import pandas as pd

def make_DatabaseInfo(idFunc,df):
    database = html.Div([
        html.H6(" ", className='my-1'),
        dash_table.DataTable(
        df.to_dict('records'),
        [{"name": i, "id": i} for i in df.columns],
        sort_action="native",
        sort_mode="multi",
        filter_action="native",
        filter_options={"placeholder_text": "Filter column..."},
        page_size=20,
        style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
        'font-family': "sans-serif",
        'textAlign': 'left',
        },
        tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('records')
        ],
        tooltip_duration=2000,
        style_table={'overflowX': 'auto',
                     'font-family': "sans-serif"},)  
    ])
    
    return database


def make_MSIHeader(idFunc):
    """
    Makes the header for the WFA page
    """
    # Main Title
    header = html.Div(
        dbc.Container([
            html.Div([
                html.H2("Spatial Metabolomics Data Visualization", className="display-4"),
                ], className='d-flex justify-content-between align-items-center mb-0'
            ),
            html.Hr(className="mt-0 mb-1"),
            html.Div([
                html.P("Explore the relationship between metabolites and gastric cancer."),
                html.H4(id=idFunc('moreInfoIcon'), className="fa-solid fa-book-open ms-3 mt-1 primary")
            ], className='d-flex mb-0'),
            dbc.Collapse(
                html.Div([
                    "This page shows the visualization of spatial metabolomics data of gastric cancer.",
                    html.Br(), 
                    html.Br(),"For detailed information of the procedure, see ",
                    html.A("here", href="", target="_blank")
                ]),
                id=idFunc("moreInfoCollapse"),
                is_open=False,
            ),
            dbc.Tooltip("More info.", target=idFunc("moreInfoIcon"), className='ms-1')
            ],
            fluid=True,
            className="py-1 bg-light rounded-3",
        ),
        className="p-0 my-1",
    )
    return header

def make_AreasChecklist(idFunc,coarseDict):
    checklist = dbc.Checklist(
        id=idFunc('chklst_areasCorr'),
        options=coarseDict,
        value=[x['value'] for x in coarseDict],
        inline=True,
        className='ms-5'
    )
    return checklist


def make_MSISelectionMenu(idFunc, genome_dict):
    """
    Makes the left-side menu with dropdowns for the histogram of the multiple staining metrics
    """
    menu = html.Div([
        html.H6(["Select a sample"],className='my-1'),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id=idFunc('drpD_Sample_Select'),
                    options=list(genome_dict.keys()),
                    value='Control', # Default ID for Aggrecan
                    multi=False,
                    clearable=False,
                )],
                style={'flex-grow':'1'},
            ),
            html.Div([
                dbc.Button([html.I(className="fa-solid fa-info")],id=idFunc('btn_info'))], 
            )],
            className='mt-1 mb-1', 
            style={'display':'flex','flex-direction':'row', 'column-gap':'5px'}
        ),
        html.Br(),

        html.H6(["Input a m/z value"],className='my-1'),
        dcc.Input(
            id=idFunc('input-mz'),
            type='number',
            value=123.14,
            className='my-1 mb-3'
        ),
        html.Br(),
        dbc.Button('Submit', id=idFunc('submit-button'), n_clicks=0),
        # TOOLTIPS
        dbc.Tooltip("Select the sample that you want to perform molecular abundance visualization on spatial metabolomics data.",
            target=idFunc("drpD_genome_Select"),placement="right"
        ),
        dbc.Tooltip("Input the m/z value that you want to visualize.",
            target=idFunc("input-mz"),placement="right"

        ),])
    return menu

def MPI_CollapsableTable(idFunc):
    """
    Makes the collapsable tabular data section
    """
    collapsTable = html.Div([
        dbc.Button("Show MPI Prediction Result",
            id=idFunc("btn_openTabMPI"),
            className="mb-1",
            color="primary",
        ),
        dbc.Collapse(
            id=idFunc("collps_MPI_Tab"),
            is_open=False,
        )],
        className='mt-3'
    )
    return collapsTable

def make_MPIVisualizationMenu(idFunc, mets_dict, protein_dict):
    """
    Makes the left-side menu with dropdowns for the histogram of the multiple staining metrics
    """
    menu = html.Div([
        html.H6(["Select a Metabolite ID:"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_metSelect'),
            options=list(mets_dict.keys()),
            value='DB0000177', # Default ID for Aggrecan
            multi=False,
            clearable=False,
        ),
        html.H6(["\n\n\n"],className='my-1'),
        html.H6(["Select a Protein:"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_ProteinSelect'),
            options = list(protein_dict.keys()),
            value='P07357', # Defaults to Isocortex
            multi = False,
            clearable=False,
            className='my-1 mb-3'
        ),
        dbc.Button('Submit', id=idFunc('dock-button'), n_clicks=0),
        dcc.Store(id=idFunc('pdb'),storage_type='local',data={}),
        dcc.Store(id=idFunc('poses'),storage_type='local',data={}),
        # TOOLTIPS
        dbc.Tooltip("Select the metabolite that interact protein with.",
            target=idFunc("drpD_metSelect"),placement="right"
        ),
        dbc.Tooltip("Select the protein to use for MPI visualization by molecular docking.",target=idFunc("drpD_ProteinSelect"),placement="right"),
    ])
    return menu


def make_InteractionSelectionMenu(idFunc):
    """
    Makes the left-side menu of the correlation plot in the interaction page
    """

    # Create a list of dicts for the dropdown of WFA vs PV
    wfaPvDictList = [{'label':'WFA', 'value':'wfa'},{'label':'Parvalbumin', 'value':'pv'}]

    # Create a list of dicts for the dropdown of the different metrics
    metricsDictList = [
        {'label':'Cell Energy','value':'energy'},
        {'label':'Diffuse Fluorescence','value':'diffuseFluo'},
        {'label':'Cell Density','value':'density'},
        {'label':'Cell Intensity','value':'intensity'},
    ]

    menu = html.Div([

        # X AXIS
        dbc.Row([
            html.Div([
                html.H4("X axis", className='my-1 mt-2'),
                html.H6("Select a staining", className='mt-3 mb-1'),
                dcc.Dropdown(
                    id=idFunc('drpD_xStaining'),
                    options = wfaPvDictList,
                    value='wfa',
                    multi = False,
                    clearable=False,
                    className=''
                ),
                html.H6("Select a metric", className='mt-3 mb-1'),
                dcc.Dropdown(
                    id=idFunc('drpD_xMetric'),
                    options = metricsDictList,
                    value='energy',
                    multi = False,
                    clearable=False,
                    className='mb-2'
                ),

            ],className='my-3 border border-light rounded-3')
        ]),

        # Y AXIS
        dbc.Row([
            html.Div([
                html.H4("Y axis", className='my-1 mt-2'),
                html.H6("Select a staining", className='mt-3 mb-1'),
                dcc.Dropdown(
                    id=idFunc('drpD_yStaining'),
                    options = wfaPvDictList,
                    value='pv',
                    multi = False,
                    clearable=False,
                    className=''
                ),
                html.H6("Select a metric", className='mt-3 mb-1'),
                dcc.Dropdown(
                    id=idFunc('drpD_yMetric'),
                    options = metricsDictList,
                    value='energy',
                    multi = False,
                    clearable=False,
                    className='mb-2'
                ),

            ],className='my-3 border border-light rounded-3')
        ]),
        dbc.Row([
            html.Div([
            # dbc.Button("Reset", id="btn-reset", color="primary", className="my-1"),
            dbc.Switch(
                label="Z-Score",
                value=False,
                id=idFunc("switch_zScore"),
                # class_name="mt-1"
                )],
            className="d-flex"
            )
        ])
    ])
    return menu

def make_MetricsHistogramSelectionMenu(idFunc, coarseDict, midDict, fineDict, staining='wfa'):
    """
    Makes the left-side menu with dropdowns for the histogram of the multiple staining metrics
    """
    menu = html.Div([
        html.H6(["Select a metric to show:"],className='my-1'),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id=idFunc('drpD_histogMetric'),
                    options=getMetricsLabels(staining=staining),
                    value='energy',
                    multi = False,
                    clearable=False,
                )],
                style={'flex-grow':'1'},
            ),
            html.Div([
                dbc.Button([html.I(className="fa-solid fa-info")],id=idFunc('btn_info'))], 
            )],
            className='mt-1 mb-5', 
            style={'display':'flex','flex-direction':'row', 'column-gap':'5px'}
        ),
        html.H6(["Select a major brain subdivision:"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_majorSubd'),
            options = coarseDict,
            value=315, # Defaults to Isocortex
            multi = False,
            className='my-1 mb-3'
        ),
        html.H6(["Add ",html.B("coarse-ontology")," region(s):"], className='my-1'),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id=idFunc('drpD_addCoarse'),
                    options = coarseDict,
                    multi = True,
                )],
                style={'flex-grow':'1'},
            ),
            html.Div([
                dbc.Button("All",id=idFunc('btn_allMajorDiff'))], 
            )],
            className='mt-1 mb-3', 
            style={'display':'flex','flex-direction':'row', 'column-gap':'5px'}
        ),
        html.H6(["Add ", html.B("mid-ontology"), " region(s):"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_addMid'),
            options = midDict,
            multi = True,
            className="mt-1 mb-3"
        ),
        html.H6(["Add ", html.B("fine-ontology"), " region(s):"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_addFine'),
            options = fineDict,
            multi = True,
            className="mt-1 mb-3"
        ),
        html.Div([
            # dbc.Button("Reset", id="btn-reset", color="primary", className="my-1"),
            dbc.Switch(
                label="Sort regions",
                value=False,
                id=idFunc("switch_sortDiff"),
                # class_name="mt-1"
                )],
            className="d-flex"
        ),

        # TOOLTIPS
        dbc.Tooltip("Add all the 12 major brain subdivisions.", target=idFunc("btn_allMajorDiff")),
        dbc.Tooltip(["Sort on intensity.", html.Br(), "Otherwise, sorted on region ontology."],
            target=idFunc("switch_sortDiff"),placement='bottom'
        ),
        dbc.Tooltip("Add all the regions of a selected major brain subdivision",
            target=idFunc("drpD_majorSubd"),placement="right"
        ),
        dbc.Tooltip("Major brain subdivisions",target=idFunc("drpD_addCoarse"),placement="right"),
        dbc.Tooltip("Regions at single-area level",target=idFunc("drpD_addMid"),placement="right"),
        dbc.Tooltip("Regions at single-layer level",target=idFunc("drpD_addFine"),placement="right"),
    ])
    return menu



def make_ColocalizationHistogramSelectionMenu(idFunc, coarseDict, midDict, fineDict):
    """
    Makes the left-side menu with dropdowns for the histogram of the multiple staining metrics
    """
    menu = html.Div([
        html.H6(["Select a colocalization metric:"],className='my-1'),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id=idFunc('drpD_Metric'),
                    options=[
                        {'label':'Percentage of PV-positive PNNs','value':'pvPositive_pnn'},
                        {'label':'Percentage of WFA-positive PV cells','value':'wfaPositive_pv'},
                    ],
                    value='pvPositive_pnn',
                    multi = False,
                    clearable=False,
                )],
                style={'flex-grow':'1'},
            ),
            html.Div([
                dbc.Button([html.I(className="fa-solid fa-info")],id=idFunc('btn_info'))], 
            )],
            className='mt-1 mb-5', 
            style={'display':'flex','flex-direction':'row', 'column-gap':'5px'}
        ),
        html.H6(["Select a major brain subdivision:"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_majorSubd'),
            options = coarseDict,
            value=315, # Defaults to Isocortex
            multi = False,
            className='my-1 mb-3'
        ),
        html.H6(["Add ",html.B("coarse-ontology")," region(s):"], className='my-1'),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id=idFunc('drpD_addCoarse'),
                    options = coarseDict,
                    multi = True,
                )],
                style={'flex-grow':'1'},
            ),
            html.Div([
                dbc.Button("All",id=idFunc('btn_allMajorDiff'))], 
            )],
            className='mt-1 mb-3', 
            style={'display':'flex','flex-direction':'row', 'column-gap':'5px'}
        ),
        html.H6(["Add ", html.B("mid-ontology"), " region(s):"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_addMid'),
            options = midDict,
            multi = True,
            className="mt-1 mb-3"
        ),
        html.H6(["Add ", html.B("fine-ontology"), " region(s):"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_addFine'),
            options = fineDict,
            multi = True,
            className="mt-1 mb-3"
        ),
        html.Div([
            # dbc.Button("Reset", id="btn-reset", color="primary", className="my-1"),
            dbc.Switch(
                label="Sort regions",
                value=False,
                id=idFunc("switch_sortDiff"),
                # class_name="mt-1"
                )],
            className="d-flex"
        ),

        # TOOLTIPS
        dbc.Tooltip("Add all the 12 major brain subdivisions.", target=idFunc("btn_allMajorDiff")),
        dbc.Tooltip(["Sort in descending order.", html.Br(), "Otherwise, sorted on region ontology."],
            target=idFunc("switch_sortDiff"),placement='bottom'
        ),
        dbc.Tooltip("Add all the regions of a selected major brain subdivision",
            target=idFunc("drpD_majorSubd"),placement="right"
        ),
        dbc.Tooltip("Major brain subdivisions",target=idFunc("drpD_addCoarse"),placement="right"),
        dbc.Tooltip("Regions at single-area level",target=idFunc("drpD_addMid"),placement="right"),
        dbc.Tooltip("Regions at single-layer level",target=idFunc("drpD_addFine"),placement="right"),
    ])
    return menu

def make_GeneCorrSelectionMenu(idFunc, genesDf):
    """
    Makes the left-side menu with dropdowns for the histogram of the multiple staining metrics
    """
    menu = html.Div([
        html.H6(["Select a gene ID:"],className='my-1'),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id=idFunc('drpD_geneSelect'),
                    options=getGenesLabels(genesDf),
                    value=11382, # Default ID for Aggrecan
                    multi=False,
                    clearable=False,
                )],
                style={'flex-grow':'1'},
            ),

            html.Div([
                dbc.Button([html.I(className="fa-solid fa-info")],id=idFunc('btn_info'))], 
            )],
            className='mt-1 mb-1', 
            style={'display':'flex','flex-direction':'row', 'column-gap':'5px'}
        ),

        html.Div([
        dbc.Button("Open Gene Info",
            id=idFunc("btn_openTabDiffuse"),
            className="mb-1",
            size='sm',
            outline=True,
            color="primary",
        ),
        dbc.Collapse(
            id=idFunc("collps_Tab"),
            is_open=False,
        )],className='mt-3 mb-5'),

        html.H6(["Correlation with:"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_metricSelector'),
            options = getMetricsForGenesLabels(),
            value='wfa_energy', # Defaults to Isocortex
            multi = False,
            clearable=False,
            className='my-1 mb-3'
        ),

        # TOOLTIPS
        dbc.Tooltip("Select the gene that you want to correlate staining metrics with.",
            target=idFunc("drpD_geneSelect"),placement="right"
        ),
        dbc.Tooltip("Select what staining metric to use for correlation.",target=idFunc("drpD_metricSelector"),placement="right"),
    ])
    return menu

def make_CollapsableTable(idFunc):
    """
    Makes the collapsable tabular data section
    """
    collapsTable = html.Div([
        dbc.Button("Open Tabular Data",
            id=idFunc("btn_openTabDiffuse"),
            className="mb-1",
            color="primary",
        ),
        dbc.Collapse(
            id=idFunc("collps_Tab"),
            is_open=False,
        )],
        className='mt-3'
    )
    return collapsTable

def make_AnatomicalExplorerSelectionMenu(idFunc, staining='wfa'):
    """
    Makes the layout for the left-side selection menu of the anatomical explorer
    """
    menu = html.Div([
        html.H6(["Select a metric to show:"],className='my-1'),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id=idFunc('drpD_anatomMetric'),
                    options= getMetricsLabels(staining=staining),
                    value='energy',
                    multi = False,
                    clearable=False,
                )],
                style={'flex-grow':'1'},
            ),
            html.Div([
                dbc.Button([html.I(className="fa-solid fa-info")],id=idFunc('btn_info_anat'))], 
            )],
            className='mt-1 mb-3', 
            style={'display':'flex','flex-direction':'row', 'column-gap':'5px'}
        ),

        html.H6(["Colormap:"],className='my-1'),
        dcc.Dropdown(
            id=idFunc('drpD_anatomCmap'),
            options = colormapDictListDropdown(),
            value='PuBu' if staining=='wfa' else 'Reds',
            multi = False,
            clearable=False,
            className="mt-1 mb-3"
        ),

        html.H6(["Antero-Posterior Axis:"],className='mt-5 mb-1'),
        dcc.Slider(0, 34, 1, value=10, id=idFunc('slider_ap'),
            marks={0:'Anterior',34:'Posterior'},
        ),

        # TOOLTIPS
        dbc.Tooltip("Visualization colormap.", target=idFunc("drpD_anatomCmap")),
        dbc.Tooltip("Set minimum and maximum values.", target=idFunc("slider_clims")),
    ])
    return menu

def make_CitationOffCanvas(idFunc):
    """
    Makes the layout for the offcanvas menu for citations
    """
    offcanvas = dbc.Offcanvas(
        html.P([
            "If you found this web server to be useful in your research, please consider ", 
            html.B("citing us."),
            html.Br(),
            dbc.Card(
            [
                dbc.CardImg(
                    src="/assets/network.jpg",
                    top=True,
                    style={"opacity": 0.4},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody(
                        [
                            html.H4("Briefings in bioinformatics", className="card-title"),
                            html.P(
                                "Check out our method paper here!",
                                className="card-text",
                            ),
                            dcc.Link([dbc.Button("Go to Paper", color="primary")],
                                href="https://academic.oup.com/bib/article/24/4/bbad189/7176311",
                                target="_blank"),
                            
                        ],
                    ),
                ),
            ],
            style={"width": "18rem"},className='mt-5'),
            make_CC_licenseBanner(idFunc),
        ]),
        
        id=idFunc("offCanv_cite"),
        title="Cite us",
        is_open=False,
    )
    return offcanvas

def make_AboutUsOffCanvas(idFunc):
    offcanvas = dbc.Offcanvas(
        html.P([
            "This work was produced in Cheng Wang's Lab thanks to the support of the following fundings: ",
            html.Br(),
            dbc.ListGroup([
                dbc.ListGroupItem(
                    html.Div([
                        "National Natural Science Foundation of China",
                        html.A(className="fa-solid fa-arrow-up-right-from-square px-3", href='https://www.nsfc.gov.cn/english/site_1/index.html', target='_blank')
                    ], className='d-flex w-100 justify-content-between align-items-center'),
                    className='rounded-3 py2'),
                dbc.ListGroupItem(
                    html.Div([
                        "Shandong Natural Science Foundation",
                        html.A(className="fa-solid fa-arrow-up-right-from-square px-3", href='http://kjt.shandong.gov.cn/', target='_blank')
                    ], className='d-flex w-100 justify-content-between align-items-center'),
                    className='rounded-3 py2'),
            ], flush=True, className='mt-5'),
        ]),
        
        id=idFunc("offCanv_abtUs"),
        title="More about us",
        is_open=False,
        placement='end',
    )
    return offcanvas

def make_MetricInfoModal(idFunc):

    diffuseCard = dbc.Card([
        dbc.CardBody([
            html.H5("Diffuse Fluorescence (A.U.)", className="card-title primary"),
            html.P(html.I("'How much staining is there?'")),
            html.Hr(className="mb-1"),
            html.P(["For each mouse, we calculate the ", html.B("average fluorescence"), 
                " intensity across all the pixels belonging to a brain region. " + 
                "Then, we normalize this value dividing it by the average fluorescence intensity " + 
                "of the entire brain."],
                className="card-text")]
        )],
        style={'height':'100%'},
        outline=True,
        color='info',
    )

    densityCard = dbc.Card([
        dbc.CardBody([
            html.H5(["Cell Density (cells/mm", html.Sup(2) ,")"], className="card-title"),
            html.P(html.I("'How many cells/PNNs are there?'")),
            html.Hr(className="mb-1"),
            html.P(["For each mouse, we calculate the ", html.B(["number of cells per mm",html.Sup(2)]), 
                " In a brain region. " + 
                "This value is the cell density."],
                className="card-text")]
        )],
        style={'height':'100%'},
        outline=True,
        color='info',
    )

    intensityCard = dbc.Card([
        dbc.CardBody([
            html.H5("Cell Intensity (A.U.)", className="card-title"),
            html.P(html.I("'How intense are the cells/PNNs here?'")),
            html.Hr(className="mb-1"),
            html.P(["For each cell, we measure the average pixel intesity value (", html.I(["range: 0-1"]), ") of ",
                "all pixels belonging to that cell.", html.Br(), "For each brain region, we compute the ",
                "average of the intensity of all the cells in that region."],
                className="card-text")],        
        )],
        style={'height':'100%'},
        outline=True,
        color='info'
    )

    energyCard = dbc.Card([
        dbc.CardBody([
            html.H5("Cell Energy (A.U.)", className="card-title"),
            html.P(html.I("'What's the overall strenght of cells/PNNs here?'")),
            html.Hr(className="mb-1"),
            html.P(["Can be thought of as a measure of cell density, weighted by intensity. ",html.Br(),
                "For each region, energy is defined as the sum of the cell intensity ",
                "of all the cells in that region, divided by the total surface area ",
                "Then, we normalize this value dividing it by the energy of the entire brain."],
                className="card-text")]
        )],
        style={'height':'100%'},
        outline=True,
        color='info',
    )

    modal = dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Metrics analyzed")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([diffuseCard], width=6),
                    dbc.Col([densityCard]),
                ], className=''),
                dbc.Row([
                    dbc.Col([intensityCard], width=6),
                    dbc.Col([energyCard]),
                ], className='my-3')]
        )],
        size='lg',
        id=idFunc('modal_info')
    )

    return modal

def make_ColocInfoModal(idFunc):

    pvPositivePnnCard = dbc.Card([
        dbc.CardBody([
            html.H5("PV-positive PNNs", className="card-title primary"),
            html.P(html.I("'What's the percentage of PNNs that surround a PV cell?'")),
            html.Hr(className="mb-1"),
            html.P(["For each mouse, we calculate the ", html.B("average fluorescence"), 
                " intensity across all the pixels belonging to a brain region. " + 
                "Then, we normalize this value dividing it by the average fluorescence intensity " + 
                "of the entire brain."],
                className="card-text")]
        )],
        style={'height':'100%'},
        outline=True,
        color='info',
    )

    wfaPositivePvCard = dbc.Card([
        dbc.CardBody([
            html.H5(["Cell Density (cells/mm", html.Sup(2) ,")"], className="card-title"),
            html.P(html.I("'What's the percentage of PV cells that are surrounded by a PNN?''")),
            html.Hr(className="mb-1"),
            html.P(["For each mouse, we calculate the ", html.B(["number of cells per mm",html.Sup(2)]), 
                " In a brain region. " + 
                "This value is the cell density."],
                className="card-text")]
        )],
        style={'height':'100%'},
        outline=True,
        color='info',
    )

    modal = dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Colocalization metrics analyzed")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([pvPositivePnnCard], width=6),
                    dbc.Col([wfaPositivePvCard]),
                ], className='')]
        )],
        size='lg',
        id=idFunc('modal_info')
    )

    return modal

def make_GeneInfoModal(idFunc):

    genesCard = dbc.Card([
        dbc.CardBody([
            # html.H5("Gene ID", className="card-title primary"),
            html.P(html.I("Samples used for metabolic biomarker discovery")),
            html.Hr(className="mb-1"),
            html.P(["Discover the metabolic heterogeniety in gastric cancer by ", html.B("Spatial Metabolomics Data"),'.'],
                className="card-text")
                ]
        )],
        style={'height':'100%'},
        outline=True,
        color='info',
    )

    modal = dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Select a sample")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([genesCard]),
                ], className='')]
        )],
        size='lg',
        id=idFunc('modal_info')
    )

    return modal

def make_CC_licenseBanner(idFunc):
    banner = []

    banner = html.Div([
        html.Hr(className="mt-2 mb-2"),
        # html.P(["Web-app developed by ",
        #     dcc.Link("Cheng Wang",
        #         href="https://scholar.google.com/citations?user=UAZhchQAAAAJ&hl=en",
        #         target="_blank", className="me-3"),
        # "See source code ",
        #     dcc.Link("here",
        #         href="https://github.com/mmetalab/mpi-vgae-web",
        #         target="_blank"),
        # ]),
        html.A([
            html.Img([], alt="Creative Commons License",  
                src="https://i.creativecommons.org/l/by/4.0/88x31.png")], 
            rel="license", href="http://creativecommons.org/licenses/by/4.0/", className="border-width:0 me-2"),
        "This work is licensed under a ",
        html.A(["Creative Commons Attribution 4.0 International License"], rel='license', href="http://creativecommons.org/licenses/by/4.0/")
    ], id=idFunc("licenseBanner"), className='pt-5')
    return banner

# ------------------------------------------------------------------------------
# 
# ------------------------------------------------------------------------------

def colormapDictListDropdown():
    """
    Creates a list of dicts to fill a dropdown to select different colormaps
    """
    cmapDictList = [
        dict(label='Blue',value='PuBu'),
        dict(label='Red',value='Reds'),
        dict(label='Green',value='Greens'),
        dict(label='Gray',value='Greys'),
        dict(label='Viridis',value='viridis'),
        dict(label='Magma',value='magma'),
    ]
    return cmapDictList

def getMetricsLabels(staining='wfa'):
    if staining == 'wfa':
        labels = [
            {'label':'PNN Energy','value':'energy'},
            {'label':'Diffuse Fluorescence','value':'diffuseFluo'},
            {'label':'PNN Density','value':'density'},
            {'label':'PNN Intensity','value':'intensity'},
        ]
    elif staining == 'pv':
        labels = [
            {'label':'PV Energy','value':'energy'},
            {'label':'Diffuse Fluorescence','value':'diffuseFluo'},
            {'label':'PV Density','value':'density'},
            {'label':'PV Intensity','value':'intensity'},
        ]

    return labels

def getGenesLabels(genesDf):
    genesDf = genesDf.sort_values(by='gene_acronym')
    labels = []
    for idx, row in genesDf.iterrows():
        temp = {'label':idx,'value':row['gene_AGEA_id']}
        labels.append(temp)
    return labels

def getMetricsForGenesLabels():
    labels = [
        {'label':'PNN Energy','value':'wfa_energy'},
        {'label':'WFA Diffuse Fluorescnece','value':'wfa_diffuseFluo'},
        {'label':'PV Energy','value':'pv_energy'},
    ]
    return labels