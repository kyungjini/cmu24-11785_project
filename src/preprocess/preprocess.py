import pandas as pd


def label_preprocess(csv_path):
    df = pd.read_csv(csv_path)
    df.drop(columns=["subject_id"], inplace=True)
    df.replace(-1, 0, inplace=True)
    df.fillna(0, inplace=True)
    return df


"/Users/james/Documents/dataset/MIMIC-CXR/labels/mimic-cxr-2.0.0-chexpert.csv"
