#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import sklearn as skl


# In[150]:


import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import session
from configparser import ConfigParser


# In[93]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[ ]:





# In[129]:


parser = ConfigParser()
_ = parser.read("config")
password = parser.get('my_db', 'password')


# In[130]:


string = f"postgresql://postgres:{password}@localhost/group-project"
engine = create_engine(string)


# In[151]:


#%%sql 
#SELECT * FROM real


# In[152]:


raw_df = pd.read_sql('SELECT * FROM real', engine)
raw_df.head(5)


# In[153]:


train_seasons = raw_df[(raw_df.season != '2019-20')]
train_seasons
test_season = raw_df[(raw_df.season == '2019-20')]

                       


# In[154]:


X = train_seasons.copy()
X = X.drop("rankings", axis=1)
X = X.drop("player", axis=1)
X = X.drop("team", axis=1)
X = X.drop("season", axis=1)


# In[135]:


y = train_seasons["rankings"].ravel()
y[:5]


# In[136]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)


# In[137]:


scaler = StandardScaler()
X_scaler = scaler.fit(X_train)

X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[138]:


rf_model = RandomForestClassifier(n_estimators=128, random_state=2)


# In[139]:


rf_model = rf_model.fit(X_train_scaled, y_train)


# In[140]:


predictions = rf_model.predict(X_test_scaled)


# In[155]:


test_df = test_season.copy()
test_df = test_df.drop("player", axis=1)
test_df = test_df.drop("team", axis=1)
test_df = test_df.drop("season", axis=1)
test_df.head()
test_x = test_df.drop("rankings", axis=1)
test_y = test_df['rankings'].ravel()


# In[142]:


testx_scaler = scaler.fit(test_x)

X_test_scaled = testx_scaler.transform(test_x)


# In[156]:


current_predictions = rf_model.predict(X_test_scaled)


# In[157]:


comparison_df = pd.DataFrame(current_predictions, columns=["predictions"])
comparison_df['real'] = test_y
comparison_df.head(20)

new_df = raw_df.merge(comparison_df, left_index=True, right_index=True)
new_df = new_df.drop('real', axis=1)
new_df.head(5)


# In[149]:


new_df.to_csv('/Users/mollysprecher/Desktop/Classwork/group/data.csv', index=False)


# In[148]:


new_df.to_sql(name='projections_2020', con=engine, if_exists='replace', method='multi')


# In[ ]:




