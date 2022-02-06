# WERNOTR
 Group Project Repository

# Objective
We will use the data set provided from Kaggle that contains the final player stats and game rankings from the 2014 - 2020 NBA seasons to predict the overall NBA rating of the top 100 players for the 2020 season.  

# DataSet
https://www.kaggle.com/mj1196/nba-2k20-player-attributes

# Team Members
Molly S.
https://github.com/john10roberts/WERNOTR/tree/Molly

Miguel M.
https://github.com/john10roberts/WERNOTR/tree/Miguel

Scott K.
https://github.com/john10roberts/WERNOTR/tree/Scott

John R.
https://github.com/john10roberts/WERNOTR/tree/John

# Initial Database
Created a script to set up the database to allow for import into postgres:
https://github.com/john10roberts/WERNOTR/blob/John/Resources/CreateNBADB.sql

Loaded the data using postgres import function. 

# Exploratory Data Analysis
Created a simple jupyter notebook to do an initial exploratory analysis of the data set:  
https://github.com/john10roberts/WERNOTR/blob/John/NBA2kRatingsEDA.ipynb

* 2412 rows
* 32 columns
* 0 Null values

# Linear Neural Network
Created a linear neural network model using tensor flow. Split the data set into a training set of all of the data excluding the 2019-2020 season and a test dataset that was just the 2019-2020 season.  Dropped the un-needed categorical columns and used 80% of the data set with a random_state of 0 to train the model. The linear model had a Mean Absolute Error of 1.53. 
https://github.com/john10roberts/WERNOTR/blob/John/NeuralNetworkDBConnect.ipynb

# Deep Neural Network 
Created a deep neural network model using tensor flow. Split the data set into a training set of all of the data excluding the 2019-2020 season and a test dataset that was just the 2019-2020 season.  Dropped the un-needed categorical columns and used 80% of the data set with a random_state of 0 to train the model.
https://github.com/john10roberts/WERNOTR/blob/John/NeuralNetworkDBConnect.ipynb

* Two Hidden layers
    * Layer 1 - 64 Neurons, relu activation
    * Layer 2 - 64 Neurons, relu activation
* Output Layer

This model had a Mean Absolute Error of 1.81 with the vast majority of projections being within +/- 5 points of the actual rating.  

# Database Integration
Using SQLalchemy created a connection to postgres to pull in the initial data set from Postgres.  Processed the data and ran the model and then connected back to the database to save and store the predictions for the 2019-2020 season to be used with our dashboard. 



