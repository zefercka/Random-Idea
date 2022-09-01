import os
import locale
# для изменения кодировки

from app import app
from flask import render_template
from flask import redirect
from flask import request
from flask import make_response
# импорт библиотек для сервера
from app.theme_load import themes as th
# темы
import random

import pymorphy2

morph = pymorphy2.MorphAnalyzer()
# Запуск инструмента для нормальных склонений

os.environ["PYTHONIOENCODING"] = "utf-8"
scriptLocale = locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8")
# Смена кодировки


@app.route("/")
def main_page():
    return render_template("index.html", themes=th.keys())
# Возвращает главную страницу


@app.route("/about-us")
def about_us():
    return render_template("about-us.html")
# Возвращает страницу о нас


@app.route("/how-work")
def how_work():
    return render_template("how-work.html")
# Возвращает страницу как это работает


@app.route("/generator", methods=['GET'])
def generation():
    query = request.args.get('theme') # Поулчаем аргумент для обработки (тему)

    while True:
        try:
            noun = th[query]['сущ'][random.randint(0, len(th[query]['сущ']) - 1)]
            adj = th[query]['прил'][random.randint(0, len(th[query]['прил']) - 1)]
            # Рандом сущ и прил

            gender = morph.parse(noun)[0].tag.gender
            number = morph.parse(noun)[0].tag.number
            # Получаем род и число сущ

            response = f"{morph.parse(adj)[0].inflect({gender, number}).word}+{noun}"
            # прил в нужной форме + сущ
            break
        except:
            continue

    return make_response(response)
    # Возвращает два слова
