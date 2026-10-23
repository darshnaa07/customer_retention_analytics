from src.churn_analysis import (load_data,
                                 check_data_quality,
                                   analyze_churn,
                                     analyze_contract_churn,
                                       plot_contract_churn,
                                       analyze_tenure_churn,
                                       plot_tennure_churn,
                                       analyze_payment_churn,
                                       plot_payment_churn,
                                       analyze_monthly_charge,
                                       plot_monthly_charge_churn,
                                       generate_business_summary
                                    )
df=load_data()
check_data_quality(df)
analyze_churn(df)
contract_churn=analyze_contract_churn(df)
plot_contract_churn(contract_churn)
tenure_churn=analyze_tenure_churn(df)
plot_tennure_churn(tenure_churn)
payment_churn=analyze_payment_churn(df)
plot_payment_churn(payment_churn)
charge_churn=analyze_monthly_charge(df)
plot_monthly_charge_churn(charge_churn)
generate_business_summary(df)



    
