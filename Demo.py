import streamlit as st

st.set_page_config(layout="wide")

dark_green = "#0a3041"
light_yellow = "#ffffc5"
yellow= "#ffff00"
white = "#ffffff"


cols = st.columns([0.7,0.3])
with cols[0]:
    st.image("logo.png", caption="")
with cols[1]:
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=400, caption = "Developed with Streamlit")

    

st.write(f"""
<style>
    div .st-emotion-cache-4uzi61 {{

        background-color:{dark_green};
        border-color: {dark_green};
    }}
</style>
""",
    unsafe_allow_html=True,
)



with st.container(border = True):

    columns = st.columns([0.2,0.4,0.4], vertical_alignment="center")
    with columns[0]:

        st.markdown(f"""<p style="font-family:Trebuchet MS;
        background-color:{light_yellow};
        color:{dark_green}; font-size: 70px;
            font-weight: bold;
            text-align: center;
            vertical-align: middle;
                padding-top: 70%;
            height: 570px;
        ">10 <br> - </p>""", unsafe_allow_html = True)




    with columns[1]:


            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 30px;
                text-align: left;
                text-weight: bold;
            ">T. CONCHA - C20012345678 <br><br></p>""", unsafe_allow_html = True)


            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 20px;
                text-align: left;
            ">Cliente - Sold To</p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{yellow}; font-size: 30px;
                text-align: left;
            ">Walmart - Lo Aguirre<br><br> </p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 20px;
                text-align: left;
            ">Estatus</p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{yellow}; font-size: 30px;
                text-align: left;
            ">Preparación<br>
                (80%)<br><br></p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 20px;
                text-align: left;
            ">Tipo de viaje</p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{yellow}; font-size: 30px;
                text-align: left;
            ">Bodega Central</p>""", unsafe_allow_html = True)
    with columns[2]:


            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 30px;
                text-align: left;
                text-weight: bold;
            "> <br> <br>         </p>""", unsafe_allow_html = True)


            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 20px;
                text-align: left;
            ">Fecha / Hora Camión Cargado</p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{yellow}; font-size: 30px;
                text-align: left;
            ">02-01-2025 / 15:40 hrs</p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 20px;
                text-align: left;
            "> <br><br>Fecha / Hora Agenda</p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{yellow}; font-size: 30px;
                 text-align: left;
            ">02-01-2025 / 17:00 hrs <br><br> </p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:{white}; font-size: 20px;
                text-align: left;
            "><br>Cumplimiento</p>""", unsafe_allow_html = True)

            st.markdown(f"""<p style="font-family:Trebuchet MS;
            background-color:{dark_green};
            color:#4ea72e; font-size: 30px;
                text-align: left;
            ">ON TIME</p>""", unsafe_allow_html = True)