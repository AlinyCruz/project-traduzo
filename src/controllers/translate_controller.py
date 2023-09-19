from flask import Blueprint, render_template, request

from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        languages = LanguageModel.list_dicts()
        text_to_translate = "O que deseja traduzir"
        translated = "Tradução"

        return render_template(
            "index.html",
            languages=languages,
            translate_from="pt",
            translate_to="en",
            text_to_translate=text_to_translate,
            translated=translated,
        )

    elif request.method == "POST":
        languages = LanguageModel.list_dicts()
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        translated2 = GoogleTranslator(
            source=translate_from, target=translate_to
        )
        translated3 = translated2.translate(text_to_translate)

        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated3,
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translator2 = GoogleTranslator(
        source=translate_from, target=translate_to
    )
    translator3 = translator2.translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=translator3,
    )
