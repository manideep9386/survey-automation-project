import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the survey data
df = pd.read_csv('responses.csv')

# Display summary statistics
print("🔍 Summary of Feedback:")
print(df['rating'].describe())
print("\n📋 All Comments:")
print(df[['email', 'comments']])

# Plot the distribution of ratings
plt.figure(figsize=(8, 5))
sns.countplot(x='rating', data=df)
plt.title('Customer Feedback Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Responses')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
