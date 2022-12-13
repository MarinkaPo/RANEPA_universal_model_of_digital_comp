import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
import os

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

### -----Устанавливаем фон:-----
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg. 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack('UMDC_images/background.png')

university_website_logo_dictionary = {'ВШКУ': ['https://gscm.ranepa.ru/', 'https://gscm.ranepa.ru/local/templates/ranhigs/images/second-logo.svg'],
                                'ВШФМ': ['http://www.shfm.ranepa.ru/', 'https://shfm.ranepa.ru/sites/all/themes/shfmRemastered/img/new/logo2.jpg'],
                                'ИБДА': ['https://ibda.ranepa.ru/', 'https://ibda.ranepa.ru/images/logo-ibda.png'],
                                'ИГСУ': ['https://igsu.ranepa.ru/', 'https://igsu.ranepa.ru/wp/wp-content/themes/Divi-child/images/logo/igsu_2017_ru.png'],
                                'ИОН': ['https://ion.ranepa.ru/', 'https://ion.ranepa.ru/local/templates/index/images/logo-iss.png'],
                                'ИОМ': ['https://iim.ranepa.ru/','https://iim.ranepa.ru/local/templates/iom_main/images/logo_iom.svg'],
                                'ИПНБ': ['https://ilns.ranepa.ru/', 'https://ilns.ranepa.ru/bitrix/templates/ranepa/etm/svg/logo-ilns.svg'],
                                'ИУРР': ['https://iurr.ranepa.ru/', 'http://iurr.ranepa.ru/wp-content/themes/iurr/asset/images/logo-iurr.png'],
                                'ИФУР': ['https://ifur.ranepa.ru/', 'https://sdpl.ru/img/IFUR.png'],
                                'ИЭМИТ': ['https://emit.ranepa.ru/', 'https://emit.ranepa.ru/wp-content/themes/emit/assets/img/site/emit-logo.svg'],
                                'ФФБ': ['ffb.ranepa.ru', 'https://learn.uniweb.ru//uploads/university/logo/122/display_______.png'],
                                'ФЭСН': ['https://fesn.ranepa.ru/', 'https://fesn.ranepa.ru/img/fesn-logo.png']}

cases_links_dictionary = {'Автоматизация модерирования объявлений с помощью нейронных сетей':'http://ccrii1.ranepa.ru:27366/',
                            'Анализ рыночной корзины и ассоциативные правила':'http://ccrii1.ranepa.ru:27382/',
                            'Базовые инструменты предварительной обработки данных':'http://ccrii1.ranepa.ru:27375/',
                            'Влияние обработки данных на точность прогноза':'http://ccrii1.ranepa.ru:27378/',
                            'Выбор рациональной маркетинговой стратегии с использованием uplift-моделирования':'http://ccrii1.ranepa.ru:27365/',
                            'Исследование надёжности заёмщиков при помощи деревьев решений':'http://ccrii1.ranepa.ru:27383/',
                            'Маркетинговые исследования с использованием A/B-тестирования':'http://ccrii1.ranepa.ru:27368/',
                            'Обнаружение поддельных новостей искусственной нейронной сетью в исторических данных':'http://ccrii1.ranepa.ru:27371/',
                            'Предсказание решений суда':'http://ccrii1.ranepa.ru:27373/',
                            'Прогноз оттока банковских клиентов':'http://ccrii1.ranepa.ru:27377/',
                            'Разведочный анализ данных':'http://ccrii1.ranepa.ru:27376/',
                            'Распознавание рукописных букв':'http://ccrii1.ranepa.ru:27384/',
                            'Распознавание рукописных цифр':'https://tialaron-laboratory5-laboratory5-w2hwy8.streamlitapp.com/',
                            'Распознавание текста на изображениях':'http://ccrii1.ranepa.ru:27372/',
                            'Сегментация изображений':'http://ccrii1.ranepa.ru:27374/',
                            'Статистический анализ показателей клиентов банка':'http://ccrii1.ranepa.ru:27367/'
                        }
# ---------------------Header---------------------
st.markdown('''<h1 style='text-align: center; color: black;'
            >Универсальная модель цифровых компетенций</h1>''', 
            unsafe_allow_html=True)
main_table = pd.read_excel(open('таблица_цифровых_компетенций.xlsx', 'rb'), sheet_name='Финальный лист') 
cases_table = pd.read_excel(open('таблица_цифровых_компетенций.xlsx', 'rb'), sheet_name='главная таблица') 

