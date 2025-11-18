import pandas as pd
from src.data_loading import load_data

def engineer_features(df_train, df_test):
        """
        Engineer features for the specified dataframe.

        Parameters
        ----------
        df : pd.DataFrame
            The dataframe to engineer features for.

        Returns
        -------
        pd.DataFrame
            The specified dataframe with engineered features.
        """

        # Monthly status of credits recorded in bureau.csv at the external credit bureau.
        df_bureau_balance = load_data("data/raw/home-credit-default-risk", "bureau_balance.csv")

        # Historical credits of the applicant from external credit bureaus (credit history outside Home Credit).
        df_bureau = load_data("data/raw/home-credit-default-risk", "bureau.csv")

        # Monthly balance information for previous credit card accounts of the applicant.
        df_credit_card_balance = load_data("data/raw/home-credit-default-risk", "credit_card_balance.csv")

        # Payment history for previously granted installment loans (all past installment payments).
        df_installments_payments = load_data("data/raw/home-credit-default-risk", "installments_payments.csv")

        # Monthly status for previous point-of-sale or cash loans provided by Home Credit.
        df_POS_CASH_balance = load_data("data/raw/home-credit-default-risk", "POS_CASH_balance.csv")

        # All previous credit applications submitted by the applicant to Home Credit.
        df_previous_application = load_data("data/raw/home-credit-default-risk", "previous_application.csv")

        # Template submission file used in the original competition (not needed for training).
        df_sample_submission = load_data("data/raw/home-credit-default-risk", "sample_submission.csv")