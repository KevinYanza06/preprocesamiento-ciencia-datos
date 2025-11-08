# preprocesamiento.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def limpiar_datos(df):
    """Elimina duplicados y valores nulos"""
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def normalizar_datos(df, columnas):
    """Normaliza columnas numéricas usando MinMaxScaler"""
    scaler = MinMaxScaler()
    df[columnas] = scaler.fit_transform(df[columnas])
    return df

def codificar_categoricas(df, columnas):
    """Codifica variables categóricas con LabelEncoder"""
    encoder = LabelEncoder()
    for col in columnas:
        df[col] = encoder.fit_transform(df[col].astype(str))
    return df

# Ejemplo de uso
if __name__ == "__main__":
    print("Funciones de preprocesamiento listas para usar.")
