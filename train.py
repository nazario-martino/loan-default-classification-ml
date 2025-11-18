import pandas as pd
from src.data_loading import load_data
from src.preprocessing import preprocess_data
from src.modeling import train_models
from src.evaluation import evaluate_models

def main():
    df = load_data("data/raw/")
    X_train, X_test, y_train, y_test = preprocess_data(df)
    models = train_models(X_train, y_train)
    evaluate_models(models, X_test, y_test)

if __name__ == "__main__":
    main()
