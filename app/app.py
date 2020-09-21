import dash
from config import external_stylesheets, app_name, meta_tags_arg
from layouts.layout_skeleton import create_layout_skeleton



app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[meta_tags_arg])
app.title = app_name
app.config.suppress_callback_exceptions = True
app.layout = create_layout_skeleton()



if __name__ == '__main__':
    app.run_server(debug=True)