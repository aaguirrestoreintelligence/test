import streamlit as st
import time
import random
import numpy as np
import pandas as pd


st.set_page_config(layout="wide")

#carga de datos
data = pd.read_csv('Dataframe_muestra_aeropuerto.csv')
#st.write(data)


#Colores:
azul_Claro = '#6EC1E4' #Fondo principal, encabezados suaves
azul_Oscuro = '#003B6F' #Barras laterales, títulos destacados
Blanco = '#FFFFFF' #Texto sobre fondos oscuros
Naranja = '#F7941D' #Indicadores de alerta o progreso
Rojo = '#D62828' #Advertencias o errores
Amarillo = '#FDCB2E' #Éxitos, logros o métricas clave
Gris_Claro = '#C0C0C0' #Líneas divisorias, bordes sutiles

#Añadidos:
Soft_Green = '#38B000' # Adds a fresh, natural touch.
Rich_Purple = '#845EC2' # Provides depth and contrast.
Vibrant_Pink = '#FF6F91' # A bold accent for energy.
Deep_Teal = '#264653' # Balances and enriches blues.
Warm_Beige = '#E4DCCF' # Soft neutral for versatility.
Muted_Orange = '#F4A261' # Enhances the warmth of #F7941D.
Dark_Indigo = '#1D3557' # Strengthens depth alongside #003B6F.
red_alert = '#C41E3A'
#Variables
size_info_right_size = 2.2
color_background = '#C3E0E5'
color_left_side_card = '#E3D7A3'# 'rgb(244, 250, 120)'

time_seconds_change = 25


