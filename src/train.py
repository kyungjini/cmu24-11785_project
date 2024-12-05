from preprocess import label_preprocess

def main():
    csv_path = "/Users/james/Documents/dataset/MIMIC-CXR/labels/mimic-cxr-2.0.0-chexpert.csv"
    df = label_preprocess(csv_path)
