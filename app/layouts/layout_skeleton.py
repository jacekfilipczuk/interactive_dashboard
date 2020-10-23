import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

linkedin_profile_link = 'https://www.linkedin.com/in/jacek-filipczuk-53626894'
github_profile_link = 'https://github.com/jacekfilipczuk'


def create_layout_skeleton():
    return html.Div([
        navbar(appname='Dashboard'),
        create_body(),
        create_footer()
    ], style={'margin': '0 auto', 'overflow': 'hidden'})


def navbar(logo="/assets/husky-logo.png", height="35px", appname="PlaceHolder Name"):
    header_style = {
        'background-color': 'rgb(79, 152, 202)',
        'padding': '1.5rem',
        'display': 'inline-block',
        'width': '100%'
    }
    logo_husky = html.Img(
        src=logo,
        className='three columns',
        style={
            'height': 'auto',
            'width': '140px',  # 'padding': 1
            'float': 'left',  # 'position': 'relative'
            'display': 'inline-block'})

    navbar = html.Div(
        [dbc.Container(
            [dbc.Row([
                dbc.Col(html.Div([logo_husky], id='logo_icon'), width=2

                        ),
                dbc.Col(html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    html.Div(
                        "Jacek Filipczuk", className="navbar white font-xl", ),
                    href=linkedin_profile_link, target="_blank"
                ), width=4),
                dbc.Col(dbc.NavbarBrand(
                    appname, className="font-lg text-white"), className="text-right", width=6)


            ],
                style={"align-items": "center", "min-height": "75px"}
            )
            ],
            style={"maxWidth": "1140px"})
        ],
        className="bottom16 navbarColor",
        style=header_style)

    return navbar


def create_footer():
    p = html.Div(
        children=[
            html.Span('Developed By: '),
            html.A('Jacek Filipczuk',
                   style={'text-decoration': 'none', 'color': '#ffffff'},
                   href=linkedin_profile_link, target='_blank')
        ], style={'float': 'right', 'margin-top': '8px',
                  'font-size': '18px', 'color': '#ffffff'}
    )

    span_style = {'horizontal-align': 'right',
                  'padding-left': '1rem',
                  'font-size': '15px',
                  'vertical-align': 'middle'}

    mapbox = html.A(
        children=[
            html.I([], className='fab fa-python'),
            html.Span('Dash Plotly', style=span_style)
        ], style={'text-decoration': 'none', 'color': '#ffffff', 'margin-right': '20px'},
        href='https://plot.ly/dash/', target='_blank')

    font_awesome = html.A(
        children=[
            html.I([], className='fa fa-font-awesome'),
            html.Span('Font Awesome', style=span_style)
        ], style={'text-decoration': 'none', 'color': '#ffffff', 'margin-right': '20px'},
        href='http://fontawesome.io/', target='_blank')

    github_profile = html.A(
        children=[
            html.I([], className='fa fa-github'),
            html.Span('Jacek Filipczuk\n Github', style=span_style)
        ], style={'text-decoration': 'none', 'color': '#ffffff', 'margin-right': '20px'},
        href=github_profile_link, target='_blank')

    ul1 = html.Div(
        children=[
            html.Li(mapbox, style={
                'display': 'inline-block', 'color': '#ffffff'}),
            html.Li(font_awesome, style={
                'display': 'inline-block', 'color': '#ffffff'}),
            html.Li(github_profile, style={
                'display': 'inline-block', 'color': '#ffffff'}),
        ],
        style={'list-style-type': 'none', 'font-size': '30px'},
    )

    #TO-DO: update twitter message text according to selected project
    hashtags = 'plotly,dash,nlp'
    tweet = 'Jacek Filipczuk Wine Reviews WebApp, a cool dashboard with Plotly Dash!'
    twitter_href = 'https://twitter.com/intent/tweet?hashtags={}&text={}' \
        .format(hashtags, tweet)
    twitter = html.A(
        children=html.I(children=[], className='fa fa-twitter',
                        style={"color": "rgb(29, 161, 242)"}),
        title='Tweet me!', href=twitter_href, target='_blank')

    github = html.A(
        children=html.I(children=[], className='fa fa-github',
                        style={'color': 'black'}),
        title='Repo on GitHub',
        href='https://github.com/jacekfilipczuk/interactive_dashboard', target='_blank')

    li_right_first = {'line-style-type': 'none', 'display': 'inline-block'}
    li_right_others = {k: v for k, v in li_right_first.items()}
    li_right_others.update({'margin-left': '10px'})
    ul2 = html.Ul(
        children=[
            html.Li(twitter, style=li_right_first),
            html.Li(github, style=li_right_others),
        ],
        style={
            'position': 'fixed',
            'right': '1.5rem',
            'bottom': '75px',
            'font-size': '60px'
        }
    )
    div = html.Div([p, ul1, ul2])

    footer_style = {
        'font-size': '2.2rem',
        'background-color': 'rgb(79, 152, 202)',
        'margin-top': '5rem',
        'display': 'inline-block', 'padding': '16px 32px 8px'
    }
    footer = html.Footer(div, style=footer_style, className='twelve columns')
    return footer


def create_body():
    #TO-DO: change label names for the tabs according to selected project
    body = dbc.Container([
        dcc.Tabs(id="tabs-header",
                 children=[
                     dcc.Tab(label='Data & Details', value='tab-data-description'),
                     dcc.Tab(label='Graphs', value='tab-graphs'),
                     dcc.Tab(label='Graphs & EDA', value='tab-3'),
                     dcc.Tab(label='Reviews Clustering', value='tab-4'),
                     dcc.Tab(label='Recommender System', value='tab-5')
                 ],
                 value='tab-data-description', className="bottom32"),
        html.Div(id='tabs-content')
    ], style={"maxWidth": "1140px"})

    return body
