import dash
import plotly.plotly as py
from apps import methods as my_method


app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True


def css_and_js_external():

    """Мой файл с гитхаба на rawgit с измененной css разметкой и файл с JS
    скриптами от разработчиков Dash."""
    #app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
    #app.css.append_css({'external_url': 'https://rawgit.com/Wittgensteen/work_stuff/master/new_buttons.css'})

    external_js = [
        "https://code.jquery.com/jquery-3.2.1.min.js",
        "https://codepen.io/bcd/pen/YaXojL.js",
        # "https://rawgit.com/Wittgensteen/work_stuff/master/html2canvas.js",
        "https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js",
        # "https://rawgit.com/Wittgensteen/work_stuff/master/download_screen_1.js",
        # "https://cdn.rawgit.com/Wittgensteen/work_stuff/master/screnn_js_no_can_clic_1.js",
        # "https://rawgit.com/taylorhakes/promise-polyfill/master/dist/polyfill.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.min.js",
        # 'https://rawgit.com/Wittgensteen/work_stuff/master/h2calpha.js',
        # "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.min.js",
        "https://raw.githubusercontent.com/taylorhakes/promise-polyfill/master/dist/polyfill.min.js",
        "https://rawgit.com/Wittgensteen/work_stuff/master/genScr.js"

    ]

    for js in external_js:
        app.scripts.append_script({"external_url": js})

    external_css = [
        "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        # "https://codepen.io/bcd/pen/KQrXdb.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
        "https://rawgit.com/Wittgensteen/work_stuff/master/mod_css_new.css",
        "https://rawgit.com/Wittgensteen/work_stuff/master/for_print.css"
    ]

    for css in external_css:
        app.css.append_css({"external_url": css})


def login():
    """Вход в аккаунт Plotly для получения доступа к API"""

    py.sign_in('Barbrady', 'V11sgDqsmE4XpTsVGoFJ')  # вход в аккаунт на plotly Дима

    try:
        py.image.get(my_method.test_account_plotly(), format='png')
    except Exception:
        py.sign_in('Wittgensteen', 'D9dEx9VG7SfqBlkoDvRl')  # вход в аккаунт на plotly Юра
    else:
        py.sign_in('account3', 'veeX6RS30XT7zhj1ULy4')  # вход в аккаунт на plotly фейк


css_and_js_external()


login()
