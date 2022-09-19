import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("water_potability_.csv")

x = df[(df['Potability']==0) & (df['Hardness']<=150)][['ph']].mean()

y = df[(df['Potability']==0) & (df['Hardness']>150)][['ph']].mean()

z = df[(df['Potability']==1) & (df['Hardness']<=150)][['ph']].mean()

o = df[(df['Potability']==1) & (df['Hardness']>150)][['ph']].mean()

for i in range (0,len(df)):
    if (pd.isnull(df['ph'][i]) == True):
        if ((df['Potability'][i]==0) & (df['Hardness'][i]<=150)):
            df['ph'][i] = x
        elif ((df['Potability'][i]==0) & (df['Hardness'][i]>150)):
            df['ph'][i] = y
        elif ((df['Potability'][i]==1) & (df['Hardness'][i]<=150)):
             df['ph'][i] = z
        else:
             df['ph'][i] = o

x = df[(df['Potability']==0)][['Sulfate']].mean()

y = df[(df['Potability']==1)][['Sulfate']].mean()

for i in range (0,len(df)):
    if (pd.isnull(df['Sulfate'][i]) == True):
        if (df['Potability'][i]==0):
            df['Sulfate'][i] = x
        else:
             df['Sulfate'][i] = y
x = df[(df['Potability']==0)][['Trihalomethanes']].mean()

y = df[(df['Potability']==1)][['Trihalomethanes']].mean()

for i in range (0,len(df)):
    if (pd.isnull(df['Trihalomethanes'][i]) == True):
        if (df['Potability'][i]==0):
            df['Trihalomethanes'][i] = x
        else:
             df['Trihalomethanes'][i] = y

cols = [0,5,8]
X = df[df.columns[cols]]
Y = df['Potability']

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=.25, random_state=83)

random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)

pickle.dump(random_forest, open('mini.pkl', 'wb'))

mini = pickle.load(open('mini.pkl', 'rb'))

