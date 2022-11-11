import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

import re
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import graphviz as graphviz


# ---------------------Функция отрисовки нужного QR-кода---------------------
def show_required_qr_code(name_of_case: str):
    INIT_PATH = 'qr-codes/'
    if 'Автоматизация модерирования объявлений с помощью нейронных сетей' in name_of_case:
        qr_code_path = INIT_PATH + 'qr_code_moderation.png'
    elif 'Анализ рыночной корзины и ассоциативные правила' in name_of_case:
        qr_code_path = INIT_PATH + 'qr-code Анализ рыночной корзины.png'
    elif 'Базовые инструменты предварительной обработки данных' in name_of_case:
        qr_code_path = INIT_PATH + 'Базовые инструменты qr-код.png'
    elif 'Влияние обработки данных на точность прогноза' in name_of_case:
        qr_code_path = INIT_PATH + 'Влияние обработки данных qr-код.png'
    elif 'Выбор рациональной маркетинговой стратегии с использованием uplift-моделирования' in name_of_case:
        qr_code_path = INIT_PATH + 'qr-code Uplift modeling.png'
    elif 'Исследование надёжности заёмщиков при помощи деревьев решений' in name_of_case:
        qr_code_path = INIT_PATH + 'qr-code Деревья решений.png'
    elif 'Маркетинговые исследования с использованием A/B-тестирования' in name_of_case:
        qr_code_path = INIT_PATH + 'qr_code_AB_test.png'
    elif 'Обнаружение поддельных новостей искусственной нейронной сетью в исторических данных' in name_of_case:
        qr_code_path = INIT_PATH + 'qr-code Поддельные новости.png'
    elif 'Предсказание решений суда' in name_of_case:
        qr_code_path = INIT_PATH + 'Предсказание решений суда qr-код.png'
    elif 'Применение метода A/B-тестирования для проверки маркетинговых гипотез' in name_of_case:
        qr_code_path = INIT_PATH + 'qr_code_AB_test.png'
    elif 'Прогноз оттока банковских клиентов' in name_of_case:
        qr_code_path = INIT_PATH + 'Проноз оттока банковских клиентов qr-код.png'
    elif 'Разведочный анализ данных' in name_of_case:
        qr_code_path = INIT_PATH + 'Разведочный анализ данных.png'
    elif 'Распознавание рукописных букв' in name_of_case:
        qr_code_path = INIT_PATH + 'Распознавание рукописных букв qr-код.png'
    elif 'Распознавание рукописных цифр' in name_of_case:
        qr_code_path = INIT_PATH + 'qr-code Распознавание рукописных цифр.png'
    elif 'Распознавание текста с изображений' in name_of_case:
        qr_code_path = INIT_PATH + 'Распознавание текста с изображений qr-код.png'
    elif 'Сегментация изображений' in name_of_case:
        qr_code_path = INIT_PATH + 'qr_instance_segmentation.png'
    elif 'Статистический анализ показателей клиентов банка' in name_of_case:
        qr_code_path = INIT_PATH + 'Статистический анализ показателей клиентов банка qr-код.png'
    else:
        qr_code_path = INIT_PATH + 'ranepa_pattern.jpg'
    return qr_code_path


# ---------------------Header---------------------
st.markdown('''<h1 style='text-align: center; color: black;'
            >Универсальная модель цифровых компетенций</h1>''', 
            unsafe_allow_html=True)

main_table = pd.read_excel(open('вспомогательная таб для циф компетенций.xlsx', 'rb'), sheet_name='главная таблица') 

list_of_universities = sorted(list(main_table[main_table['Место обучения'].notnull()]['Место обучения'].unique()), reverse=False)

# ВЫБОР УНИВЕРСИТЕТА/ВУЗА/...:
choose_university = st.multiselect(('Выберите место обучения'), list_of_universities)

