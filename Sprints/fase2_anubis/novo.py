import os
os.system('cls' if os.name == 'nt' else 'clear')

import streamlit as st
import Files.Code.papelao as page_papelao
import Files.Code.hexano as page_hexano
import Files.Code.about as page_about
############################################################
def main():
    st.sidebar.image('https://github.com/zolpy/Hub-ia-senai-londrina-pr/blob/main/Sprints/fase2_anubis/Files/Images/anubis.jpg')
    menu = ["Papelão", "Hexano", "About"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Papelão":
        page_papelao.chamaPapelao()

    elif choice == "Hexano":
        page_hexano.chamaHexano()

    else:
        page_about.chamaAbout()

if __name__ == '__main__':
    main()
