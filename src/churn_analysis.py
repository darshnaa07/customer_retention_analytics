import pandas as pd
def load_data():
    file_path="data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    df=pd.read_csv(file_path) 
    print("\n---CUSTOMER CHURN DATASET---")
    print(df.head())
    print("\n---DATASET SHAPE---")
    print(df.shape)
    print("\n---COLUMN NAME---")
    print(df.columns.tolist())
    return df

def check_data_quality(df):
    print("\n---MISSING VALUE---")
    print(df.isnull().sum())
    print("\n---DUPLICATED ROWS---")
    print(df.duplicated().sum())
    print(df.dtypes)

def analyze_churn(df):
    total_customer=len(df)
    churned_customer=(df["Churn"]=="Yes").sum()
    retained_customer=(df["Churn"]=="No").sum()
    churn_rate=(churned_customer/total_customer)*100
    retention_rate=(retained_customer/total_customer)*100
    print("\n---CUSTOMER CHURN ANALYSIS---")
    print(f"Total customer:{total_customer}")
    print(f"churned customer:{churned_customer}")
    print(f"Retained customer:{retained_customer}")
    print(f"churn rate:{churn_rate:2f}%")
    print(f"retention rate:{retention_rate:2f}%")
    return churn_rate,retention_rate

def analyze_contract_churn(df):
    print("\n---CHURN RATE BY CONTRACT TYPE---")
    contract_churn=df.groupby("Contract").agg(total_customer=("customerID","count"),
                                              churned_customer=("Churn",lambda x:(x=="Yes").sum()))
    contract_churn["churn_rate"]=(contract_churn["churned_customer"]/contract_churn["total_customer"]*100)
    contract_churn["churn_rate"]=contract_churn["churn_rate"].round(2)
    print(contract_churn.sort_values("churn_rate",ascending=False))
    return contract_churn

import matplotlib.pyplot as plt
import seaborn as sns

def plot_contract_churn(contract_churn):
    plt.figure(figsize=(8,4))
    sns.barplot(
        x=contract_churn.index,
        y=contract_churn["churn_rate"]
    )
    plt.title("Customer Churn Rate by Contract Type")
    plt.xlabel("Contract Type")
    plt.ylabel("Churn_rate(%)")
    plt.tight_layout()
    plt.savefig("reports/churn_by_contract.png")
    plt.show()

def analyze_tenure_churn(df):
    df=df.copy()
    df["tenure_group"]=pd.cut(
        df["tenure"],
        bins=[-1,12,48,72],
        labels=["New(0-12 Months)",
                "Medium(13-48 Months)",
                "Long-term(49-72 Months)"] )
    tenure_churn=df.groupby("tenure_group",observed=False).agg(
        total_customer=("customerID","count"),
        churned_customer=("Churn",lambda x:(x=="Yes").sum())
    )
    tenure_churn["churn_rate"]=(tenure_churn["churned_customer"]/tenure_churn["total_customer"]*100).round(2)
    print("\n---CHURN RATE BY CUSTOMER TENURE---")
    print(tenure_churn)
    return tenure_churn

def plot_tennure_churn(tenure_churn):
    plt.figure(figsize=(8,4))
    sns.barplot(
        x=tenure_churn.index.astype(str),
        y=tenure_churn["churn_rate"] )
    plt.title("Customer Churn Rate by Tenure")
    plt.xlabel("Customer Tenure")
    plt.ylabel("Churn Rate(%)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("reports/churn_by_tenure.png")
    plt.show()

def analyze_payment_churn(df):
    payment_churn=df.groupby("PaymentMethod").agg(total_customer=("customerID","count"),
                                                  churned_customer=("Churn",lambda x:(x=="Yes").sum()))
    payment_churn["churn_rate"]=(payment_churn["churned_customer"]/payment_churn["total_customer"]*100).round(2)
    payment_churn=payment_churn.sort_values("churn_rate",ascending=False)
    print("\n---CHURN RATE BY PAYMENT METHOD---")
    print(payment_churn)
    return payment_churn

def plot_payment_churn(payment_churn):
    plt.figure(figsize=(8,4))
    sns.barplot(
        x=payment_churn.index,
        y=payment_churn["churn_rate"]
     )
    plt.title("Customer churn rate by payment method")
    plt.xlabel("Payment method")
    plt.ylabel("chhurn rate(%)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("reports/churn_by_payment_method.png")
    plt.show()

def analyze_monthly_charge(df):
    df=df.copy()
    df["charge_group"]=pd.cut(df["MonthlyCharges"],
                              bins=[0,35,70,float("inf")],
                              labels=["Low charges","Medium charges","High charges"],
                              include_lowest=True)
    charge_churn=df.groupby("charge_group",observed=False).agg(
        total_customer=("customerID","count"),
        churned_customer=("Churn",lambda x:(x=="Yes").sum())
    )
    charge_churn["churn_rate"]=(charge_churn["churned_customer"]/charge_churn["total_customer"]*100).round(2)
    print("\n---CHURN RATE BY MONTHLY CHARGES---")
    print(charge_churn) 
    return charge_churn   

def plot_monthly_charge_churn(charge_churn):
    plt.figure(figsize=(8,4))
    sns.barplot(
        x=charge_churn.index.astype(str),
        y=charge_churn["churn_rate"]
                )
    plt.title("Customer churn rate by Monthly Charges")
    plt.xlabel("Monthly Charges Group")
    plt.ylabel("Churn rate(%)")
    plt.tight_layout()
    plt.savefig("reports/churn_by_monthly_charges.png")
    plt.show()

def generate_business_summary(df):
    total_customer=len(df)
    churned_customer=(df["Churn"]=="Yes").sum()
    retained_customer=(df["Churn"]=="No").sum()
    churn_rate=(churned_customer/total_customer)*100
    retention_rate=(retained_customer/total_customer)*100
    contract_churn=df.groupby("Contract")["Churn"].apply(lambda x:(x=="Yes").mean()*100)
    highest_churn_contract=contract_churn.idxmax()
    highest_churn_rate=contract_churn.max()

    summary=("CUSTOMER CHURN & RETENTION ANALYSIS\n"
    "======================================\n\n"
    f"Total customers:{total_customer}\n"
    f"Customer who left:{churned_customer}\n"
    f"Customer who stayed:{retained_customer}\n\n"
    f"Churn rate:{churn_rate:2f}%\n"
    f"Retention rate:{retention_rate:2f}%\n\n"
    "CONTRACT ANALYSIS\n"
    "---------------------\n"
    f"Highest-churn contract:{highest_churn_contract}\n"
    f"Its churn rate:{highest_churn_rate:2f}\n\n"
    "BUSINESS RECOMMENDATIONS\n"
    "---------------------------\n"
    "1.Investigate why customer leave.\n"
    "2.Offer suitable retention plans to at-risk customers.\n"
    "3.Collect customer feedback to identify service problems and their views.\n"
    "4.Monitor churn rate regularly.\n"
    )
    print("\n"+summary)
    with open("reports/bussiness_summary.txt","w",encoding="utf-8") as file:
        file.write(summary)
    print("Bussiness summary saved successfully!")