import json
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_curve


def clean_data(df: pd.DataFrame):
    """
    Cleans the input DataFrame by removing duplicates and filling null values.

    Args:
        df (pd.DataFrame): The DataFrame to be cleaned.

    Prints:
        - Shape of the DataFrame before and after removing duplicates.
        - Information about data types and null values.
    """
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

def data_visualization(df):
    """
    Visualizes the correlation matrix of the 'metadata' column in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the 'metadata' column.
    
    Displays:
        - Correlation matrix.
    """
    if "metadata" in df.columns:
        parsed_metadata = df["metadata"].apply(lambda x: json.loads(x))
        parsed_metadata_list = parsed_metadata.tolist()
        df_metadata = pd.json_normalize(parsed_metadata_list)
        breakpoint()
        correlation_matrix = df_metadata.corr()
        print(correlation_matrix)

def big_data_analytics(df, file_path, results):
    """
    Analyzes precision, recall, and F1 scores for the given DataFrame, and appends the results.

    Args:
        df (pd.DataFrame): The DataFrame containing 'label' and 'score' columns.
        file_path (str): Path to the file being analyzed, used for identifying results.
        results (list): A list to append the results to.

    Returns:
        tuple: A tuple containing precision, recall arrays, and the updated results list.

    Prints:
        - The file name.
        - The optimal threshold, precision, recall, and F1 score.
    """
    y_true = df["label"].astype(int)
    y_pred = df["score"].astype(float)
    precision, recall, thresholds = precision_recall_curve(y_true, y_pred)
    f1_scores = 2 * (precision * recall) / (precision + recall)
    optimal_index = np.argmax(f1_scores)
    optimal_threshold = thresholds[optimal_index]

    results.append(
        {
            "file": os.path.basename(file_path),
            "optimal_threshold": optimal_threshold,
            "precision": precision[optimal_index],
            "recall": recall[optimal_index],
            "f1_score": f1_scores[optimal_index],
        }
    )

    print(f"File: {os.path.basename(file_path)}")
    print(f"Optimal Threshold: {optimal_threshold}")
    print(f"Precision: {precision[optimal_index]}")
    print(f"Recall: {recall[optimal_index]}")
    print(f"F1 Score: {f1_scores[optimal_index]}\n")
    return precision, recall, results

def precision_recall_visualization(precision, recall, file_path):
    """
    Plots the Precision-Recall curve for the given precision and recall values.

    Args:
        precision (np.ndarray): Array of precision values.
        recall (np.ndarray): Array of recall values.
        file_path (str): Path to the file being analyzed, used for the plot title.

    Displays:
        - A Precision-Recall curve.
    """
    plt.plot(recall, precision, marker=".")
    plt.title(f"Precision-Recall Curve for {os.path.basename(file_path)}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.show()

def model_comparison_histogram(comparison_df):
    """
    Creates a bar plot comparing F1 scores across different datasets.

    Args:
        comparison_df (pd.DataFrame): DataFrame containing the comparison data with 'file' and 'f1_score' columns.

    Displays:
        - A bar plot comparing F1 scores across datasets.
    """
    comparison_df.plot(x="file", y="f1_score", kind="bar", legend=False)
    plt.title("F1 Score Comparison Across Datasets")
    plt.xlabel("Dataset")
    plt.ylabel("F1 Score")
    plt.xticks(rotation=45, ha="right")
    plt.show()
