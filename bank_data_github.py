import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
customers = pd.read_csv("customers.csv")
transactions = pd.read_csv("transactions.csv")
products = pd.read_csv("products.csv")
print(customers.head())
print(transactions.head())
print(products.head())
# Gender üzrə paylanma
print(customers['gender'].value_counts())

# Churn paylanması
print(customers['churn'].value_counts(normalize=True))
#Şəhər üzrə paylanması
print(customers['city'].value_counts(normalize=True))
# Əməliyyat növləri üzrə paylanma
print(transactions['type'].value_counts())
# Məbləğ üzrə statistikalar
print(transactions['amount'].describe())

customer_transactions = pd.merge(
    customers,
    transactions,
    on="customer_id",
    how="left" 
)

# 2️⃣ Müştəri + məhsulları birləşdir
customer_products = pd.merge(
    customers,
    products,
    on="customer_id",
    how="left"
)


# Nəticəyə bax
print(customer_products.head())

# Datanı birləşdirdilib ayrıca csv faylı
customer_products.to_csv("full_bank_data.csv", index=False)



# Churn paylanması qrafiki
sns.countplot(data=customers, x='churn')
plt.title("Churn Paylanması")
plt.show()
# Gender vs Churn qrafiki
sns.countplot(data=customers, x='gender', hue='churn')
plt.title("Gender vs Churn")
plt.show()

# Yaş paylanması qrafiki
sns.histplot(customers['age'], bins=20, kde=True)
plt.title("Müştərilərin Yaş Paylanması")
plt.show()

# Əməliyyat növləri qrafiki
sns.countplot(data=transactions, x='type')
plt.title("Əməliyyat Növləri Paylanması")
plt.xticks(rotation=45)
plt.show()