#.st-emotion-cache-1yiq2ps, .st-emotion-cache-12fmjuu, .st-emotion-cache-1fvrkc
# Define CSS for background color
# Inject CSS using markdown
st.markdown(f"""
    <style>
    div .stMain, .stAppHeader {{
            background-color: {color_background} !important;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"""
    <style>
    div .st-emotion-cache-vlxhtx {{
            gap: 0rem !important;
        }}
    </style>
""", unsafe_allow_html=True)

def individual_card(color_left_side_card, number_data, color_left=azul_Oscuro,background_color_right=Dark_Indigo):
    st.markdown(f"""<style>
    .rectangle_individual {{
        display: grid;
        grid-template-columns: 0.65fr 1.2fr 1.1fr; /* Creates 3 equal columns */
        height: 85vh;
        padding: 0;
        width: 94vw;
        background-color: {color_background};
        box-shadow: 0.5vw 0.5vw 1vw rgba(0, 0, 0, 0.8); /* Creates the shadow effect */
        border-radius: 1vw; /* Adds soft corners */
        
            }}

        .column_individual {{
            padding: 0;
            margin: 0;
            text-align: center;
            color: white;
            font-weight: bold;
        }}
        </style>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="rectangle_individual">
    <div class="column_individual" style="background-color:{color_left_side_card};
            color:{color_left}; 
            font-size: 5vw;
            font-weight: {'bold'};
            text-align: center;
            vertical-align: middle;
            padding-top: 30%;
            height: 100%;
            border-radius: 1vw 0vw 0vw 1vw;
            ">Anden <br> {data['anden'].values[number_data]} <br>
            Muelle <br> {data['muelle'].values[number_data]} <br>
            </div>
            
    <div class="column_individual" style="font-family:Trebuchet MS;
            background-color:{Dark_Indigo};
            color:{Blanco};
            font-size: {size_info_right_size}vw;
            text-align: left;
            text-weight: bold;
            padding-top: 1vw;
            padding-left: 1vw;
            line-height: 2.5;
            "><span style="font-size: 3.5vw; padding-left: 1vw; color: {Amarillo};">{data['cod_carga'].values[number_data]}</span>   
            Cumplimiento: <span style="color: white;
            background-color: {red_alert if data['cumplimiento'].values[number_data] !='On time' else Soft_Green};
            padding: 1vw;
            border-radius: 1vw;">
            {data['cumplimiento'].values[number_data]} </span><br>    
            Estatus: <span style="color: white;
            background-color: {red_alert if data['cumplimiento'].values[number_data] !='On time' else Soft_Green};
            padding: 1vw;
            border-radius: 1vw;">{data['estatus'].values[number_data]}</span><br>    
            <br> 
            Nombre transporte: {data['nombre_transporte'].values[number_data]} <br>  
            Presentación anden:  <span style="color: {Naranja}; ">{data['presentacion_anden'].values[number_data]}  </span><br>     
            Camión cargado:  <span style="color: {Naranja};  ">{data['camion_cargado'].values[number_data]}  </span><br>      
            </div>
    <div class="column_individual" style="font-family:Trebuchet MS;
            background-color:{Dark_Indigo};
            color:{Blanco};
            font-size: {size_info_right_size}vw;
            text-align: left;
            text-weight: bold;
            padding-top: 9vw;
            padding-left: 0.005vw;
            line-height: 2.5;
            border-radius: 0 1vw  1vw 0;
            ">{data['cliente'].values[number_data]}     
            <br>Picking:<span style="color: {Naranja};  ">{data['picking'].values[number_data]}</span>
            - Full Pallet: <span style="color: {Naranja};  "> {data['full_pallet'].values[number_data]}</span>     
            <br> Total post: <span style="color: {Naranja};  "> {data['total_post'].values[number_data]}</span> <br>   
    </div>""", unsafe_allow_html=True)


st.markdown(f"""<style>
.rectangle_multiple {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* Creates 3 equal columns */
    grid-template-rows: 1fr 1fr; /* Creates 2 equal rows */
    height: 87vh;
    padding: 0vw;
    width: 95vw;
    background-color: {color_background};
    //box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.8); /* Creates the shadow effect */
    border-radius: 1vw; /* Adds soft corners */
        }}

    .cell {{
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: darkblue;
    border-radius: 1vw; /* Optional: rounds the corners */
    }}
    </style>
    """, unsafe_allow_html=True)

st.write(f"""<style>
        .rectangle_individual_multiple {{
        display: grid;
        grid-template-columns: 0.65fr 1.2fr 1.1fr; /* Creates 3 equal columns */
        height: 40vh;
        padding: 0vw;
        width: 31vw;
        background-color: {color_background};
        box-shadow: 0.5vw 0.5vw 1vw rgba(0, 0, 0, 0.8); /* Creates the shadow effect */
        border-radius: 1vw; /* Adds soft corners */ }}
        .column_individual_multiple {{
            padding: 0.5vw;
            margin: 0;
            text-align: center;
            color: white;
            font-weight: bold;
            height: 40vh;
            font-size: 0.9vw;
            font-weight: {'bold'};
        }}
            </style>""", unsafe_allow_html=True)

def individual_cell_for_6_pack(number_data):

    return f"""
    <div class="rectangle_individual_multiple">
    <div class="column_individual_multiple" style="background-color:{color_left_side_card};
            color:{azul_Oscuro}; 
            text-align: center;
            vertical-align: middle;
            padding-top: 50%;
            border-radius: 1vw 0vw 0vw 1vw;
            font-size: 1.8vw;
            ">Anden <br> {data['anden'].values[number_data]} <br>
            Muelle <br> {data['muelle'].values[number_data]} <br>
            </div>       
    <div class="column_individual_multiple" style="font-family:Trebuchet MS;
            background-color:{Dark_Indigo};
            color:{Blanco};
            text-align: left;
            text-weight: bold;
            padding-top: 1vw;
            padding-left: 1vw;
            line-height: 2;
            "><span style="font-size: 1.8vw; padding-left: 1vw; color: {Amarillo};">{data['cod_carga'].values[number_data]}</span>   
            Cumplimiento: <span style="color: white;
            background-color: {red_alert if data['cumplimiento'].values[number_data] !='On time' else Soft_Green};
            padding: 0.2vw;
            border-radius: 0.2vw;">
            {data['cumplimiento'].values[number_data]} </span><br>    
            Estatus: <span style="color: white;
            background-color: {red_alert if data['cumplimiento'].values[number_data] !='On time' else Soft_Green};
            padding: 0.2vw;
            border-radius: 0.2vw;">{data['estatus'].values[number_data]}</span><br>   
            <br> 
            Nombre transporte: {data['nombre_transporte'].values[number_data]} <br>  
            Presentación anden:  <span style="color: {Naranja}; ">{data['presentacion_anden'].values[number_data]}  </span><br>     
            Camión cargado:  <span style="color: {Naranja};  ">{data['camion_cargado'].values[number_data]}  </span><br>      
            </div>
    <div class="column_individual_multiple" style="font-family:Trebuchet MS;
            background-color:{Dark_Indigo};
            color:{Blanco};
            text-align: left;
            padding-top: 11vh;
            padding-left: 0.005vw;
            line-height: 2.5;
            border-radius: 0 1vw  1vw 0;
            ">{data['cliente'].values[number_data]}     
            <br>Picking:<span style="color: {Naranja};  ">{data['picking'].values[number_data]}</span>
            <br> Full Pallet: <span style="color: {Naranja};  "> {data['full_pallet'].values[number_data]}</span>     
            <br> Total post: <span style="color: {Naranja};  "> {data['total_post'].values[number_data]}</span> <br>   
    </div></div>"""


number_data_t= 22



        #change display every time_seconds_change:
changed_page = True

# Initialize session state

if "last_updated" not in st.session_state:
    st.session_state.last_updated = time.time()
    st.session_state.page = 0  # Track content changes

if st.session_state.page == 0:
    st.markdown(f"""
    <div class="rectangle_multiple">
    <div class="cell" style="">{individual_cell_for_6_pack(0)}</div>
    <div class="cell" style="">{individual_cell_for_6_pack(1)}</div>
    <div class="cell" style="">{individual_cell_for_6_pack(2)}</div>
    <div class="cell" style="">{individual_cell_for_6_pack(3)}</div>
    <div class="cell" style="">{individual_cell_for_6_pack(4)}</div>
    <div class="cell" style="">{individual_cell_for_6_pack(5)}</div>
    </div>
        """,unsafe_allow_html=True)

elif st.session_state.page == 1:
    individual_card(color_left_side_card,0, azul_Oscuro,Dark_Indigo)

elif st.session_state.page == 2:
    individual_card(color_left_side_card,1, azul_Oscuro,Dark_Indigo)

elif st.session_state.page == 3:
    individual_card(color_left_side_card,2, azul_Oscuro,Dark_Indigo)

elif st.session_state.page == 4:
    individual_card(color_left_side_card,3, azul_Oscuro,Dark_Indigo)

elif st.session_state.page == 5:
    individual_card(color_left_side_card,4, azul_Oscuro,Dark_Indigo)

elif st.session_state.page == 6:
    individual_card(color_left_side_card,5, azul_Oscuro,Dark_Indigo)


while changed_page:
    # Continuously update the timestamp

    time.sleep(1)  # Wait 1 second before refreshing
    if time.time() - st.session_state.last_updated > time_seconds_change:
        st.session_state.page = (st.session_state.page + 1) % 7  # Cycle through pages
        st.session_state.last_updated = time.time()
        changed_page = False
        st.rerun()  # Updated Streamlit rerun method
    else:
        changed_page = True

