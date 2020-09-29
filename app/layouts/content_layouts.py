import dash_html_components as html
import dash_bootstrap_components as dbc


def render_data_description():
    return html.Div([
        get_data_description(),
        get_techniques_description()
    ], className="BgDisplay")

def get_data_description():
    return html.Div([
            html.Div(html.Div("Data Description",
                              className="font-xl bottom16 paddingtop32 text-color")),
            html.Div(html.Div(["The dataset used in this project is ",
                               html.A(
                                   'Anime Dataset with Reviews - MyAnimeList',
                                   href='https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews', target='_blank'),
                               " and it was downloaded from ", html.A(
                                   'Kaggle.', href='https://www.kaggle.com/', target='_blank'),
                               " I decided to use this dataset as I am a big fan of japanese animated series and I wanted to "
                               "apply my skills to something I am passionate about."
                               ], className="font-md  text-color")),
            html.Br(),
            html.Div(
                html.Div("Data Specification", className="font-lg bottom16 text-color")),
            html.Div(html.Div("This dataset contains informations about Anime (16k), Reviews (130k) and Profiles (47k) crawled from "
                              "https://myanimelist.net/ at 05/01/20.",
                              className="font-md  text-color")),
            html.Div(html.Div(children=["The dataset contains 3 files:",
                                        html.P(children=[html.B("animes.csv"), " contains list of anime, with title, title synonyms, "
                                                "genre, duration, rank, populatiry, score, airing date, episodes "
                                                "and many other important data about individual anime providing "
                                                "sufficient information about trends in time about important aspects "
                                                "of anime. Rank is in float format in csv, but it contains only integer "
                                                "value. This is due to NaN values and their representation in pandas."]),
                                        html.P(children=[html.B("profiles.csv"), " contains information about users who watch anime, namely "
                                               "username, birth date, gender, and favorite animes list."]),
                                        html.P(children=[html.B("reviews.csv"), " contains information about reviews users x animes, with text review and scores"])],
                              className="font-md  text-color")),
            html.Br()], className="boxed")

def get_techniques_description():
    return dbc.Row([
            html.Div("Principal techniques applied to extract informations and insights: ",
                     className="font-lg margin-auto bottom16 text-color"),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Div("Data Analysis:",
                             className="font-md bold  text-color"),
                    html.Div("Data Analysis is the process of examining the data available from an \
                            existing information source and collecting statistics or informative summaries about that data.",
                             className="font-md text-color")
                ], style={"height": "100%"}, className="radius12 padding16 BgDisplay2"),
                    width={"size": 12, "offset": 0}, md={"size": 6, "offset": 3}, lg={"size": 4, "offset": 0},
                    className="bottom32"
                ),
                dbc.Col(html.Div([
                    html.Div(
                        "Sentiment Analysis:", className="font-md bold text-color"),
                    html.Div("Sentiment Analysis refers to the use of natural language processing to systematically identify, "
                             "extract, quantify, and study affective states and subjective information. "
                             "A basic task in sentiment analysis is classifying the polarity of a given text - whether the text "
                             "is positive, negative or neutral.",
                             className="font-md text-color")
                ], style={"height": "100%"}, className="radius12 padding16 BgDisplay2"),
                    width={"size": 12, "offset": 0}, md={"size": 6, "offset": 0}, lg={"size": 4, "offset": 0},
                    className="bottom32"
                ),
                dbc.Col(html.Div([
                    html.Div("Recomendation System:",
                             className="font-md bold text-color"),
                    html.Div("A recommender system is a subclass of information filtering system that seeks to predict the "
                             "'rating' or 'preference' a user would give to an item.", className="font-md text-color")
                ], style={"height": "100%"}, className="radius12 padding16 BgDisplay2"),
                    width={"size": 12, "offset": 0}, md={"size": 6, "offset": 0}, lg={"size": 4, "offset": 0},
                    className="bottom32"
                ),
            ])
        ], className="boxed")


def render_graph_2():
    return html.Div('Bubbacchiella')