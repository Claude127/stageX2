from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# initialisation de l'application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# lecture des donnees
fl = pd.read_csv('claude_csv/projet.csv', parse_dates=['order_date'])

# agreger les donnees par mois et par projet
df = fl.groupby([pd.Grouper(key='order_date', freq='M'), 'poduct_name']).sum().reset_index()
# agreger et sommer les montants par projet
dp = fl.groupby('poduct_name')['Revenue_projet'].sum()

# construction de composants
header_component = html.H1("Visualiser vos données")

# graphe1

cumulfig = go.FigureWidget()

for name, group in df.groupby("poduct_name"):
    cumulfig.add_scatter(
        x=group["order_date"].dt.strftime("%Y %b"),
        y=group["Revenue_projet"],
        mode="lines",
        name=name
    )

cumulfig.update_layout(
    title="Revenus par produit",
    xaxis_title="Date",
    yaxis_title="Revenu (en XAF)",
    xaxis=dict(
        tickformat="%b"
    )
)

# graphe 2

piefig = go.FigureWidget(
    px.pie(
        labels=dp.index,
        values=dp.values,
        names=dp.index
    )
)

piefig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# liste des projets pour le widget Dropdown

projectlist = [
    {"label": name, "value": name} for name in df["poduct_name"].unique()
]
# liste des annees pour le widget dropdown
default_year = 2022
yearlist = [
    {"label": year, "value": year} for year in df["order_date"].dt.year.unique()

]


# callback pour mettre le graphe 1 a jour en fonction du projet selectionne et du l'annee selectionnee

@app.callback(
    Output('graph', 'figure'),
    [Input('list_dropdown', 'value'),
     Input('year_dropdown', 'value')])
def update_figure(projet, year):
    filter_df = df[df["poduct_name"] == projet]
    if year:
        filter_df = filter_df[filter_df["order_date"].dt.year == year]
    cumulfig.update_layout(title=f"Revenus pour le projet {projet}")

    cumulfig.data = []

    for name, group in filter_df.groupby("poduct_name"):
        cumulfig.add_scatter(
            x=group["order_date"].dt.strftime("%Y %b"),
            y=group["Revenue_projet"],
            mode="lines",
            name=name
        )

    return cumulfig


# Callback pour mettre a jour le graphe 2 en fonction de l'annee selectionnee

@app.callback(
    Output('pie_graph', 'figure'),
    [Input('year2_dropdown', 'value')]
)
def update_pie(year2):
    if year2:
        filter_fl = fl[fl["order_date"].dt.year == year2]
    else:
        filter_fl = fl
    dp = filter_fl.groupby('poduct_name')['Revenue_projet'].sum()
    piefig = go.FigureWidget(
        px.pie(
            labels=dp.index,
            values=dp.values,
            names=dp.index
        )
    )
    piefig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    return piefig


# design du layout de l'application
app.layout = html.Div(
    [
        dbc.Row(
            [header_component

             ]
        ),
        dbc.Row(
            [dbc.Col(
                [
                    html.Label('selectionnez un projet'),
                    dcc.Dropdown(
                        id='list_dropdown',
                        options=projectlist,
                        value=df["poduct_name"].iloc[0]
                    ),
                    html.Label('selectionnez une annee'),
                    dcc.Dropdown(
                        id='year_dropdown',
                        options=yearlist,
                        value=default_year
                    ),
                    dcc.Graph(id='graph', figure=cumulfig)
                ]
            ), dbc.Col(
                [html.Label('selectionnez une annee'),
                 dcc.Dropdown(
                     id='year2_dropdown',
                     options=yearlist,
                     value=default_year
                 ),
                 dcc.Graph(id='pie_graph', figure=piefig)
                 ]
            ), dbc.Col()]
        ),
        dbc.Row(
            [dbc.Col(), dbc.Col()]
        ),
    ]
)

# Demarrer l'application
if __name__ == '__main__':
    app.run_server(debug=True)
