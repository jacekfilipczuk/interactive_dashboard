import dash
from config import external_stylesheets, app_name, meta_tags_arg
from layouts.layout_skeleton import create_layout_skeleton
from dash.dependencies import Input, Output
from layouts.content_layouts import render_data_description, get_charts



app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[meta_tags_arg])
app.title = app_name
app.config.suppress_callback_exceptions = True
app.layout = create_layout_skeleton()

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs-header', 'value')])
def render_tabs_content(tab_value):
    if tab_value == 'tab-data-description':
        return render_data_description()
    elif tab_value == 'tab-graphs':
        return get_charts()
    else:
        pass



if __name__ == '__main__':
    app.run_server(debug=True, port=8060)