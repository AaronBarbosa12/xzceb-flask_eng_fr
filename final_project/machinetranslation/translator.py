import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    model_id = "en-fr"

    if english_text is not None:
        french_text = language_translator.translate(
            text=english_text, model_id=model_id
        ).get_result()["translations"][0]["translation"]
        return french_text
    else:
        return None 

def french_to_english(french_text):
    model_id = "fr-en"

    if french_text is not None:        
        english_text = language_translator.translate(
            text=french_text, model_id=model_id
        ).get_result()["translations"][0]["translation"]
        return english_text
    else:
        return None