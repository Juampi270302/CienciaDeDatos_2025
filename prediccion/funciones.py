import pandas as pd
import numpy as np

def cargar_datos_limpios():
    return pd.read_csv('../dataset/datos_limpios.csv', skipinitialspace=True)


def diccionario_tipos_atributos():
    return {
        'atributos_cantidad': np.array(['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_words',
                                        'n_non_stop_unique_tokens', 'num_hrefs', 'num_self_hrefs', 'num_imgs',
                                        'num_videos', 'average_token_length', 'num_keywords']),
        'atributos_tematica': np.array(['data_channel_is_lifestyle', 'data_channel_is_entertainment',
                                        'data_channel_is_bus', 'data_channel_is_socmed', 'data_channel_is_tech',
                                        'data_channel_is_world']),
        'atributos_min_max_avg_terceros': np.array(['kw_min_min', 'kw_max_min', 'kw_avg_min', 'kw_min_max',
                                                    'kw_max_max', 'kw_avg_max', 'kw_min_avg', 'kw_max_avg',
                                                    'kw_avg_avg', 'self_reference_min_shares',
                                                    'self_reference_max_shares', 'self_reference_avg_sharess']),
        'atributos_dia_semana': np.array(['weekday_is_monday', 'weekday_is_tuesday', 'weekday_is_wednesday',
                                          'weekday_is_thursday', 'weekday_is_friday', 'weekday_is_saturday',
                                          'weekday_is_sunday', 'is_weekend']),
        'atributos_cercania_tema': np.array(['LDA_00', 'LDA_01', 'LDA_02', 'LDA_03', 'LDA_04']),
        'atributos_polaridad_sentimiento_subjetividad': np.array(['global_subjectivity', 'global_sentiment_polarity',
                                                                  'global_rate_positive_words',
                                                                  'global_rate_negative_words',
                                                                  'rate_positive_words', 'rate_negative_words',
                                                                  'avg_negative_polarity', 'min_negative_polarity',
                                                                  'max_negative_polarity', 'avg_positive_polarity',
                                                                  'min_positive_polarity', 'max_positive_polarity',
                                                                  'title_subjectivity', 'title_sentiment_polarity',
                                                                  'abs_title_subjectivity',
                                                                  'abs_title_sentiment_polarity'])
    }


def columnas_numericas():
    return ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_words',
            'n_non_stop_unique_tokens', 'num_hrefs', 'num_self_hrefs', 'num_imgs',
            'num_videos', 'average_token_length', 'num_keywords', 'LDA_00', 'LDA_01', 'LDA_02', 'LDA_03', 'LDA_04',
            'global_subjectivity', 'global_sentiment_polarity',
            'global_rate_positive_words',
            'global_rate_negative_words',
            'rate_positive_words', 'rate_negative_words',
            'avg_negative_polarity', 'min_negative_polarity',
            'max_negative_polarity', 'avg_positive_polarity',
            'min_positive_polarity', 'max_positive_polarity',
            'title_subjectivity', 'title_sentiment_polarity',
            'abs_title_subjectivity',
            'abs_title_sentiment_polarity']


def columnas_one_hot():
    return ['data_channel_is_lifestyle', 'data_channel_is_entertainment',
            'data_channel_is_bus', 'data_channel_is_socmed', 'data_channel_is_tech',
            'data_channel_is_world', 'weekday_is_monday', 'weekday_is_tuesday', 'weekday_is_wednesday',
            'weekday_is_thursday', 'weekday_is_friday', 'weekday_is_saturday',
            'weekday_is_sunday', 'is_weekend']


def columnas_cantidad():
    return ['n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_words',
            'n_non_stop_unique_tokens', 'num_hrefs', 'num_self_hrefs', 'num_imgs',
            'num_videos', 'average_token_length', 'num_keywords']

def columnas_one_hot_dia_semana():
    return ['weekday_is_monday', 'weekday_is_tuesday', 'weekday_is_wednesday',
            'weekday_is_thursday', 'weekday_is_friday', 'weekday_is_saturday',
            'weekday_is_sunday', 'is_weekend']

def columnas_one_hot_tematica():
    return ['data_channel_is_lifestyle', 'data_channel_is_entertainment',
            'data_channel_is_bus', 'data_channel_is_socmed', 'data_channel_is_tech',
            'data_channel_is_world']

def columna_cercania_tema():
    return ['LDA_00', 'LDA_01', 'LDA_02', 'LDA_03', 'LDA_04']
