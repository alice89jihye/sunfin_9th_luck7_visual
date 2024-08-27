import streamlit as st
from component import divider
from component.font import customText

def show_content():
    customText.subheaderNoLink("Big Five Personalit")
    divider.space(40)

    customText.boldHNoLink("What is PERSONALITY?")
    customText.regular4NoLink("Allport, G. W. (1937). Personality: a psychological interpretation. Holt.", None, "16px", False)
    # customText.regular4IndentLink("https://archive.org/details/in.ernet.dli.2015.155561/page/n45/mode/2up", "https://archive.org/details/in.ernet.dli.2015.155561/page/n45/mode/2up", "#0000FF", "16px", "0px")
    divider.space(40)

    # customText.boldWithSubtext("“Persona”","_ the theatrical mask first used in Greek drama")
    customText.regular4NoLink("peri sô ma (around the body)", None, "16px", True)
    customText.regular4NoLink("persum (head or face; the Etruscan and Old Latin).", None, "16px", True)
    customText.regular4NoLink("per se una (self-containing; the Latin).®", None, "16px", True)
    divider.space(40)

show_content()




