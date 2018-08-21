import dash
import base64
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from apps import static
from apps import colors_and_fonts as color

from app import app


@app.callback(dash.dependencies.Output('interface-default-graphics', 'labelStyle'),
              # Отображение блока со списком дефолтных графиков
              [dash.dependencies.Input('tree-checklist-default-graphics', 'values')
               ])
def show_default_graphics_tree(val):
    """В декораторе на вход принимается значение чеклиста 'colums'.
       Если значение выбрано, то отрисовывается новый блок со списком, как в дереве"""
    if 'Show' in val:
        children = {'display': 'block',
                    'width': '192px',
                    'margin': '0 0 0 10px',
                    }
    else:
        children = {'display': 'none'
                    }
    return children


def select_default_graph_from_check_graphics():
    """Функция отображения дефолтных графиков по значению checklist`а
       Эта функция введена искуственно для возможности скрыть блок кода в IDE"""

    @app.callback(dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-2017-RU', 'style'),
                  [dash.dependencies.Input('interface-default-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_graph_ru(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-RU' in val:
                show_graph = {'display': 'inline-block',
                              # 'padding': '100px 0px 0px 50px'
                              'vertical-align': 'middle'
                              }

            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-RU' not in val:
                show_graph = {'display': 'none',
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_graph

    @app.callback(dash.dependencies.Output('pie-4-text', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_text_ru(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-RU' in val:
                show_text = {'display': 'inline-block',
                             'horizontal-align': 'middle'
                             }

            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-RU' not in val:
                show_text = {'display': 'none',
                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_text

    @app.callback(dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-1Q2018-RU', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_1q_2018_graph_ru(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-RU' in val:
                show_graph = {'display': 'inline-block',
                              # 'padding': '100px 0px 0px 50px'
                              'vertical-align': 'middle'

                              }

            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-RU' not in val:
                show_graph = {'display': 'none'
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_graph

    @app.callback(dash.dependencies.Output('pie-5-text', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_text_ru(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-RU' in val:
                show_text = {'display': 'inline-block',
                             'padding-left': '150px'
                             }

            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-RU' not in val:
                show_text = {'display': 'none',
                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_text

    @app.callback(dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-five-years-RU', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_five_years_graph_ru(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-RU' in val:
                show_graph = {'display': 'inline-block',
                              # 'padding': '100px 0px 0px 50px'
                              'vertical-align': 'middle'

                              }

            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-RU' not in val:
                show_graph = {'display': 'none',
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_graph

    @app.callback(dash.dependencies.Output('pie-6-text', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_text_ru(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-RU' in val:
                show_text = {'display': 'inline-block',
                             'padding-left': '90px'
                             }

            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-RU' not in val:
                show_text = {'display': 'none',
                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_text

    @app.callback(dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-2017-MOS', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_graph_mos(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-MOS' in val:
                show_graph = {'display': 'inline-block',
                              }

            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-MOS' not in val:
                show_graph = {'display': 'none',
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_graph

    @app.callback(dash.dependencies.Output('pie-7-text', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_text_mos(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-MOS' in val:
                show_text = {'display': 'inline-block',
                             'padding-left': '50px'
                             }

            if 'LLR, (E)TR, LLR/(E)TR-pie-2017-MOS' not in val:
                show_text = {'display': 'none',
                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_text

    @app.callback(dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-1Q2018-MOS', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_1q_2018_graph_mos(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-MOS' in val:
                show_graph = {'display': 'inline-block',
                              }

            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-MOS' not in val:
                show_graph = {'display': 'none',
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_graph

    @app.callback(dash.dependencies.Output('pie-8-text', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_text_mos(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-MOS' in val:
                show_text = {'display': 'inline-block',
                             'padding-left': '50px'
                             }

            if 'LLR, (E)TR, LLR/(E)TR-pie-1Q2018-MOS' not in val:
                show_text = {'display': 'none',
                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_text

    @app.callback(dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-five-years-MOS', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_five_years_graph_mos(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-MOS' in val:
                show_graph = {'display': 'inline-block',
                              }

            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-MOS' not in val:
                show_graph = {'display': 'none',
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_graph

    @app.callback(dash.dependencies.Output('pie-9-text', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_llr_etr_pie_2017_text_mos(val):
        try:
            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-MOS' in val:
                show_text = {'display': 'inline-block',
                             'padding-left': '50px'
                             }

            if 'LLR, (E)TR, LLR/(E)TR-pie-five-years-MOS' not in val:
                show_text = {'display': 'none',
                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_text

    @app.callback(dash.dependencies.Output('html-tab-RU-2017-div', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_bigest_deal_table_2017(val):
        try:
            if 'biggest-deal-tab-2017' in val:
                show_tab = {'display': 'inline',
                            }

            if 'biggest-deal-tab-2017' not in val:
                show_tab = {'display': 'none',
                            }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_tab

    @app.callback(dash.dependencies.Output('html-tab-RU-1q2018-div', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_bigest_deal_table_1q2018(val):
        try:
            if 'biggest-deal-tab-1q2018' in val:
                show_tab = {'display': 'inline',
                            }

            if 'biggest-deal-tab-1q2018' not in val:
                show_tab = {'display': 'none',
                            }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_tab

    @app.callback(dash.dependencies.Output('html-tab-RU-five-years-div', 'style'),
                  [dash.dependencies.Input('interface-graphics', 'values')
                   ])
    def update_bigest_deal_table_2013_2018(val):
        try:
            if 'biggest-deal-tab-2013-2018' in val:
                show_tab = {'display': 'inline',
                            }

            if 'biggest-deal-tab-2013-2018' not in val:
                show_tab = {'display': 'none',
                            }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return show_tab


select_default_graph_from_check_graphics()  # вызов функции с отображением дефолтных графиков и подписей к ним


def default_graphics():
    """Функция по отрисовке дефолтных графиков. Сначала идет блок с
       интерактивными графиками, далее по коду идет вызов функции получения
       байткода картинки с сервера Plotly и загрузки него в элемент страницы """

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-2017-RU', 'figure'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ]
    )
    def update_pie_graph_4(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[(df_plot['Year'].isin(['2017'])) & (df_plot['Country'].isin(['RU']))]
        print(data['LLR_Only'])
        data_llr_only = data[(data['LLR_Only'].isin(['Y']))]
        print(data_llr_only)
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)
        print(df_graph)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        print(pv)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        return {
            'data': [pie1],
            'layout': go.Layout(
                title='2017',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-1Q2018-RU', 'figure'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_pie_graph_5(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[
            (df_plot['Year'].isin(['2018'])) & (df_plot['Country'].isin(['RU'])) & (df_plot['Quarter'].isin(['1']))]
        data_llr_only = data[(data['LLR_Only'].isin(['Y']))]
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        return {
            'data': [pie1],
            'layout': go.Layout(
                title='LLR, (E)TR and LLR/(E)TR deals in Russia<br>'
                      '1Q 2018',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

    # @app.callback(
    #     dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-five-years-RU', 'figure'),
    #     [dash.dependencies.Input('interface-default-graphics', 'values')
    #      ])
    # def update_pie_graph_6(values):
    #     df_plot = static.all_deals_query_df.copy()
    #     data = df_plot[(df_plot['Country'].isin(['RU']))]
    #     data_llr_only = data[(data['LLR_Only'].isin(['Y'])) & (df_plot['Country'].isin(['RU']))]
    #     data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
    #     data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
    #     d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
    #          'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
    #     df_graph = pd.DataFrame(data=d)
    #
    #     width = 600
    #     height = 450
    #
    #     pv = pd.pivot_table(
    #         df_graph,
    #         index=["Type"],
    #         values=["SQM"],
    #         aggfunc=sum,
    #         fill_value=0)
    #     colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
    #     pie1 = go.Pie(values=pv["SQM"],
    #                   labels=['LLR', '(E)TR', 'LLR/(E)TR'],
    #                   hoverinfo='label+value+percent',
    #                   textinfo='label+percent',
    #                   textposition='outside',
    #                   textfont=dict(
    #                       color=colors_pie,
    #                       size=12),
    #                   marker=dict(colors=colors_pie,
    #                               line=dict(
    #                                   color=color.white,
    #                                   width=1
    #                               )
    #                               )
    #                   )
    #     return {
    #         'data': [pie1],
    #         'layout': go.Layout(
    #             title='2013-2018',
    #             width=width,
    #             height=height,
    #             legend=dict(orientation="h",
    #                         traceorder="normal"),
    #         )
    #     }

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-2017-MOS', 'figure'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_pie_graph_7(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[(df_plot['Year'].isin(['2017'])) & (df_plot['City'].isin(['Moscow']))]
        data_llr_only = data[(data['LLR_Only'].isin(['Y']))]
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        return {
            'data': [pie1],
            'layout': go.Layout(
                title='LLR, (E)TR and LLR/(E)TR deals in Russia<br>'
                      '2017',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-1Q2018-MOS', 'figure'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_pie_graph_8(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[
            (df_plot['Year'].isin(['2018'])) & (df_plot['City'].isin(['Moscow'])) & (df_plot['Quarter'].isin(['1']))]
        data_llr_only = data[(data['LLR_Only'].isin(['Y']))]
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        return {
            'data': [pie1],
            'layout': go.Layout(
                title='LLR, (E)TR and LLR/(E)TR deals in Moscow<br>'
                      '1Q 2018',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-five-years-MOS', 'figure'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_pie_graph_9(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[(df_plot['City'].isin(['Moscow']))]
        data_llr_only = data[(data['LLR_Only'].isin(['Y']))]
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
        # ## ('data_llr_only_sum', data_llr_only["SQM"].sum())
        # ## ('data_e_tr_only', data_e_tr_only["SQM"].sum())
        # ## ('data_llr_e_tr_only', data_llr_e_tr_only["SQM"].sum())
        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        return {
            'data': [pie1],
            'layout': go.Layout(
                title='LLR, (E)TR and LLR/(E)TR deals in Moscow<br>'
                      '2013-2018',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

    """ТУТ НАЧИНАЮТСЯ ФУНКЦИИ ЗАГРУЗКИ СТАТИЧЕСКИХ КАРТИНОК"""

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-2017-RU-img', 'src'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_pie_graph_4_img(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[(df_plot['Year'].isin(['2017'])) & (df_plot['Country'].isin(['RU']))]
        data_llr_only = data[(data['LLR_Only'].isin(['Y']))]
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]

        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        image_data = {
            'data': [pie1],
            'layout': go.Layout(
                title='LLR, (E)TR and LLR/(E)TR deals in Russia<br>'
                      '2017',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

        img = py.image.get(image_data, format='png')
        plot_bytes_encode = str(base64.b64encode(img))
        plot_bytes_encode = plot_bytes_encode[0:-1]
        plot_bytes_encode_fin = plot_bytes_encode[2:]
        stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

        return stringpic

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-1Q2018-RU-img', 'src'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_pie_graph_5_img(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[
            (df_plot['Year'].isin(['2018'])) & (df_plot['Country'].isin(['RU'])) & (df_plot['Quarter'].isin(['1']))]
        data_llr_only = data[(data['LLR_Only'].isin(['Y']))]
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        image_data = {
            'data': [pie1],
            'layout': go.Layout(
                title='LLR, (E)TR and LLR/(E)TR deals in Russia<br>'
                      '1Q 2018',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

        img = py.image.get(image_data, format='png')
        plot_bytes_encode = str(base64.b64encode(img))
        plot_bytes_encode = plot_bytes_encode[0:-1]
        plot_bytes_encode_fin = plot_bytes_encode[2:]
        stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли
        return stringpic

    @app.callback(
        dash.dependencies.Output('LLR, (E)TR, LLR/(E)TR-pie-five-years-RU-img', 'src'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_pie_graph_6_img(values):
        df_plot = static.all_deals_query_df.copy()
        data = df_plot[(df_plot['Country'].isin(['RU']))]
        data_llr_only = data[(data['LLR_Only'].isin(['Y'])) & (df_plot['Country'].isin(['RU']))]
        data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
        data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
        d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
             'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
        df_graph = pd.DataFrame(data=d)

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Type"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
        pie1 = go.Pie(values=pv["SQM"],
                      labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                      hoverinfo='label+value+percent',
                      textinfo='label+percent',
                      textposition='outside',
                      textfont=dict(
                          color=colors_pie,
                          size=12),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        image_data = {
            'data': [pie1],
            'layout': go.Layout(
                title='LLR, (E)TR and LLR/(E)TR deals in Russia<br>'
                      '2013-2018',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

        img = py.image.get(image_data, format='png')
        plot_bytes_encode = str(base64.b64encode(img))
        plot_bytes_encode = plot_bytes_encode[0:-1]
        plot_bytes_encode_fin = plot_bytes_encode[2:]
        stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли
        return stringpic


default_graphics()  # вызов функции с отображением базовых pie графиков


def default_tables():
    '''Функция по отрисовке дефолтных таблиц по крупнейшим этим сделкам за этот период'''

    @app.callback(
        dash.dependencies.Output('biggest-deal-tab-test', 'figure'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_biggest_deals_tab(values):
        all_deals_2017 = static.all_deals_query_df[static.all_deals_query_df['Year'].isin(['2017'])]
        all_deals_2017 = all_deals_2017.sort_values('SQM', ascending=False)

        all_deals_2017_selected = all_deals_2017[['Agency', 'Property_Name', 'City', 'SQM',
                                                  'Company', 'Business_Sector', 'Type_of_Deal']].head(10)

        trace = go.Table(
            columnwidth=[80, 200, 80, 100, 150, 200, 100],

            header=dict(
                values=["Agency", "Property Name", 'City', "Office area", "Company", "Business Sector", "Type of Deal"],
                line=dict(color=color.white),
                fill=dict(color=color.sar_color),
                align=['left', 'left', 'left', 'center', 'left', 'left', 'center'],
                font=dict(color='white', size=12), ),

            cells=dict(values=[all_deals_2017_selected.Agency.tolist(),
                               all_deals_2017_selected.Property_Name.tolist(),
                               all_deals_2017_selected.City,
                               all_deals_2017_selected.SQM,
                               all_deals_2017_selected.Company,
                               all_deals_2017_selected.Business_Sector,
                               all_deals_2017_selected.Type_of_Deal
                               ],
                       line=dict(color=color.white),
                       fill=dict(color='#EDFAFF'),
                       align=['left', 'left', 'left', 'center', 'left', 'left', 'center']))

        layout = dict(width=830, height=330)
        data = [trace]
        fig = dict(data=data, layout=layout)
        return fig

    @app.callback(
        dash.dependencies.Output('html-tab-RU-2017', 'children'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_html_tab(values):
        all_deals_2017 = static.all_deals_query_df[static.all_deals_query_df['Year'].isin(['2017'])]
        all_deals_2017 = all_deals_2017.sort_values('SQM', ascending=False)
        all_deals_2017['SQM'] = all_deals_2017['SQM'].round()
        all_deals_2017_selected = all_deals_2017[['Agency', 'Property_Name', 'City', 'SQM',
                                                  'Company', 'Business_Sector', 'Type_of_Deal']].head(10)
        return generate_table_top_deals(all_deals_2017_selected)

    @app.callback(
        dash.dependencies.Output('html-tab-RU-1q2018', 'children'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_html_tab(values):
        all_deals_2018 = static.all_deals_query_df[
            static.all_deals_query_df['Year'].isin(['2018']) & static.all_deals_query_df['Quarter'].isin(['1'])]
        all_deals_2018 = all_deals_2018.sort_values('SQM', ascending=False)
        all_deals_2018['SQM'] = all_deals_2018['SQM'].round()
        all_deals_2018_selected = all_deals_2018[['Agency', 'Property_Name', 'City', 'SQM',
                                                  'Company', 'Business_Sector', 'Type_of_Deal']].head(10)
        return generate_table_top_deals(all_deals_2018_selected)

    @app.callback(
        dash.dependencies.Output('html-tab-RU-five-years', 'children'),
        [dash.dependencies.Input('interface-default-graphics', 'values')
         ])
    def update_html_tab(values):
        all_deals_2018 = static.all_deals_query_df
        all_deals_2018 = all_deals_2018.sort_values('SQM', ascending=False)
        all_deals_2018['SQM'] = all_deals_2018['SQM'].round()
        all_deals_2018_selected = all_deals_2018[['Agency', 'Property_Name', 'City', 'SQM',
                                                  'Company', 'Business_Sector', 'Type_of_Deal',
                                                  'Year', 'Quarter']].head(10)
        return generate_table_top_deals_with_year(all_deals_2018_selected)


default_tables()  # вызов функции с отображением базовых таблиц

''' Начало блока по отрисовке статических изображений. Код закомментирован до обсуждения  '''


# _-_-------___----


# БЛОК КОДА ПО ОТРИСОВКЕ ТИПОВЫХ ТАБЛИЦ

def generate_table_top_deals_with_year(dataframe, max_rows=10):
    """ФУНКЦИЯ ОТРИСОВКИ ТАБЛИЦЫ ЧЕРЕЗ  HTML, ДЛЯ НАСТРОЙКИ СТИЛЯ ИСПОЛЬЗУЕТСЯ CSS РАЗМЕТКА"""
    return html.Table(
        [
            html.Tr(  # HEADER
                [
                    html.Th(col,
                            style={
                                'text-align': pos,
                                'width': wid,
                                'height': hei
                            })
                    for col, wid, hei, pos in zip(["Agency", "Property Name", "City", "Office area", "Company",
                                                   "Business Sector", "Type of Deal", 'Year', 'Quarter'],
                                                  ['70px', '175px', '70px', '105px', '171px', '229px',
                                                   '102px', '60px', '30px'],
                                                  ['20px', '20px', '20px', '20px', '20px', '20px', '20px', '20px',
                                                   '20px'],
                                                  ['left', 'left', 'center', 'center', 'left', 'left', 'center',
                                                   'center', 'center'])
                ],
                style={  # CSS разметка
                    'background-color': color.colliers_light_blue,
                    'color': color.white,

                }
            )
        ]
        +
        [
            html.Tr(  # BODY
                [
                    html.Td(dataframe.iloc[i][col],
                            style={
                                'text-align': pos,
                                'width': wid,
                                'height': hei

                            })
                    for col, wid, hei, pos in
                    zip(dataframe.columns, ['70px', '175px', '70px', '105px', '171px', '229px',
                                            '102px', '60px', '30px'],
                        ['20px', '20px', '20px', '20px', '20px', '20px', '20px', '20px', '20px'],
                        ['left', 'left', 'center', 'center', 'left', 'left', 'center',
                         'center', 'center'])
                ],
                style={  # CSS разметка
                    'background-color': color.colliers_pale_blue,
                }
            ) for i in range(min(len(dataframe), max_rows))]
    )


def generate_table_top_deals(dataframe, max_rows=10):
    """ФУНКЦИЯ ОТРИСОВКИ ТАБЛИЦЫ ЧЕРЕЗ  HTML, ДЛЯ НАСТРОЙКИ СТИЛЯ ИСПОЛЬЗУЕТСЯ CSS РАЗМЕТКА"""
    return html.Table(
        [
            html.Tr(  # HEADER
                [
                    html.Th(col,
                            style={
                                'text-align': pos,
                                'width': wid,
                                'height': hei
                            })
                    for col, wid, hei, pos in zip(["Agency", "Property Name", "City", "Office area", "Company",
                                                   "Business Sector", "Type of Deal"],
                                                  ['70px', '175px', '70px', '105px', '171px', '229px', '102px'],
                                                  ['20px', '20px', '20px', '20px', '20px', '20px', '20px'],
                                                  ['left', 'left', 'center', 'center', 'left', 'left', 'center'])
                ],
                style={  # CSS разметка
                    'background-color': color.colliers_light_blue,
                    'color': color.white,

                }
            )
        ]
        +
        [
            html.Tr(  # BODY
                [
                    html.Td(dataframe.iloc[i][col],
                            style={
                                'text-align': pos,
                                'width': wid,
                                'height': hei

                            })
                    for col, wid, hei, pos in zip(dataframe.columns,
                                                  ['70px', '175px', '70px', '105px', '171px', '229px', '102px'],
                                                  ['20px', '20px', '20px', '20px', '20px', '20px', '20px'],
                                                  ['left', 'left', 'center', 'center', 'left', 'left', 'center']
                                                  )
                ],
                style={  # CSS разметка
                    'background-color': color.colliers_pale_blue,
                }
            ) for i in range(min(len(dataframe), max_rows))]
    )

# ______________________________________________________________


def update_pie_graph_def_sale_lease_1q_2018_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1'])) & (df_plot['Country'].isin(['RU']))]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_sale_1q_2018_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1'])) & (df_plot['Country'].isin(['RU']))]
    data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_lease_1q_2018_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1'])) & (df_plot['Country'].isin(['RU']))]
    data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def update_pie_graph_def_sale_lease_2q_2018_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    if not df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        data = df_plot[
            (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2'])) & (df_plot['Country'].isin(['RU']))]
        df_graph = data

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Agency"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                      color.jll_color, color.kf_color, color.sar_color]
        pie1 = go.Pie(values=round(pv["SQM"]),
                      labels=pv.index,
                      hoverinfo='skip',
                      textinfo='percent',
                      textposition='inside',
                      textfont=dict(
                          color=color.white,
                          size=12,
                          family='Arial, bold'),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        # image_data =

        # img = py.image.get(image_data, format='png')
        # plot_bytes_encode = str(base64.b64encode(img))
        # plot_bytes_encode = plot_bytes_encode[0:-1]
        # plot_bytes_encode_fin = plot_bytes_encode[2:]
        # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

        return {
            'data': [pie1],
            'layout': go.Layout(
                title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }

    if df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        return {
            'data': [go.Pie(values=[1],
                            labels=['NONE'],
                            hoverinfo='skip',
                            textinfo='percent',
                            textposition='inside',
                            textfont=dict(
                                color=color.white,
                                size=12,
                                family='Arial, bold'),
                            marker=dict(colors=color.colliers_grey_80,
                                        line=dict(
                                            color=color.white,
                                            width=1
                                        )
                                        )
                            )],
            'layout': go.Layout(
                title='<b>' + 'НЕТ ДАННЫХ' + '</b>',
                width=600,
                height=450,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }


def update_pie_graph_def_sale_2q_2018_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    if not df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        data = df_plot[
            (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2'])) & (df_plot['Country'].isin(['RU']))]
        data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
        df_graph = data

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Agency"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                      color.jll_color, color.kf_color, color.sar_color]
        pie1 = go.Pie(values=round(pv["SQM"]),
                      labels=pv.index,
                      hoverinfo='skip',
                      textinfo='percent',
                      textposition='inside',
                      textfont=dict(
                          color=color.white,
                          size=12,
                          family='Arial, bold'),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        # image_data =

        # img = py.image.get(image_data, format='png')
        # plot_bytes_encode = str(base64.b64encode(img))
        # plot_bytes_encode = plot_bytes_encode[0:-1]
        # plot_bytes_encode_fin = plot_bytes_encode[2:]
        # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

        return {
            'data': [pie1],
            'layout': go.Layout(
                title='<b>' + 'Объём сделок (продажа)' + '</b>',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }
    if df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        return {
            'data': [go.Pie(values=[1],
                            labels=['NONE'],
                            hoverinfo='skip',
                            textinfo='percent',
                            textposition='inside',
                            textfont=dict(
                                color=color.white,
                                size=12,
                                family='Arial, bold'),
                            marker=dict(colors=color.colliers_grey_80,
                                        line=dict(
                                            color=color.white,
                                            width=1
                                        )
                                        )
                            )],
            'layout': go.Layout(
                title='<b>' + 'НЕТ ДАННЫХ' + '</b>',
                width=600,
                height=450,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }


def update_pie_graph_def_lease_2q_2018_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 2 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    print(type(df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]))
    if not df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        data = df_plot[
            (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2'])) & (df_plot['Country'].isin(['RU']))]
        data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
        df_graph = data

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Agency"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                      color.jll_color, color.kf_color, color.sar_color]
        pie1 = go.Pie(values=round(pv["SQM"]),
                      labels=pv.index,
                      hoverinfo='skip',
                      textinfo='percent',
                      textposition='inside',
                      textfont=dict(
                          color=color.white,
                          size=12,
                          family='Arial, bold'),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        # image_data =

        # img = py.image.get(image_data, format='png')
        # plot_bytes_encode = str(base64.b64encode(img))
        # plot_bytes_encode = plot_bytes_encode[0:-1]
        # plot_bytes_encode_fin = plot_bytes_encode[2:]
        # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

        return {
            'data': [pie1],
            'layout': go.Layout(
                title='<b>' + 'Объём сделок (аренда)' + '</b>',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }
    if df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        return {
            'data': [go.Pie(values=[1],
                            labels=['NONE'],
                            hoverinfo='skip',
                            textinfo='percent',
                            textposition='inside',
                            textfont=dict(
                                color=color.white,
                                size=12,
                                family='Arial, bold'),
                            marker=dict(colors=color.colliers_grey_80,
                                        line=dict(
                                            color=color.white,
                                            width=1
                                        )
                                        )
                            )],
            'layout': go.Layout(
                title='<b>' + 'НЕТ ДАННЫХ' + '</b>',
                width=600,
                height=450,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def update_pie_graph_def_sale_lease_2017_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2017'])) & (df_plot['Country'].isin(['RU']))]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_sale_2017_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2017'])) & (df_plot['Country'].isin(['RU']))]
    data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_lease_2017_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2017'])) & (df_plot['Country'].isin(['RU']))]
    data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def update_pie_graph_def_sale_lease_1q_2018_mos():  # pie по ДОЛЯ РЫНКА ПО МОСКВЕ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1'])) & (df_plot['Country'].isin(['RU'])) & (
            df_plot['City'].isin(['Moscow']))]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_sale_1q_2018_mos():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['Moscow']))]
    data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_lease_1q_2018_mos():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['Moscow']))]
    data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def update_pie_graph_def_sale_lease_2q_2018_mos():  # pie по ДОЛЯ РЫНКА ПО МОСКВЕ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    if not df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        data = df_plot[
            (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2'])) & (df_plot['Country'].isin(['RU'])) & (
                df_plot['City'].isin(['Moscow']))]
        df_graph = data

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Agency"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                      color.jll_color, color.kf_color, color.sar_color]
        pie1 = go.Pie(values=round(pv["SQM"]),
                      labels=pv.index,
                      hoverinfo='skip',
                      textinfo='percent',
                      textposition='inside',
                      textfont=dict(
                          color=color.white,
                          size=12,
                          family='Arial, bold'),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        # image_data =

        # img = py.image.get(image_data, format='png')
        # plot_bytes_encode = str(base64.b64encode(img))
        # plot_bytes_encode = plot_bytes_encode[0:-1]
        # plot_bytes_encode_fin = plot_bytes_encode[2:]
        # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

        return {
            'data': [pie1],
            'layout': go.Layout(
                title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }
    if df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        return {
            'data': [go.Pie(values=[1],
                            labels=['NONE'],
                            hoverinfo='skip',
                            textinfo='percent',
                            textposition='inside',
                            textfont=dict(
                                color=color.white,
                                size=12,
                                family='Arial, bold'),
                            marker=dict(colors=color.colliers_grey_80,
                                        line=dict(
                                            color=color.white,
                                            width=1
                                        )
                                        )
                            )],
            'layout': go.Layout(
                title='<b>' + 'НЕТ ДАННЫХ' + '</b>',
                width=600,
                height=450,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }


def update_pie_graph_def_sale_2q_2018_mos():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    if not df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        data = df_plot[
            (df_plot['Year'].isin(['2018']))
            & (df_plot['Quarter'].isin(['2']))
            & (df_plot['Country'].isin(['RU']))
            & (df_plot['City'].isin(['Moscow']))]
        data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
        df_graph = data

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Agency"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                      color.jll_color, color.kf_color, color.sar_color]
        pie1 = go.Pie(values=round(pv["SQM"]),
                      labels=pv.index,
                      hoverinfo='skip',
                      textinfo='percent',
                      textposition='inside',
                      textfont=dict(
                          color=color.white,
                          size=12,
                          family='Arial, bold'),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        # image_data =

        # img = py.image.get(image_data, format='png')
        # plot_bytes_encode = str(base64.b64encode(img))
        # plot_bytes_encode = plot_bytes_encode[0:-1]
        # plot_bytes_encode_fin = plot_bytes_encode[2:]
        # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

        return {
            'data': [pie1],
            'layout': go.Layout(
                title='<b>' + 'Объём сделок (продажа)' + '</b>',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }
    if df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        return {
            'data': [go.Pie(values=[1],
                            labels=['NONE'],
                            hoverinfo='skip',
                            textinfo='percent',
                            textposition='inside',
                            textfont=dict(
                                color=color.white,
                                size=12,
                                family='Arial, bold'),
                            marker=dict(colors=color.colliers_grey_80,
                                        line=dict(
                                            color=color.white,
                                            width=1
                                        )
                                        )
                            )],
            'layout': go.Layout(
                title='<b>' + 'НЕТ ДАННЫХ' + '</b>',
                width=600,
                height=450,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }


def update_pie_graph_def_lease_2q_2018_mos():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    if not df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        data = df_plot[
            (df_plot['Year'].isin(['2018']))
            & (df_plot['Quarter'].isin(['2']))
            & (df_plot['Country'].isin(['RU']))
            & (df_plot['City'].isin(['Moscow']))]
        data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
        df_graph = data

        width = 600
        height = 450

        pv = pd.pivot_table(
            df_graph,
            index=["Agency"],
            values=["SQM"],
            aggfunc=sum,
            fill_value=0)
        colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                      color.jll_color, color.kf_color, color.sar_color]
        pie1 = go.Pie(values=round(pv["SQM"]),
                      labels=pv.index,
                      hoverinfo='skip',
                      textinfo='percent',
                      textposition='inside',
                      textfont=dict(
                          color=color.white,
                          size=12,
                          family='Arial, bold'),
                      marker=dict(colors=colors_pie,
                                  line=dict(
                                      color=color.white,
                                      width=1
                                  )
                                  )
                      )
        # image_data =

        # img = py.image.get(image_data, format='png')
        # plot_bytes_encode = str(base64.b64encode(img))
        # plot_bytes_encode = plot_bytes_encode[0:-1]
        # plot_bytes_encode_fin = plot_bytes_encode[2:]
        # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
        # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

        return {
            'data': [pie1],
            'layout': go.Layout(
                title='<b>' + 'Объём сделок (аренда)' + '</b>',
                width=width,
                height=height,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }
    if df_plot[(df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['2']))]['SQM'].empty:
        return {
            'data': [go.Pie(values=[1],
                            labels=['NONE'],
                            hoverinfo='skip',
                            textinfo='percent',
                            textposition='inside',
                            textfont=dict(
                                color=color.white,
                                size=12,
                                family='Arial, bold'),
                            marker=dict(colors=color.colliers_grey_80,
                                        line=dict(
                                            color=color.white,
                                            width=1
                                        )
                                        )
                            )],
            'layout': go.Layout(
                title='<b>' + 'НЕТ ДАННЫХ' + '</b>',
                width=600,
                height=450,
                legend=dict(orientation="h",
                            traceorder="normal"),
            )
        }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def update_pie_graph_def_sale_lease_1q_2018_sp():  # pie по ДОЛЯ РЫНКА ПО МОСКВЕ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018']))
        & (df_plot['Quarter'].isin(['1']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['St. Pete']))]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_sale_1q_2018_sp():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018']))
        & (df_plot['Quarter'].isin(['1']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['St. Pete']))]
    data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_lease_1q_2018_sp():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018']))
        & (df_plot['Quarter'].isin(['1']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['St. Pete']))]
    data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def update_pie_graph_def_sale_lease_2017_sp():  # pie по ДОЛЯ РЫНКА ПО МОСКВЕ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2017']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['St. Pete']))]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_sale_2017_sp():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['St. Pete']))]
    data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_lease_2017_sp():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['St. Pete']))]
    data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def update_pie_graph_def_sale_lease_2017_mos():  # pie по ДОЛЯ РЫНКА ПО МОСКВЕ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2017']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['Moscow']))]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_sale_2017_mos():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['Moscow']))]
    data = data[data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_def_lease_2017_mos():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 SALE
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018']))
        & (df_plot['Country'].isin(['RU']))
        & (df_plot['City'].isin(['Moscow']))]
    data = data[~data['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    df_graph = data

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Agency"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.cbre_color, color.cw_color, color.colliers_color,
                  color.jll_color, color.kf_color, color.sar_color]
    pie1 = go.Pie(values=round(pv["SQM"]),
                  labels=pv.index,
                  hoverinfo='skip',
                  textinfo='percent',
                  textposition='inside',
                  textfont=dict(
                      color=color.white,
                      size=12,
                      family='Arial, bold'),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    # image_data =

    # img = py.image.get(image_data, format='png')
    # plot_bytes_encode = str(base64.b64encode(img))
    # plot_bytes_encode = plot_bytes_encode[0:-1]
    # plot_bytes_encode_fin = plot_bytes_encode[2:]
    # stringpic = "data:image/png;base64," + plot_bytes_encode_fin  # строчка с байткодом картинки
    # # stringpic = plot_url_png                # строчка с сылкой на файл картинки на сайте плотли

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


def update_pie_graph_llr_etr_2017_ru():
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[(df_plot['Year'].isin(['2017'])) & (df_plot['Country'].isin(['RU']))]
    data_llr_only = data[(data['LLR_Only'].isin(['Yes']))]
    data_e_tr_only = data[(data['E_TR_Only'].isin(['Yes']))]
    data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Yes']))]
    # ##print('data_llr_only_sum', data_llr_only["SQM"].sum())
    # ##print('data_e_tr_only', data_e_tr_only["SQM"].sum())
    # ##print('data_llr_e_tr_only', data_llr_e_tr_only["SQM"].sum())
    d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
         'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
    df_graph = pd.DataFrame(data=d)

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Type"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
    pie1 = go.Pie(values=pv["SQM"],
                  labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                  hoverinfo='label+value+percent',
                  textinfo='label+percent',
                  textposition='outside',
                  textfont=dict(
                      color=colors_pie,
                      size=12),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    return {
        'data': [pie1],
        'layout': go.Layout(
            title='2017',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


def update_pie_graph_llr_etr_1q2018_ru():
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Country'].isin(['RU'])) & (df_plot['Quarter'].isin(['1']))]
    data_llr_only = data[(data['LLR_Only'].isin(['Yes']))]
    data_e_tr_only = data[(data['E_TR_Only'].isin(['Yes']))]
    data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Yes']))]
    d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
         'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
    df_graph = pd.DataFrame(data=d)

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Type"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
    pie1 = go.Pie(values=pv["SQM"],
                  labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                  hoverinfo='label+value+percent',
                  textinfo='label+percent',
                  textposition='outside',
                  textfont=dict(
                      color=colors_pie,
                      size=12),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    return {
        'data': [pie1],
        'layout': go.Layout(
            title='LLR, (E)TR and LLR/(E)TR deals in Russia<br>'
                  '1Q 2018',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


def pie_graph_five_years_llr_tr():
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[(df_plot['Country'].isin(['RU']))]
    data_llr_only = data[(data['LLR_Only'].isin(['Y'])) & (df_plot['Country'].isin(['RU']))]
    data_e_tr_only = data[(data['E_TR_Only'].isin(['Y']))]
    data_llr_e_tr_only = data[(data['LLR/E_TR'].isin(['Y']))]
    d = {'Type': ['LLR', '(E)TR', 'LLR/(E)TR'],
         'SQM': [data_llr_only["SQM"].sum(), data_e_tr_only["SQM"].sum(), data_llr_e_tr_only["SQM"].sum()]}
    df_graph = pd.DataFrame(data=d)

    width = 600
    height = 450

    pv = pd.pivot_table(
        df_graph,
        index=["Type"],
        values=["SQM"],
        aggfunc=sum,
        fill_value=0)
    colors_pie = [color.colliers_dark_blue, color.colliers_extra_light_blue, color.colliers_light_blue]
    pie1 = go.Pie(values=pv["SQM"],
                  labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                  hoverinfo='label+value+percent',
                  textinfo='label+percent',
                  textposition='outside',
                  textfont=dict(
                      color=colors_pie,
                      size=12),
                  marker=dict(colors=colors_pie,
                              line=dict(
                                  color=color.white,
                                  width=1
                              )
                              )
                  )
    return {
        'data': [pie1],
        'layout': go.Layout(
            title='2013-2018',
            width=width,
            height=height,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }