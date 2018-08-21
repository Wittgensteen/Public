import dash
import base64
import io
import urllib
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd
from apps import static as static


from app import app


@app.callback(
    dash.dependencies.Output('download-example-button', 'href'),
    # формирования файла-шаблона с первой строкой - названием столбцов таблицы
    [dash.dependencies.Input('download-example-button', 'n_clicks')]
)
def example_button(n_clicks):
    data = pd.DataFrame.from_records([static.list_of_columns_for_example])  # создание датафрейма из списка заголовков столбца
    csv_string = data.to_csv(header=False, index=False, encoding='utf-8',
                             sep=';')  # формирование csv файла выбранной кодировкой и знаком разделения
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(
        csv_string)  # декодирование csv файла в байткод и запись в ссылку байткода для скачивани
    return csv_string  # возвращает сформированный байткод в строку-ссылку


def parse_contents(contents, filename):  # чтение загруженного файла, определение расширения,
    content_type, content_string = contents.split(',')  # разделителя и декодирование из байткода
    decoded = base64.b64decode(content_string + "==")
    try:
        if 'csv' in filename:
            #print('file is csv')
            df = pd.read_csv((io.StringIO(decoded.decode('utf-8'))), header=None)
            df.columns = df.iloc[0]
            print('data frame before drop index')
            print(df)
            df.drop(df.index[0], inplace=True)
            #print('data frame after drop index')
            #print(df)
        elif 'xls' in filename:  # проверка, является ли загруженный файл xls, не всегда работает корректно, так что пока лучше остановиться на csv
            print('file is xls')
            df = pd.read_excel((io.BytesIO(decoded)), header=None)
            df.columns = df.iloc[0]
            df.drop(df.index[0], inplace=True)
            print('data frame after drop index')
            print(df)
    except Exception as e:
        #print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return html.Div(
        [
            html.H5(filename),
            dt.DataTable(rows=df.to_dict('records'),
                         ),
        ]
    )


@app.callback(dash.dependencies.Output('output-data-upload', 'children'),  # отображение в таблице загруженных данных
              [dash.dependencies.Input('upload-data', 'contents'),
               dash.dependencies.Input('upload-data', 'filename'),
               ])
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children


def save_contents(contents_save, filename_save):
    """данные, загруженные в скрипт сохраняются в скрытом элементе страницы в
    json массиве, это необходимо для передачи данных между callback`ами.

    это решение - единственный способ передать данные без использования глобальных переменных
    """
    content_type, content_string = contents_save.split(',')
    decoded = base64.b64decode(content_string + "==")
    try:
        if 'csv' in filename_save:  # проверка, является ли загруженный файл csv
            print('yes, it`s csv')
            df = pd.read_csv((io.StringIO(decoded.decode('utf-8'))), header=None)
            print(df)
            df.columns = df.iloc[0]
            df.drop(df.index[0], inplace=True)
            json = df.to_json(date_format='iso', orient='split')
            print('json',json)
        elif 'xls' in filename_save:  # проверка, является ли загруженный файл xls
            df = pd.read_excel((io.BytesIO(decoded)), header=None)
            df.columns = df.iloc[0]
            df.drop(df.index[0], inplace=True)
            json = df.to_json(date_format='iso', orient='split')
    except Exception as e:
        print('Exception', e)
        return html.Div(
            ['Произошла ошибка при загрузке данных.'])

    return json


@app.callback(dash.dependencies.Output('intermediate-value', 'children'), # callback, выполняющий функцию "save_contents"
              [dash.dependencies.Input('upload-data', 'contents'),
               dash.dependencies.Input('upload-data', 'filename'),
               ])
def save_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            save_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children


@app.callback(dash.dependencies.Output('results', 'children'),  # сохранение данных из загруженного файла в БД
              [dash.dependencies.Input('intermediate-value', 'children')]
              )
def update_table(jsonified_cleaned_data):
    if jsonified_cleaned_data is not None:
        print(jsonified_cleaned_data)
        dff = pd.read_json(jsonified_cleaned_data[0], orient='split')
        dff.columns = static.list_of_columns_for_example
        dff.to_sql('Market_Share', static.con, if_exists='replace', index=None)
        return html.Div([
            'База успешно обновлена'
        ])
    else:
        html.Div([
            'Произошла ошибка при загрузке данных'
        ])