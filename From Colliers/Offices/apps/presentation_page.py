import dash
import base64
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from apps import static
from apps  import colors_and_fonts as color


# Файл с элементами страницы с разметкой для презентации
# Функции не принимают на вход данные, в дальнейшем добавить
# больше графиков и, возможно, добавить выбор графиков

def pie_graph_for_pres_ru_1q2018_sale_lease():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1'])) & (df_plot['Country'].isin(['RU']))]
    df_graph = data

    width = 290
    height = 227

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
                  legendgroup='group',
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

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда и продажа)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="v",
                        traceorder="normal"),
            margin=go.Margin(
                l=0,  # 50
                r=0,  # 50
                b=0,  # 100
                t=50,  # 100
                pad=4  # 4
            ),
        )
    }


def pie_graph_for_pres_ru_1q2018_lease():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    df_plot = static.all_deals_query_df.copy()
    data = df_plot[
        (df_plot['Year'].isin(['2018'])) & (df_plot['Quarter'].isin(['1'])) & (df_plot['Country'].isin(['RU']))
        & (~df_plot['Type_of_Deal'].isin(['Sale', 'Purchase']))]
    df_graph = data

    width = 290
    height = 227

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

    return {
        'data': [pie1],
        'layout': go.Layout(
            title='<b>' + 'Объём сделок (аренда)' + '</b>',
            width=width,
            height=height,
            legend=dict(orientation="v",
                        traceorder="normal"),

            margin=go.Margin(
                l=0,  # 50
                r=0,  # 50
                b=0,  # 100
                t=50,  # 100
                pad=4  # 4
            ),
        )
    }


def table_for_pres_sale_lease_ru(dataframe, max_rows=10):
    """ФУНКЦИЯ ОТРИСОВКИ ТАБЛИЦЫ ЧЕРЕЗ  HTML, ДЛЯ НАСТРОЙКИ СТИЛЯ ИСПОЛЬЗУЕТСЯ CSS РАЗМЕТКА"""
    return html.Table(
        [
            html.Tr(  # HEADER
                [
                    html.Th(
                        col,
                        style={
                            'text-align': 'center',
                            'width': wid,
                            'font-size': '10pt',
                            'font-weight': ['bold']
                        })
                    for col, wid in zip([" ",
                                         "Объём, кв. м",
                                         "Доля в объёме"],
                                        ['90px', '110px', '100px']
                                        )
                ],
                style={  # CSS разметка
                    'background-color': color.colliers_light_blue,
                    'color': color.white,
                    'allign': 'left',
                    # "padding-left": "50px",
                    'font-size': '12pt'

                }
            )
        ]
        +
        [
            html.Tr(  # BODY
                [
                    html.Td(dataframe.iloc[i][col],
                            style={
                                'text-align': 'right',
                                'width': wid,
                                "min-height": "15px",
                                'font-size': '10pt',
                                'border-bottom': '1px solid {}'.format(color.colliers_grey_10)

                            })
                    for col, wid in zip(dataframe.columns,
                                        ['100px', '100px', '100px'],
                                        )
                ],
                style={  # CSS разметка
                    # 'background-color': color.colliers_pale_blue,
                    'allign': 'left',
                    'margin-left': '50px',
                    # "padding-left": "50px",
                    "min-height": "15px",

                }
            ) for i in range(min(len(dataframe), max_rows)
                             )
        ],
        # style={
        #     'font-size': '10pt'
        # }

    )


def generate_table_for_pres_sale_lease_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    all_deals_2018 = static.all_deals_query_df
    all_deals_2018 = all_deals_2018[
        (all_deals_2018['Year'].isin(['2018'])) & (all_deals_2018['Quarter'].isin(['1'])) & (
            all_deals_2018['Country'].isin(['RU']))]
    all_deals_2018 = all_deals_2018[['SQM', 'Agency']]
    all_deals_2018['Percent'] = (all_deals_2018[['SQM']] / all_deals_2018['SQM'].sum()) * 100
    all_deals_2018 = all_deals_2018.groupby('Agency', as_index=False).sum()
    all_deals_2018['SQM'] = all_deals_2018['SQM'].apply(np.round).astype(int)
    all_deals_2018['Percent'] = all_deals_2018['Percent'].apply(np.round).astype(int).astype(str) + '%'
    all_deals_2018 = all_deals_2018.sort_values('SQM', ascending=False)

    nan_df = pd.DataFrame(
        {'Agency': [np.nan],
         'SQM': [all_deals_2018['SQM'].sum()],
         'Percent': [np.nan]
         })
    all_deals_2018 = pd.concat((all_deals_2018, nan_df))
    return table_for_pres_sale_lease_ru(all_deals_2018)


