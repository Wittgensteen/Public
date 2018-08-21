import dash
import dash_html_components as html
from apps import colors_and_fonts as color
from apps import static as static
import pandas as pd
import plotly.graph_objs as go


def get_key(d, value):
    """ФУНКЦИЯ ВОЗВРАЩЕНИЯ ИМЕНИ КЛЮЧА В СЛОВАРЕ ПО ЗНАЧЕНИЮ"""
    for k, v in d.items():
        if v == value:
            return k


def replace_index(list_of_ind):
    """ФУНКЦИЯ УБИРАЕТ НИЖНИЕ ПОДЧЕРКИВАНИЯ В НАЗВАНИИ ИНДЕКСОВ ДЛЯ ВЫВОДА НА ЭКРАН"""
    list_of_ind = [w.replace('Property_Name', 'Property name') for w in list_of_ind]
    list_of_ind = [w.replace('Business_Sector', 'Business sector') for w in list_of_ind]
    list_of_ind = [w.replace('Type_of_Deal', 'Type of deal') for w in list_of_ind]
    list_of_ind = [w.replace('Type_of_Consultancy', 'Type of consultancy') for w in list_of_ind]
    list_of_ind = [w.replace('LLR_TR', 'LLR/TR') for w in list_of_ind]
    list_of_ind = [w.replace('Include_in_Market_Share', 'Include in market share') for w in list_of_ind]
    list_of_ind = [w.replace('Submarket_Large', 'Submarket') for w in list_of_ind]
    list_of_ind = [w.replace('Date_of_acquiring', 'Date of acquiring') for w in list_of_ind]
    list_of_ind = [w.replace('Class_Colliers', 'Class Colliers') for w in list_of_ind]
    list_of_ind = [w.replace('Deal_Size', 'Deal size') for w in list_of_ind]
    list_of_ind = [w.replace('Sublease_Agent', 'Sublease agent') for w in list_of_ind]
    list_of_ind = [w.replace('LLR_Only', 'LLR') for w in list_of_ind]
    list_of_ind = [w.replace('E_TR_Only', '(E)TR') for w in list_of_ind]
    list_of_ind = [w.replace('LLR_E_TR', 'LLR/(E)TR') for w in list_of_ind]
    print(list_of_ind)
    return list_of_ind


def data_to_table_preparation(llr_type, list_of_values_copy, cond_1, sale_type):
    """ФИЛЬТРУЕТ ДАННЫЕ ДЛЯ ТАБЛИЦЫ И ГРАФИКОВ ПО ЗНАЧЕНИЯМ, ВЫБРАННЫМ В ПОЛЕ СЛЕВА"""

    if 'All deals' in llr_type:
        data_to_table = static.all_deals_query_df
        if len(list_of_values_copy) != 0:
            for i in range(len(list_of_values_copy)):
                ind = get_key(cond_1, [list_of_values_copy[i]])
                data_to_table = data_to_table[(data_to_table[ind].isin(list_of_values_copy[i]))]
    if 'LLR' in llr_type:
        data_to_table = static.all_deals_query_df[static.all_deals_query_df['LLR_Only'].isin(['Y'])]
        if len(list_of_values_copy) != 0:
            for i in range(len(list_of_values_copy)):
                ind = get_key(cond_1, [list_of_values_copy[i]])
                data_to_table = data_to_table[(data_to_table[ind].isin(list_of_values_copy[i]))]
    if '(E)TR' in llr_type:
        data_to_table = static.all_deals_query_df[static.all_deals_query_df['E_TR_Only'].isin(['Y'])]
        if len(list_of_values_copy) != 0:
            for i in range(len(list_of_values_copy)):
                ind = get_key(cond_1, [list_of_values_copy[i]])
                data_to_table = data_to_table[(data_to_table[ind].isin(list_of_values_copy[i]))]
    if 'LLR/(E)TR' in llr_type:
        data_to_table = static.all_deals_query_df[static.all_deals_query_df['LLR/E_TR'].isin(['Y'])]
        if len(list_of_values_copy) != 0:
            for i in range(len(list_of_values_copy)):
                ind = get_key(cond_1, [list_of_values_copy[i]])
                data_to_table = data_to_table[(data_to_table[ind].isin(list_of_values_copy[i]))]
    if 'All LLR (include double)' in llr_type:
        data_to_table_double = static.all_deals_query_df[static.all_deals_query_df['LLR/E_TR'].isin(['Y'])]
        data_to_table_llr = static.all_deals_query_df[static.all_deals_query_df['LLR_Only'].isin(['Y'])]
        data_to_table = pd.concat([data_to_table_double, data_to_table_llr], join='outer')
        if len(list_of_values_copy) != 0:
            for i in range(len(list_of_values_copy)):
                ind = get_key(cond_1, [list_of_values_copy[i]])
                data_to_table = data_to_table[(data_to_table[ind].isin(list_of_values_copy[i]))]
    if 'All (E)TR (include double)' in llr_type:
        data_to_table_double = static.all_deals_query_df[static.all_deals_query_df['LLR/E_TR'].isin(['Y'])]
        data_to_table_etr = static.all_deals_query_df[static.all_deals_query_df['E_TR_Only'].isin(['Y'])]
        data_to_table = pd.concat([data_to_table_double, data_to_table_etr], join='outer')
        if len(list_of_values_copy) != 0:
            for i in range(len(list_of_values_copy)):
                ind = get_key(cond_1, [list_of_values_copy[i]])
                data_to_table = data_to_table[(data_to_table[ind].isin(list_of_values_copy[i]))]

    if "Sale" in sale_type:
        data_to_table_2 = data_to_table[data_to_table['Include_in_Market_Share'].isin(['Y']) &
                                        data_to_table['Type_of_Deal'].isin(['Sale', 'Purchase'])]
    if "Lease" in sale_type:
        data_to_table_2 = data_to_table[data_to_table['Include_in_Market_Share'].isin(['Y']) &
                                        ~data_to_table['Type_of_Deal'].isin(['Sale', 'Purchase'])]

    if "Sale and Lease" in sale_type:
        data_to_table_2 = data_to_table

    return data_to_table_2


def print_button():
    """Функция вызова кнопки Print PDF"""
    printButton = html.A(['Print PDF'], className="button no-print print",
                         style={'position': "absolute",
                                # 'top': '-40',
                                'right': '0'})
    return printButton


def test_account_plotly():
    """Функция проверки лимита на trial аккаунте plotly"""
    test_pie = go.Pie(values=[1,2,3],
                          labels=['LLR', '(E)TR', 'LLR/(E)TR'],
                          hoverinfo='label+value+percent',
                          textinfo='label+percent',
                          textposition='outside',
                          textfont=dict(
                              size=12),
                          marker=dict(
                                      line=dict(
                                          width=1
                                      )
                                      )
                          )
    image_data = {
        'data': [test_pie],
        'layout': go.Layout(
            title='LLR, (E)TR and LLR/(E)TR deals in Russia<br>'
                          '1Q 2018',
            width=200,
            height=200,
            legend=dict(orientation="h",
                        traceorder="normal"),
        )
    }
    return image_data


