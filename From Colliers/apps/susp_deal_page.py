import dash
import dash_html_components as html
import pandas as pd
from apps import static as static
from apps import methods as my_method

from app import app


# Начало блока кода по странице с 'сомнительными' сделками
# Графики не используютсяб есть тлько таблица с данными,
# отфильтрованными по  обговоренному критерию

@app.callback(dash.dependencies.Output('interface_susp', 'labelStyle'),
              # на вход принимается значение чеклиста 'colums'
              [dash.dependencies.Input('tree-checklist_susp', 'values')
               # если значение выбрано, то отрисовывается новый блок со списком, как в дереве
               ])
def show_tree(val):
    if 'Show' in val:
        children = {'display': 'block',
                    'width': '192px',
                    'margin': '0 0 0 10px',
                    }
    else:
        children = {'display': 'none'
                    }
    return children


def select_drop_from_check_susp():
    @app.callback(dash.dependencies.Output('Include_in_Market_Share_Div_susp', 'style'),
                  # проверка checklist со значениями выбранных столбов в таблице
                  [dash.dependencies.Input('interface_susp', 'values')
                   # при выборе столбца добавляется выпадающий список
                   ])
    def update_drop_include(val):
        try:
            if 'Include_in_Market_Share' in val:
                style_include = {'display': 'inline-block',
                                 'width': '80px',
                                 }

            if 'Include_in_Market_Share' not in val:
                style_include = {'display': 'none',
                                 'width': '80px',
                                 }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_include

    @app.callback(dash.dependencies.Output('Agency_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_agency(val):
        try:
            if 'Agency' in val:
                style_agency = {'display': 'inline-block',
                                'width': '80px',
                                }

            if 'Agency' not in val:
                style_agency = {'display': 'none',
                                'width': '80px',
                                }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_agency

    @app.callback(dash.dependencies.Output('Country_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_country(val):
        try:
            if 'Country' in val:
                style_country = {'display': 'inline-block',
                                 'width': '80px',
                                 }

            if 'Country' not in val:
                style_country = {'display': 'none',
                                 'width': '80px',
                                 }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_country

    @app.callback(dash.dependencies.Output('City_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_city(val):
        try:
            if 'City' in val:
                style_city = {'display': 'inline-block',
                              'width': '80px',
                              }

            if 'City' not in val:
                style_city = {'display': 'none',
                              'width': '80px',
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_city

    @app.callback(dash.dependencies.Output('Property_name_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_property_name(val):
        try:
            if 'Property_Name' in val:
                style_property_name = {'display': 'inline-block',
                                       'width': '80px',
                                       }

            if 'Property_Name' not in val:
                style_property_name = {'display': 'none',
                                       'width': '80px',
                                       }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_property_name

    @app.callback(dash.dependencies.Output('Class_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_class(val):
        try:
            if 'Class' in val:
                style_class = {'display': 'inline-block',
                               'width': '80px',
                               }

            if 'Class' not in val:
                style_class = {'display': 'none',
                               'width': '80px',
                               }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_class

    @app.callback(dash.dependencies.Output('SQM_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_SQM(val):
        try:
            if 'SQM' in val:
                style_SQM = {'display': 'inline-block',
                             'width': '80px',
                             }

            if 'SQM' not in val:
                style_SQM = {'display': 'none',
                             'width': '80px',
                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_SQM

    @app.callback(dash.dependencies.Output('Company_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Company(val):
        try:
            if 'SQM' in val:
                style_Company = {'display': 'inline-block',
                                 'width': '80px',
                                 }

            if 'SQM' not in val:
                style_Company = {'display': 'none',
                                 'width': '80px',
                                 }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Company

    @app.callback(dash.dependencies.Output('Business_Sector_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Business_Sector(val):
        try:
            if 'Business_Sector' in val:
                style_Business_Sector = {'display': 'inline-block',
                                         'width': '80px',
                                         }

            if 'Business_Sector' not in val:
                style_Business_Sector = {'display': 'none',
                                         'width': '80px',
                                         }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Business_Sector

    @app.callback(dash.dependencies.Output('Type_of_Deal_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Type_of_Deal(val):
        try:
            if 'Type_of_Deal' in val:
                style_Type_of_Deal = {'display': 'inline-block',
                                      'width': '80px',
                                      }

            if 'Type_of_Deal' not in val:
                style_Type_of_Deal = {'display': 'none',
                                      'width': '80px',
                                      }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Type_of_Deal

    @app.callback(dash.dependencies.Output('Type_of_Consultancy_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Type_of_Consultancy(val):
        try:
            if 'Type_of_Consultancy' in val:
                style_Type_of_Consultancy = {'display': 'inline-block',
                                             'width': '80px',
                                             }

            if 'Type_of_Consultancy' not in val:
                style_Type_of_Consultancy = {'display': 'none',
                                             'width': '80px',
                                             }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Type_of_Consultancy

    @app.callback(dash.dependencies.Output('LLR/TR_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Type_of_Consultancy(val):
        try:
            if 'LLR_TR' in val:
                style_LLR_TR = {'display': 'inline-block',
                                'width': '80px',
                                }

            if 'LLR_TR' not in val:
                style_LLR_TR = {'display': 'none',
                                'width': '80px',
                                }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_LLR_TR

    @app.callback(dash.dependencies.Output('Year_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Year(val):
        try:
            if 'Year' in val:
                style_Year = {'display': 'inline-block',
                              'width': '80px',
                              }

            if 'Year' not in val:
                style_Year = {'display': 'none',
                              'width': '80px',
                              }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Year

    @app.callback(dash.dependencies.Output('Quarter_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Quarter(val):
        try:
            if 'Quarter' in val:
                style_Quarter = {'display': 'inline-block',
                                 'width': '80px',
                                 }
            if 'Quarter' not in val:
                style_Quarter = {'display': 'none',
                                 'width': '80px',
                                 }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Quarter

    @app.callback(dash.dependencies.Output('Address_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Address(val):
        try:
            if 'Address' in val:
                style_Addres = {'display': 'inline-block',
                                'width': '80px',
                                }

            if 'Address' not in val:
                style_Addres = {'display': 'none',
                                'width': '80px',
                                }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Addres

    @app.callback(dash.dependencies.Output('Submarket_Large_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Submarket_large(val):
        try:
            if 'Submarket_Large' in val:
                style_Submarket_Large = {'display': 'inline-block',
                                         'width': '80px',
                                         }

            if 'Submarket_Large' not in val:
                style_Submarket_Large = {'display': 'none',
                                         'width': '80px',
                                         }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Submarket_Large

    @app.callback(dash.dependencies.Output('Owner_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Owner(val):
        try:
            if 'Owner' in val:
                style_Owner = {'display': 'inline-block',
                               'width': '80px',
                               }

            if 'Owner' not in val:
                style_Owner = {'display': 'none',
                               'width': '80px',
                               }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Owner

    @app.callback(dash.dependencies.Output('Date_of_acquiring_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Date_of_acquiring(val):
        try:
            if 'Date_of_acquiring' in val:
                style_Date_of_acquiring = {'display': 'inline-block',
                                           'width': '80px',
                                           }

            if 'Date_of_acquiring' not in val:
                style_Date_of_acquiring = {'display': 'none',
                                           'width': '80px',
                                           }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Date_of_acquiring

    @app.callback(dash.dependencies.Output('Class_Colliers_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Class_Colliers(val):
        try:
            if 'Class_Colliers' in val:
                style_Class_Colliers = {'display': 'inline-block',
                                        'width': '80px',
                                        }

            if 'Class_Colliers' not in val:
                style_Class_Colliers = {'display': 'none',
                                        'width': '80px',
                                        }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Class_Colliers

    @app.callback(dash.dependencies.Output('Floor_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Floor(val):
        try:
            if 'Floor' in val:
                style_Floor = {'display': 'inline-block',
                               'width': '80px',
                               }

            if 'Floor' not in val:
                style_Floor = {'display': 'none',
                               'width': '80px',
                               }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Floor

    @app.callback(dash.dependencies.Output('Deal_Size_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Deal_Size(val):
        try:
            if 'Deal_Size' in val:
                style_Deal_Size = {'display': 'inline-block',
                                   'width': '80px',
                                   }

            if 'Deal_Size' not in val:
                style_Deal_Size = {'display': 'none',
                                   'width': '80px',
                                   }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Deal_Size

    @app.callback(dash.dependencies.Output('Sublease_Agent_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Sublease_Agent(val):
        try:
            if 'Sublease_Agent' in val:
                style_Sublease_Agent = {'display': 'inline-block',
                                        'width': '80px',
                                        }

            if 'Sublease_Agent' not in val:
                style_Sublease_Agent = {'display': 'none',
                                        'width': '80px',
                                        }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Sublease_Agent

    @app.callback(dash.dependencies.Output('LLR_Only_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_LLR_Only(val):
        try:
            if 'LLR_Only' in val:
                style_LLR_Only = {'display': 'inline-block',
                                  'width': '80px',
                                  }

            if 'LLR_Only' not in val:
                style_LLR_Only = {'display': 'none',
                                  'width': '80px',
                                  }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_LLR_Only

    @app.callback(dash.dependencies.Output('E_TR_Only_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_E_TR_Only(val):
        try:
            if 'E_TR_Only' in val:
                style_E_TR_Only = {'display': 'inline-block',
                                   'width': '80px',
                                   }

            if 'E_TR_Only' not in val:
                style_E_TR_Only = {'display': 'none',
                                   'width': '80px',
                                   }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_E_TR_Only

    @app.callback(dash.dependencies.Output('LLR/E_TR_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_LLR_E_TR(val):
        try:
            if 'LLR/E_TR' in val:
                style_LLR_E_TR = {'display': 'inline-block',
                                  'width': '80px',
                                  }

            if 'LLR/E_TR' not in val:
                style_LLR_E_TR = {'display': 'none',
                                  'width': '80px',
                                  }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_LLR_E_TR

    @app.callback(dash.dependencies.Output('Month_Div_susp', 'style'),
                  [dash.dependencies.Input('interface_susp', 'values')
                   ])
    def update_drop_Month(val):
        try:
            if 'Month' in val:
                style_Month = {'display': 'inline-block',
                               'width': '80px',
                               }

            if 'Month' not in val:
                style_Month = {'display': 'none',
                               'width': '80px',
                               }
        except Exception as e:
            return html.Div([
                'There was an error'
            ])
        return style_Month


select_drop_from_check_susp()  # вызов функции с отображением выпадающих списков


@app.callback(dash.dependencies.Output('datatable-suspicious', 'rows'),
              [dash.dependencies.Input('Year_susp', 'value'),
               dash.dependencies.Input('Country_susp', 'value'),
               dash.dependencies.Input('Agency_susp', 'value'),
               dash.dependencies.Input('City_susp', 'value'),
               dash.dependencies.Input('Property_name_susp', 'value'),
               dash.dependencies.Input('Class_susp', 'value'),
               dash.dependencies.Input('SQM_susp', 'value'),
               dash.dependencies.Input('Business_Sector_susp', 'value'),
               dash.dependencies.Input('Type_of_Deal_susp', 'value'),
               dash.dependencies.Input('Type_of_Consultancy_susp', 'value'),
               dash.dependencies.Input('LLR/TR_susp', 'value'),
               dash.dependencies.Input('Quarter_susp', 'value'),
               dash.dependencies.Input('Company_susp', 'value'),
               dash.dependencies.Input('Include_in_Market_Share_susp', 'value'),
               dash.dependencies.Input('Address_susp', 'value'),
               dash.dependencies.Input('Submarket_Large_susp', 'value'),
               dash.dependencies.Input('Owner_susp', 'value'),
               dash.dependencies.Input('Date_of_acquiring_susp', 'value'),
               dash.dependencies.Input('Class_Colliers_susp', 'value'),
               dash.dependencies.Input('Floor_susp', 'value'),
               dash.dependencies.Input('Deal_Size_susp', 'value'),
               dash.dependencies.Input('Sublease_Agent_susp', 'value'),
               dash.dependencies.Input('LLR_Only_susp', 'value'),
               dash.dependencies.Input('E_TR_Only_susp', 'value'),
               dash.dependencies.Input('LLR/E_TR_susp', 'value'),
               dash.dependencies.Input('Month_susp', 'value'),
               dash.dependencies.Input('interface_susp', 'values')  # значение чеклиста из дерева с выбором столбцов
               ])
def update_datatable_susp(Year, Country, Agency, City, Property_Name, Class, SQM, Business_Sector, Type_of_Deal,
                          Type_of_Consultancy, LLR_TR, Quarter, Company, Include_in_Market_Share, Address,
                          Submarket_Large, Owner, Date_of_acquiring, Class_Colliers, Floor, Deal_Size, Sublease_Agent,
                          LLR_Only, E_TR_Only, LLR_E_TR, Month, col):
    cond = dict(Year=[Year], Country=[Country], Agency=[Agency],
                City=[City], Property_Name=[Property_Name], Class=[Class],
                SQM=[SQM], Company=[Company], Business_Sector=[Business_Sector],
                Type_of_Deal=[Type_of_Deal], Type_of_Consultancy=[Type_of_Consultancy],
                LLR_TR=[LLR_TR], Quarter=[Quarter], Include_in_Market_Share=[Include_in_Market_Share],
                Address=[Address], Submarket_Large=[Submarket_Large], Owner=[Owner],
                Date_of_acquiring=[Date_of_acquiring], Class_Colliers=[Class_Colliers],
                Floor=[Floor], Deal_Size=[Deal_Size], Sublease_Agent=[Sublease_Agent],
                LLR_Only=[LLR_Only], E_TR_Only=[E_TR_Only], LLR_E_TR=[LLR_E_TR], Month=[Month])

    list_of_values = (Year, Country, Agency, City, Property_Name, Class, SQM, Business_Sector, Type_of_Deal,
                      Type_of_Consultancy, LLR_TR, Quarter, Company, Include_in_Market_Share, Address, Submarket_Large,
                      Owner,
                      Date_of_acquiring, Class_Colliers, Floor, Deal_Size, Sublease_Agent, LLR_Only, E_TR_Only,
                      LLR_E_TR,
                      Month)
    cond_1 = cond.copy()
    list_of_values_copy = list(filter(None, list_of_values))

    suspecious_deals_df_equal_sqm = static.all_deals_query_df[
        static.all_deals_query_df.duplicated(['SQM'], keep=False)].sort_values(
        'SQM', ascending=False)

    sort_for_dif = static.all_deals_query_df.sort_values('SQM', ascending=False)
    suspecious_deals_df_sqm_diff_less_five = sort_for_dif[sort_for_dif['SQM'].diff() < 5]

    suspecious_deals_df_merged_by_equal_and_diff = pd.merge(suspecious_deals_df_equal_sqm,
                                                            suspecious_deals_df_sqm_diff_less_five, how='inner')
    # ##print('merged')
    # ##print(suspecious_deals_df_merged_by_equal_and_diff)

    # suspecious_deals_df_sqm_diff_year = sort_for_dif[sort_for_dif['Year'].diff() <= 1]
    # suspecious_deals_df_sqm_diff_year_sorted = suspecious_deals_df_sqm_diff_year.sort_values('Year', ascending=False)
    # ###print('suspecious_deals_df_sqm_diff_year_sorted')
    # ###print(suspecious_deals_df_sqm_diff_year_sorted)

    sort_for_dif = static.all_deals_query_df.sort_values('Quarter', ascending=False)
    suspecious_deals_df_quar_diff = sort_for_dif[sort_for_dif['Quarter'].diff() <= 2]

    suspecious_deals_df_merged_by_equal_year_qurter_diff = pd.merge(suspecious_deals_df_merged_by_equal_and_diff,
                                                                    suspecious_deals_df_quar_diff, how='inner')

    suspecious_deals_total = suspecious_deals_df_merged_by_equal_year_qurter_diff

    if len(list_of_values_copy) == 0:
        return suspecious_deals_total[col].to_dict('records')
    if len(list_of_values_copy) != 0:
        for i in range(len(list_of_values_copy)):
            ind = my_method.get_key(cond_1, [list_of_values_copy[i]])
            if i == 0:
                data = suspecious_deals_total[(suspecious_deals_total[ind].isin(list_of_values_copy[i]))]
            else:
                data = suspecious_deals_total[(suspecious_deals_total[ind].isin(list_of_values_copy[i]))]
        return data[col].to_dict('records')
