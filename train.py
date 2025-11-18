import pandas as pd
from src.data_loading import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import engineer_features
from src.modeling import train_models
from src.evaluation import evaluate_models

def main():
    # Main training dataset – one row per loan application, includes the TARGET variable.
    df_train = load_data("data/raw/home-credit-default-risk", "application_train.csv")

    # Main test dataset – same structure as application_train but without TARGET.
    df_test = load_data("data/raw/home-credit-default-risk", "application_test.csv")

if __name__ == "__main__":
    main()