root_choise = st.radio('Я точно знаю...', ['...где хочу учиться', '...кем хочу стать'])

if root_choise == '...где хочу учиться':
    # -------------------ВЫБОР ВУЗА-------------------:
    list_of_universities = sorted(list(main_table[main_table['Институт/Факультет'].notnull()]['Институт/Факультет'].unique()), reverse=False)
    # st.write(list_of_universities)
    choose_university= st.multiselect(('Укажите место обучения:'), list_of_universities)
    if choose_university:

        # -------------------ВЫБОР НАПРАВЛЕНИЯ-------------------:
        list_of_direction_of_study = sorted(list(main_table.loc[(main_table['Институт/Факультет']==choose_university[0])].reset_index()['Направление'].unique()), reverse=False)
        # st.write(list_of_direction_of_study)
        choose_direction_of_study = st.multiselect(('Выберите направление подготовки:'), list_of_direction_of_study)
        if choose_direction_of_study:

            #-------------------ВЫБОР ПРОФИЛЯ-------------------:
            list_of_profiles= sorted(list(main_table.loc[(main_table['Институт/Факультет']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0])].reset_index()['Профиль'].unique()), reverse=False)
            # st.write(list_of_profiles)
            choose_profile = st.multiselect(('Выберите профиль:'), list_of_profiles)
            if choose_profile:

                #-------------------ПОДБОР ПРОФЕССИИ И ВЫВОД НАВЫКОВ-------------------:
                list_of_professions = sorted(list(main_table.loc[(main_table['Институт/Факультет']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Профессия'].unique()), reverse=False)

                list_of_salary = sorted(list(main_table.loc[(main_table['Институт/Факультет']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Гросс (тыс. руб.)'].unique()), reverse=False)

                list_of_scills = sorted(list(main_table.loc[(main_table['Институт/Факультет']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Навыки'].unique()), reverse=False)
                
                general_digital_scills = sorted(list(main_table.loc[(main_table['Институт/Факультет']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Цифровые навыки (общие)'].unique()), reverse=False)
                list_of_general_digital_scills = []
                for competences_sequence in general_digital_scills:
                    # иногда для колонка 'Цифровые навыки (общие)' пустая, поэтому так:
                    if str(competences_sequence) != 'nan':
                        # competences_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(competences_sequence))
                        competence_names = competences_sequence.split('\n')
                        list_of_general_digital_scills.extend(competence_names)
                    else:
                        pass
                
                prophile_digital_scills = sorted(list(main_table.loc[(main_table['Институт/Факультет']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Цифровые навыки (профильные)'].unique()), reverse=False)
                list_of_prophile_digital_scills = []
                for competences_sequence in prophile_digital_scills:
                    # иногда для госслужбы колонка 'Цифровые навыки (профильные)' пустая, поэтому так:
                    if str(competences_sequence) != 'nan':
                        # competences_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(competences_sequence))
                        competence_names = competences_sequence.split('\n')
                        list_of_prophile_digital_scills.extend(competence_names)
                    else:
                        pass    

                # подбор кейсов для обучения по направлению из основной вкладки:
                list_of_cases= sorted(list(cases_table.loc[(cases_table['Профиль']==choose_profile[0])].reset_index()['Кейсы лаборатории'].unique()), reverse=False)
                unique_cases = []
                for cases_sequence in list_of_cases:
                    cases_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(cases_sequence))
                    cases_names = cases_sequence.split('\n')
                    unique_cases.extend(cases_names)
                unique_cases = sorted(list(set(unique_cases)), reverse=False)
                if '' in unique_cases:
                    unique_cases.remove('')
                elif ' ' in unique_cases:
                    unique_cases.remove(' ')

                # подбор лого и сайта ВУЗа:
                university_website_link  = university_website_logo_dictionary[choose_university[0]][0]
                university_logo_image_link = university_website_logo_dictionary[choose_university[0]][1]
                
                # ВЫВОДИМ РЕЗУЛЬТАТ:
                st.markdown(f''' \n##### Учебное заведение: [<img src={university_logo_image_link} width="60">]({university_website_link})
                        ''', unsafe_allow_html=True)

                st.write(f'''\n##### Ваша возможная будущая профессия: 
                            \n{list_of_professions[0]}
                            \n##### Зарплата подобных специалстов до вычета налогов: 
                            \n{list_of_salary[0]} тысяч рублей
                            \n##### Навыки для этой должности: 
                            \n{list_of_scills[0]}
                            \n##### Цифровые навыки и инструменты, которые вы освоите:''')
                if list_of_general_digital_scills != [] and list_of_prophile_digital_scills != [] :
                    col1, col2 = st.columns([1,1])
                    col1.write(f'''\n###### Общие: ''')
                    for skill in list_of_general_digital_scills:
                        col1.write(skill)
                    col2.write(f'''\n###### Профильные: ''')
                    for skill in list_of_prophile_digital_scills:
                        col2.write(skill)
                else:                    
                    for skill in list_of_general_digital_scills:
                        st.write(skill)
                    for skill in list_of_prophile_digital_scills:
                        st.write(skill)

                st.write(f'''\n##### Подходящие обучающие кейсы по вашему профилю подготовки:''')
                for i in range(len(unique_cases)):
                        st.write(f'''**{i+1}).** [{unique_cases[i]}]({cases_links_dictionary[unique_cases[i]]})''')

                st.markdown(f''' \n##### Посмотреть дополнительные учебные кейсы по ссылке: [<img src='https://lia.ranepa.ru/images/tild3366-3736-4637-a339-366136616230__studysvg3.svg' width="70">](https://lia.ranepa.ru/)
                        ''', unsafe_allow_html=True)           


elif root_choise == '...кем хочу стать':
    # -------------------ВЫБОР ПРОФЕССИИ-------------------:
    list_of_professions = sorted(list(main_table[main_table['Профессия'].notnull()]['Профессия'].unique()), reverse=False)
    choose_profession= st.multiselect(('Укажите желаемую профессию:'), list_of_professions)
    if choose_profession:
        #-------------------ВЫБОР ПРОФИЛЯ-------------------:
            list_of_profiles= sorted(list(main_table.loc[(main_table['Профессия']==choose_profession[0])].reset_index()['Профиль'].unique()), reverse=False)
            # st.write(list_of_profiles)
            choose_profile = st.multiselect(('Выберите профиль:'), list_of_profiles)
            if choose_profile:
            #-------------------ПОДБОР НАПРАВЛЕНИЯ, МЕСТА ОБУЧЕНИЯ И ВЫВОД НАВЫКОВ-------------------:
                list_of_direction_of_study = sorted(list(main_table.loc[(main_table['Профессия']==choose_profession[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Направление'].unique()), reverse=False)

                list_of_universities = sorted(list(main_table.loc[(main_table['Профессия']==choose_profession[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Институт/Факультет'].unique()), reverse=False)

                list_of_salary = sorted(list(main_table.loc[(main_table['Профессия']==choose_profession[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Гросс (тыс. руб.)'].unique()), reverse=False)

                list_of_scills = sorted(list(main_table.loc[(main_table['Профессия']==choose_profession[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Навыки'].unique()), reverse=False)
                
                general_digital_scills = sorted(list(main_table.loc[(main_table['Профессия']==choose_profession[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Цифровые навыки (общие)'].unique()), reverse=False)
                list_of_general_digital_scills = []
                for competences_sequence in general_digital_scills:
                    # иногда для колонка 'Цифровые навыки (общие)' пустая, поэтому так:
                    if str(competences_sequence) != 'nan':
                        # competences_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(competences_sequence))
                        competence_names = competences_sequence.split('\n')
                        list_of_general_digital_scills.extend(competence_names)
                    else:
                        pass
                
                prophile_digital_scills = sorted(list(main_table.loc[(main_table['Профессия']==choose_profession[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Цифровые навыки (профильные)'].unique()), reverse=False)
                list_of_prophile_digital_scills = []
                for competences_sequence in prophile_digital_scills:
                    # иногда для госслужбы колонка 'Цифровые навыки (профильные)' пустая, поэтому так:
                    if str(competences_sequence) != 'nan':
                        # competences_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(competences_sequence))
                        competence_names = competences_sequence.split('\n')
                        list_of_prophile_digital_scills.extend(competence_names)
                    else:
                        pass
                
                # подбор кейсов для обучения по направлению из основной вкладки:
                list_of_cases= sorted(list(cases_table.loc[(cases_table['Профиль']==choose_profile[0])].reset_index()['Кейсы лаборатории'].unique()), reverse=False)
                unique_cases = []
                for cases_sequence in list_of_cases:
                    cases_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(cases_sequence))
                    cases_names = cases_sequence.split('\n')
                    unique_cases.extend(cases_names)
                unique_cases = sorted(list(set(unique_cases)), reverse=False)
                if '' in unique_cases:
                    unique_cases.remove('')
                elif ' ' in unique_cases:
                    unique_cases.remove(' ')

                
                university_website_link  = university_website_logo_dictionary[list_of_universities[0]][0]
                university_logo_image_link = university_website_logo_dictionary[list_of_universities[0]][1]

                # ВЫВОДИМ РЕЗУЛЬТАТ:  # height="40"
                st.markdown(f''' \n##### Учебное заведение: [<img src={university_logo_image_link} width="90" >]({university_website_link})
                        ''', unsafe_allow_html=True)

                st.write(f'''\n##### Ваша желаемая будущая профессия: 
                            \n{choose_profession[0]}
                            \n##### Зарплата подобных специалстов до вычета налогов: 
                            \n{list_of_salary[0]} тысяч рублей
                            \n##### Навыки для этой должности: 
                            \n{list_of_scills[0]}
                            \n##### Цифровые навыки и инструменты, которые вы освоите:''')
                if list_of_general_digital_scills != [] and list_of_prophile_digital_scills != [] :
                    col1, col2 = st.columns([1,1])
                    col1.write(f'''\n###### Общие: ''')
                    for skill in list_of_general_digital_scills:
                        col1.write(skill)
                    col2.write(f'''\n###### Профильные: ''')
                    for skill in list_of_prophile_digital_scills:
                        col2.write(skill)
                else:                    
                    for skill in list_of_general_digital_scills:
                        st.write(skill)
                    for skill in list_of_prophile_digital_scills:
                        st.write(skill)
                
                st.write(f'''\n##### Подходящие обучающие кейсы по вашему профилю подготовки:''')
                for i in range(len(unique_cases)):
                        st.write(f'''**{i+1}).** [{unique_cases[i]}]({cases_links_dictionary[unique_cases[i]]})''')

                st.markdown(f''' \n##### Посмотреть дополнительные учебные кейсы по ссылке: [<img src='https://lia.ranepa.ru/images/tild3366-3736-4637-a339-366136616230__studysvg3.svg' width="70">](https://lia.ranepa.ru/)
                        ''', unsafe_allow_html=True)     



        
















# # -------------------ВЫБОР НАПРАВЛЕНИЯ-------------------:
# list_of_direction_of_study = sorted(list(main_table[main_table['Направление'].notnull()]['Направление'].unique()), reverse=False)
# # добавялем 'Безопасность сферы государственных услуг' в конец списка:
# if 'Безопасность сферы государственных услуг' in list_of_direction_of_study:
#     list_of_direction_of_study.remove('Безопасность сферы государственных услуг')
#     list_of_direction_of_study.append('Безопасность сферы государственных услуг')
# choose_direction_of_study = st.multiselect(('Выберите направление подготовки:'), list_of_direction_of_study)
# if choose_direction_of_study:

#     skills_table = pd.read_excel(open('вспомогательная_таб_для_циф_компетенций.xlsx', 'rb'), sheet_name='навыки таблица') 

#     # подбор цифровых компетенций по направлению из 2ой вкладки 'навыки таблица':    
#     list_of_digit_competences = list(skills_table.loc[(skills_table['Направление']==choose_direction_of_study[0])].reset_index().iloc[0,1:-5])
#     list_of_digit_competences = [vacancy for vacancy in list_of_digit_competences if 'str' in str(type(vacancy))]
#     list_of_digit_competences = list(set(list_of_digit_competences))
#     # st.write(list_of_digit_competences)
#     unique_digit_competences = []
#     for competences_sequence in list_of_digit_competences:
#         competences_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(competences_sequence))
#         competence_names = competences_sequence.split('\n')
#         unique_digit_competences.extend(competence_names)

#     # подбор вакансий по направлению из 2ой вкладки 'навыки таблица':
#     # list_of_vacancies = sorted(list(skills_table.loc[(skills_table['Направление']==choose_direction_of_study[0])].reset_index()['ссылки'].unique()), reverse=False) # ДОБАВИТЬ И ОСТАЛЬНЫЕ ЧЕРЕЗ columns_with_vacancies!!!!  
#     list_of_vacancies = list(skills_table.loc[(skills_table['Направление']==choose_direction_of_study[0])].reset_index().iloc[0,-4:])
#     list_of_vacancies = [vacancy for vacancy in list_of_vacancies if 'str' in str(type(vacancy))]
#     list_of_vacancies = list(set(list_of_vacancies))
#     # st.write(list_of_vacancies)
    
#     # подбор кейсов для обучения по направлению из основной вкладки:
#     list_of_cases= sorted(list(main_table.loc[(main_table['Направление']==choose_direction_of_study[0])].reset_index()['Кейсы лаборатории'].unique()), reverse=False)
#     unique_cases = []
#     for cases_sequence in list_of_cases:
#         cases_sequence = re.sub('\d\d\) |\d\d\)|\d\) |\d\)', '', str(cases_sequence))
#         cases_names = cases_sequence.split('\n')
#         unique_cases.extend(cases_names)
#     unique_cases = sorted(list(set(unique_cases)), reverse=False)
#     if '' in unique_cases:
#         unique_cases.remove('')
#     elif ' ' in unique_cases:
#         unique_cases.remove(' ')

#     # выпадающее окно с предложением (выбрано направление подготовки):
#     with st.expander(label='Посмотреть подходящие предложения:'):
#         # выводим найденные вакансии:
#         st.write('')
#         st.markdown('''<h5 style='text-align: left; color: black;'>Вакансии, подходящие по направлению обучения:</h5>''', unsafe_allow_html=True)
#         st.write('')
#         for i in range(len(list_of_vacancies)):
#             st.write(f'[Ссылка на вакансию {i+1}]({list_of_vacancies[i]})')
#         st.write('')
#         # выводим найденные кейсы:
#         st.markdown('''<h5 style='text-align: left; color: black;'>Образовательные кейсы, подходящие по направлению обучения:</h5>''', unsafe_allow_html=True)
#         for i in range(len(unique_cases)):
#             col1, col2 = st.columns([4,1])
#             col1.write(unique_cases[i])        
#             qr_code_path = show_required_qr_code(unique_cases[i])
#             col2.image(qr_code_path, width=100) #width=450  , use_column_width='auto'


#     #-------------------ВЫБОР ПРОФИЛЯ-------------------:
#     list_of_profiles= sorted(list(main_table.loc[(main_table['Направление']==choose_direction_of_study[0])].reset_index()['Профиль'].unique()), reverse=False)
#     # list_of_profiles= sorted(list(main_table.loc[(main_table['Место обучения']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0])].reset_index()['Профиль'].unique()), reverse=False)
#     # st.write(list_of_profiles)
#     choose_profile = st.multiselect(('Выберите профиль:'), list_of_profiles)
#     if choose_profile:

#         #-------------------ВЫБОР ПРОФЕССИИ-------------------:
#         list_of_professions= sorted(list(main_table.loc[(main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Профессия'].unique()), reverse=False)
#         # list_of_professions = sorted(list(main_table.loc[(main_table['Место обучения']==choose_university[0]) & (main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0])].reset_index()['Профессия'].unique()), reverse=False)
#         unique_professions = []
#         for professions_sequence in list_of_professions:
#             proffessoions_names= professions_sequence.split('\n')
#             unique_professions.extend(proffessoions_names)
#         unique_professions = sorted(list(set(unique_professions)), reverse=False)
#         if '' in unique_professions:
#             unique_professions.remove('')
#         elif ' ' in unique_professions:
#             unique_professions.remove(' ')
#         choose_profession = st.multiselect(('Выберите профессию:'), unique_professions)

#         if choose_profession:
#             # ВЫБОР УНИВЕРСИТЕТА/ВУЗА/...:
#             list_of_universities = sorted(list(main_table.loc[(main_table['Направление']==choose_direction_of_study[0]) & (main_table['Профиль']==choose_profile[0]) & (main_table['Профессия'].str.contains(choose_profession[0]))].reset_index()['Место обучения'].unique()), reverse=False)
#             # list_of_universities = sorted(list(main_table[main_table['Место обучения'].notnull()]['Место обучения'].unique()), reverse=False)
#             # choose_university = st.multiselect(('Выберите место обучения:'), list_of_universities)
            
#             st.markdown('''<h5 style='text-align: left; color: black;'>Образовательные подразделения РАНХиГС, подходящие вам:</h5>''', unsafe_allow_html=True)
#             for university_name in list_of_universities:
#                 st.write(university_name)

#             st.markdown('''<h5 style='text-align: left; color: black;'>Навыки и инструменты, которые вы освоите: </h5>''', unsafe_allow_html=True)
#             # выводим найденные цифровые компетенции:
#             st.image('digital_competences.jpg',  use_column_width='auto') 
#             # col1, col2 = st.columns([1,1])
#             for i in range(len(unique_digit_competences)):
#                 st.write(f'{i+1}. {unique_digit_competences[i]}')
#             st.write('')

 