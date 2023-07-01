"""
This module Translate English Language into French Language and vise versa
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translate text from english to french.
    """

    french_text = MyMemoryTranslator(source='en-IN', target="fr-FR").translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates the french language into English.
    """

    english_text = MyMemoryTranslator(source='fr-FR', target="en-IN").translate(french_text)
    print(english_text)
    return english_text
