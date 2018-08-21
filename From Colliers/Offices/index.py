import dash
import dash_core_components as dcc
import dash_html_components as html

from apps import pages_layout as pages
from apps import deals_page
from apps import update_base_page
from apps import susp_deal_page
from apps import default_graphics
from apps import presentation_page
from app import app

app.layout = pages.serve_layout()


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-deals':
        return pages.deals_page()
    elif pathname == '/page-update-database':
        return pages.update_database()
    elif pathname == '/suspicious_deals':
        return pages.suspicious_deals_page()
    elif pathname == '/page-default-graphs':
        return pages.default_graphics_and_tables_page()
    elif pathname == '/page-presentations':
        return pages.presentation_list()
    elif pathname == '/page-help':
        return pages.help_page()
    elif pathname == '/page-about':
        return pages.about_page()
    else:
        return pages.index_page()


if __name__ == '__main__':
    app.run_server(debug=True, host='10.168.207.67')
