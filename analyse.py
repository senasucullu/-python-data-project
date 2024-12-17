import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')

data['Age'].fillna(data['Age'].mean(), inplace=True)

sns.countplot(x="Sex", data=data)
plt.title('Cinsiyet Dağılımı')
plt.show()


sns.countplot(x="Survived", data=data)
plt.title('Hayatta Kalma Durumu')
plt.show()

sns.histplot(data['Age'], kde=True, bins=30)
plt.title('Yaş Dağılımı')
plt.show()

sns.countplot(x="Sex", hue="Survived", data=data)
plt.title('Cinsiyete Göre Hayatta Kalma Oranı')
plt.show()

sns.boxplot(x="Pclass", y="Fare", data=data)
plt.title('Sınıfa Göre Ücret Dağılımı')
plt.show()
