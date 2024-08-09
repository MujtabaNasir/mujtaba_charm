import glob
import os

import matplotlib.pyplot as plt
import pandas as pd


def read_file(directory_path):
    data_frames = []
    csv_files = glob.glob(os.path.join(directory_path, "*.csv"))

    for file_path in csv_files:
        df = pd.read_csv(file_path, encoding="unicode_escape")
        data_frames.append(df)

    return data_frames


def clean_data(df):
    print(f"shape is: {df.shape}")
    df.info()
    print(f"Information regarding the data types:\n{df.dtypes}")

    if df.duplicated().sum() > 0:
        print(f"Sum of duplicated values: {df.duplicated().sum()}")
        df.drop_duplicates(inplace=True)
        print(f"shape is: {df.shape}")
    else:
        print("There are no duplicate values")

    null_count = df.isnull().sum().sum()
    if null_count > 0:
        print(f" Null values exist as shown below:\n{df.isnull().sum()}")
        df.fillna(0, inplace=True)
        print(f" Null values cleaned:\n{df.isnull().sum()}")
    else:
        print("There are no null values")


def descriptive_statistics(df):
    print(f"Statistical data:\n{df.describe()}")


def data_visualization(df):
    df.select_dtypes(include="number").boxplot()
    plt.title("Boxplot of Numerical Columns")
    plt.xticks(rotation=70)
    plt.show()

    df.select_dtypes(include="number").hist(edgecolor="black")
    plt.title("Histograms of Numerical Columns")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