def table_for_pres_lease_ru(dataframe, max_rows=10):
    """ФУНКЦИЯ ОТРИСОВКИ ТАБЛИЦЫ ЧЕРЕЗ  HTML, ДЛЯ НАСТРОЙКИ СТИЛЯ ИСПОЛЬЗУЕТСЯ CSS РАЗМЕТКА"""
    return html.Div(
        [
            html.Table(
                [
                    html.Tr(  # HEADER
                        [
                            html.Th(
                                col,
                                style={
                                    'text-align': 'center',
                                    'width': wid,
                                    'font-size': '10pt',
                                    'font-weight': ['bold']
                                }
                            )
                            for col, wid in zip([" ", "Объём, кв. м", "Доля в объёме"],
                                                ['95px', '105px', '100px']
                                                )
                        ],
                        style={  # CSS разметка
                            'background-color': color.colliers_light_blue,
                            'color': color.white,
                            'allign': 'left',
                            # "padding-left": "50px",
                            'font-size': '12pt'

                        }
                    )
                ]
                +
                [
                    html.Tr(  # BODY
                        [
                            html.Td(dataframe.iloc[i][col],
                                    style={
                                        'text-align': 'right',
                                        'width': wid,
                                        "min-height": "15px",
                                        'font-size': '10pt',
                                        'border': '0px',
                                        'border-bottom': '1px solid {}'.format(color.colliers_grey_10)

                                    }
                                    )
                            for col, wid in zip(dataframe.columns,
                                                ['100px', '100px', '100px']
                                                )
                        ],
                        style={  # CSS разметка
                            # 'background-color': color.colliers_pale_blue,
                            'allign': 'left',
                            'margin-left': '50px',
                            # "padding-left": "50px",
                            "min-height": "15px",

                        }
                    ) for i in range(min(len(dataframe), max_rows))]
            )
        ],
        # style={
        #     'line-height': '12px',
        #     'padding': '12px 0px'
        #      'height': '12px'
        # }
    )


def generate_table_for_pres_lease_ru():  # pie по ДОЛЯ РЫНКА ПО РОССИИ В 1 КВ. 2018 ВСЕ СДЕЛКИ / СДЕЛКИ АРЕНДЫ
    all_deals_2018 = static.all_deals_query_df
    all_deals_2018 = all_deals_2018[
        (all_deals_2018['Year'].isin(['2018'])) & (all_deals_2018['Quarter'].isin(['1'])) & (
            all_deals_2018['Country'].isin(['RU']))
        & (~all_deals_2018['Type_of_Deal'].isin(['Sale', 'Purchase']))]
    all_deals_2018 = all_deals_2018[['SQM', 'Agency']]
    all_deals_2018['Percent'] = (all_deals_2018[['SQM']] / all_deals_2018['SQM'].sum()) * 100
    all_deals_2018 = all_deals_2018.groupby('Agency', as_index=False).sum()
    all_deals_2018['SQM'] = all_deals_2018['SQM'].apply(np.round).astype(int)
    all_deals_2018['Percent'] = all_deals_2018['Percent'].apply(np.round).astype(int).astype(str) + '%'
    all_deals_2018 = all_deals_2018.sort_values('SQM', ascending=False)

    nan_df = pd.DataFrame(
        {'Agency': [np.nan],
         'SQM': [all_deals_2018['SQM'].sum()],
         'Percent': [np.nan]
         })
    all_deals_2018 = pd.concat((all_deals_2018, nan_df))
    return table_for_pres_lease_ru(all_deals_2018)
