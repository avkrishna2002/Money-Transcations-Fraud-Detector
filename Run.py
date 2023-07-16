import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


# Exercise functions
def exercise_0(file):
    # Read the dataset as a Pandas dataframe
    df = pd.read_csv("/Path of the Transcations.csv")
    return df

def exercise_1(df):
    # Return the column names as a list
    return list(df.columns)

def exercise_2(df, k):
    # Return the first k rows from the dataframe
    return df.head(k)

def exercise_3(df, k):
    # Return a random sample of k rows from the dataframe
    return df.sample(k)

def exercise_4(df):
    # Return a list of unique transaction types
    return df['type'].unique().tolist()

def exercise_5(df):
    # Return a Pandas series of the top 10 transaction destinations with frequencies
    return df['nameDest'].value_counts().head(10)

def exercise_6(df):
    # Return all the rows from the dataframe for which fraud was detected
    return df[df['isFraud'] == 1]

def exercise_7(df):
    # Return a dataframe with the number of distinct destinations that each source has interacted with, sorted in descending order
    return df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False)

# Visualization functions
def visual_1(df):
    def transaction_counts(df):
        # Count the transactions by type
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        # Count the transactions by type and fraud status
        return df.groupby(['type', 'isFraud']).size().unstack()

    fig, axs = plt.subplots(2, figsize=(6, 10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Types')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Types Split by Fraud')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'The bar charts provide insights into the distribution of transaction types and their occurrence of fraud.'

def visual_2(df):
    def query(df):
        # Filter the dataframe for Cash Out transactions and select relevant columns
        return df[df['type'] == 'CASH_OUT'][['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']]

    plot = query(df).plot.scatter(x='oldbalanceOrg', y='newbalanceDest')
    plot.set_title('Account Balance Delta for Cash Out Transactions')
    plot.set_xlabel('Origin Account Balance Delta')
    plot.set_ylabel('Destination Account Balance Delta')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'The scatter plot shows the relationship between the origin and destination account balance deltas for Cash Out transactions.'

def exercise_custom(df):
    # Perform your custom analysis/query on the dataset
    # Return the results as desired
    pass

def visual_custom(df):
    # Create a visualization based on your custom analysis/query
    # Return a string description of the chart
    pass

# Main script
if __name__ == "__main__":
    # Read the dataset
    df = exercise_0('transactions.csv')

    # Test exercises and visualizations
    print(exercise_1(df))
    print(exercise_2(df, 5))
    print(exercise_3(df, 5))
    print(exercise_4(df))
    print(exercise_5(df))
    print(exercise_6(df))
    print(exercise_7(df))

    print(visual_1(df))
    print(visual_2(df))

    # Perform and visualize custom analysis
    exercise_custom(df)
    visual_custom(df)
