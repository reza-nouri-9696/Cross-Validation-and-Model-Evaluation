# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kLZSgGB2TYKNFISqXz6NeIidcZwRqbrQ
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing
import argparse
import matplotlib.pyplot as plt
import seaborn as sns

def run(fold, csv_file):
    df = pd.read_csv(csv_file)
    features = [f for f in df.columns if f not in ("id", "target", "kfold")]
    for col in features:
        df.loc[:, col] = df[col].astype(str).fillna("None")
    df_train = df[df.kfold != fold].reset_index(drop=True)
    df_valid = df[df.kfold == fold].reset_index(drop=True)
    ohe = preprocessing.OneHotEncoder()
    full_data = pd.concat([df_train[features], df_valid[features]], axis=0)
    ohe.fit(full_data[features])
    x_train = ohe.transform(df_train[features])
    x_valid = ohe.transform(df_valid[features])
    model = linear_model.LogisticRegression()
    model.fit(x_train, df_train.target.values)
    valid_preds = model.predict_proba(x_valid)[:, 1]
    auc = metrics.roc_auc_score(df_valid.target.values, valid_preds)
    print(f"Fold: {fold}, AUC: {auc}")

    # Additional evaluation metrics
    y_true = df_valid.target.values
    y_pred = model.predict(x_valid)

    return auc, y_true, y_pred

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Path to the input CSV file with folds")
    args = parser.parse_args()

    auc_values = []
    all_y_true = []
    all_y_preds = []

    for fold_ in range(5):
        auc, y_true, y_preds = run(fold_, args.input)
        auc_values.append(auc)
        all_y_true.extend(y_true)
        all_y_preds.extend(y_preds)

    # Confusion matrix
    cm = metrics.confusion_matrix(all_y_true, (np.array(all_y_preds) > 0.5).astype(int))
    print(f"Confusion Matrix (Combined Folds):\n{cm}")

    # Normalize confusion matrix
    cm_normalized = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
    print(f"Normalized Confusion Matrix (Combined Folds):\n{cm_normalized}")

    # Save confusion matrix figure
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["0", "1"], yticklabels=["0", "1"])
    plt.title('Confusion Matrix (Combined Folds)')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig("/content/confusion_matrix.png")
    plt.show()

    # Save normalized confusion matrix figure
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_normalized, annot=True, cmap="Blues", xticklabels=["0", "1"], yticklabels=["0", "1"])
    plt.title('Normalized Confusion Matrix (Combined Folds)')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig("/content/normalized_confusion_matrix.png")
    plt.show()

    # Plot AUC graph
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 6), auc_values, marker='o', linestyle='-', color='b')
    plt.title('AUC Values for Each Fold')
    plt.xlabel('Fold')
    plt.ylabel('AUC')
    plt.grid(True)

    # Save the AUC graph to a file
    plt.savefig("/content/auc_graph.png")
    plt.show()