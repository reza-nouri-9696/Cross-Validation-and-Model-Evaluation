# Machine Learning Project For Unbalanced Dataset

This project implements a machine learning pipeline for a classification task. It includes data preprocessing, model training, evaluation, and visualization.
Be careful that this model is suitable for a dataset whose labels are unbalanced. So and so has been used straitfieldKFOLD for cross validation.

## Installation

Clone the repository and install requirements:

```bash
!git clone https://github.com/reza-nouri-9696/Cross-Validation-and-Model-Evaluation.git
%cd ml-project
```

Requirements:
- pandas 
- numpy
- scikit-learn
- matplotlib
- seaborn

## Usage

you should first add folds to your dataset with:

```nash
!python creat_folds.py --input "/path_your_input_dataset/train.csv" --output "/path_your_output/cat_train_folds.csv"
```
then run model with:
```bash
python run.py --input "/path_of/cat_train_folds.csv"
```
This will:

- Load the data 
- Split into train/validate folds
- Train a logistic regression model
- Calculate AUC 
- Generate evaluation plots

The input CSV file must have the following columns:

- `id` - sample id
- `target` - binary target variable 
- `features` - feature columns
- `kfold` - cross-validation folds 

## Code Overview

The main scripts are:

- `create_folds.py` - split data into folds
- `run.py` - train and evaluate model


The model training pipeline handles:

- One-hot encoding features
- Fitting a logistic regression model
- Making predictions
- Calculating AUC
- Plotting confusion matrix, normalized confusion matrix, AUC curves

## Results

The pipeline achieves an AUC of around 0.85 on the validation set. Example output plots are shown below.

Confusion matrix:

![Confusion Matrix](confusion_matrix.png)

Normalized confusion matrix:

![Normalized Confusion Matrix](normalized_confusion_matrix.png) 

AUC plot:

![AUC plot](auc_graph.png)

## Contributing

Contributions to improve the code are welcome! Please open an issue or PR.


## License

[MIT](https://choosealicense.com/licenses/mit/)

This covers the key points that should be included in a README for a machine learning project. Let me know if you would like me to elaborate or modify anything!