if choose_university:
    # ВЫБОР НАПРАВЛЕНИЯ:
    list_of_direction_of_study = sorted(list(main_table.loc[main_table['Место обучения']==choose_university[0]].reset_index()['Направление'].unique()), reverse=False)
    # list_of_direction_of_study = sorted(list(main_table[main_table['Направление'].notnull()]['Направление'].unique()), reverse=False)
    choose_direction_of_study = st.multiselect(('Выберите направление подготовки'), list_of_direction_of_study)

    if choose_direction_of_study:
        # ПОДБОР ВАКАНСИЙ ПО НАПРАВЛЕНИЮ:
        skills_table = pd.read_excel(open('вспомогательная таб для циф компетенций.xlsx', 'rb'), sheet_name='навыки таблица') 
        columns_with_vacancies = skills_table.columns.tolist()[-4:]
        list_of_vacancies = sorted(list(skills_table.loc[(skills_table['Направление']==choose_direction_of_study[0])].reset_index()['ссылки'].unique()), reverse=False) # ДОБАВИТЬ И ОСТАЛЬНЫЕ ЧЕРЕЗ columns_with_vacancies!!!!
        # st.write(list_of_vacancies)

        # ВЫБОР ПРОФИЛЯ:
        list_of_profiles= sorted(list(main_table.loc[(main_table['Место обучения']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0])].reset_index()['Профиль'].unique()), reverse=False)
        # st.write(list_of_profiles)
        choose_profile = st.multiselect(('Выберите профиль'), list_of_profiles)

        if choose_profile:
            # ВЫБОР ПРОФЕССИИ:
            list_of_professions = sorted(list(main_table.loc[(main_table['Место обучения']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Профессия'].unique()), reverse=False)
            unique_professions = []
            for professions_sequence in list_of_professions:
                proffessoions_names= professions_sequence.split('\n')
                unique_professions.extend(proffessoions_names)
            unique_professions = sorted(list(set(unique_professions)), reverse=False)
            if '' in unique_professions:
                unique_professions.remove('')
            elif ' ' in unique_professions:
                unique_professions.remove(' ')
            choose_profession = st.multiselect(('Выберите профессию'), unique_professions)

            # ВЫБОР КЕЙСОВ ДЛЯ ОБУЧЕНИЯ:
            if choose_profession:
                list_of_cases= sorted(list(main_table.loc[(main_table['Место обучения']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0]) & (main_table['Профессия'].str.contains(choose_profession[0]))].reset_index()['Кейсы лаборатории'].unique()), reverse=False)
                unique_cases = []
                for cases_sequence in list_of_cases:
                    cases_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', cases_sequence)
                    cases_names = cases_sequence.split('\n')
                    unique_cases.extend(cases_names)
                unique_cases = sorted(list(set(unique_cases)), reverse=False)
                if '' in unique_cases:
                    unique_cases.remove('')
                elif ' ' in unique_cases:
                    unique_cases.remove(' ')

# ДЕЛАЕМ ПРЕДЛОЖЕНИЕ АБИТУРИЕНТУ:                    
if choose_university != [] and choose_direction_of_study != [] and choose_profile != [] and choose_profession != [] :
    st.write('')
    st.markdown('''<h5 style='text-align: left; color: black;'>Образовательные кейсы, подходящие под выбранные параметры обучения:</h5>''', unsafe_allow_html=True)
    st.write('')

    for i in range(len(unique_cases)):
        col1, col2 = st.columns([1,1])
        col1.write(unique_cases[i])        
        qr_code_path = show_required_qr_code(unique_cases[i])
        col2.image(qr_code_path, width=100) #width=450  , use_column_width='auto'

    st.write('')
    st.markdown('''<h5 style='text-align: left; color: black;'>Вакансии, подходящие по направлению обучения:</h5>''', unsafe_allow_html=True)
    st.write('')
    st.write(f'[Ссылка на вакансию]({list_of_vacancies[0]})')
    
else:
    pass
















            # unique_ccc = []
            # aaa = sorted(list(main_table[main_table['Кейсы лаборатории'].notnull()]['Кейсы лаборатории'].unique()), reverse=False)
            # for bbb in aaa:
            #     bbb = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', bbb)
            #     ccc = bbb.split('\n')
            #     unique_ccc.extend(ccc)
            # unique_ccc = sorted(list(set(unique_ccc)), reverse=False)
            # if '' in unique_ccc:
            #     unique_ccc.remove('')
            # elif ' ' in unique_ccc:
            #     unique_ccc.remove(' ')
            # st.write(f'{unique_ccc}')

        # filtered_main_table = main_table.loc[main_table['Направление']==choose_direction_of_study[0]].reset_index()['Профессия']
        # st.write(filtered_main_table[0])
        # for row in range(len(filtered_main_table)):
        #     cell = filtered_main_table[row]
        #     proffessoions_name= cell.split('\n')
        #     unique_professions.extend(proffessoions_name)
        # unique_professions = sorted(list(set(unique_professions)), reverse=False)
        # if '' in unique_professions:
        #     unique_professions.remove('')
        # elif ' ' in unique_professions:
        #     unique_professions.remove(' ')
        # # st.write(unique_professions)
        # choose_profession = st.multiselect(('Выберите профессию'), unique_professions)
        # if choose_profession:



# df.loc[df['column_name'] != some_value]


# with st.sidebar:
#     st.markdown(''' # Содержание:''')
#     # st.markdown("<h1 style='text-align: left; color: black;'>О приложении:</h1>]#about)", unsafe_allow_html=True)

#     st.markdown("# [1. Возможности прототипа](#targets_and_goals)", unsafe_allow_html=True)
 