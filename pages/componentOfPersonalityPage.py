import streamlit as st
from component import divider
from component.font import customText

def show_content():
    customText.subheaderNoLink("Big Five Personalit")
    divider.space(40)

    customText.boldNoLink("What is PERSONALITY?")
    customText.regularNoLink("Allport, G. W. (1937). Personality: a psychological interpretation. Holt.")
    customText.link("https://archive.org/details/in.ernet.dli.2015.155561/page/n45/mode/2up", "https://archive.org/details/in.ernet.dli.2015.155561/page/n45/mode/2up")
    divider.space(40)

    customText.mixed_style_text("“Persona”","_ the theatrical mask first used in Greek drama")
    customText.italicNoLink("peri sô ma (around the body)")
    customText.italicNoLink("persum (head or face; the Etruscan and Old Latin).")
    customText.italicNoLink("per se una (self-containing; the Latin).®")
    divider.space(40)



show_content()




