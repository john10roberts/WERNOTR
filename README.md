# WE R NOT R
 Group Project Repository of Molly Sprecher, John Roberts, Miguel Montoya, and Scott Karan
 
 Communication procedure: Slack channel and zoom
 
 ## Outline 
 
We are planning to use the NBA dataset included to analyze real player stats in comparison to the NBA 2k20 video game. Basketball players in the video game are given a ranking based on over 50 different factors, according to developers of the game. 
 
Our goal is to design a machine learning model that will closely predict what ranking players will be given in the game based on the provided statistics. 

We plan to limit our analysis to the top 100 ranked players for the season, but have discussed opening this range further if needed. 

## Integrated RandomForest model 

* Preprocessing: Our dataset was strong to begin with, so the only consideration before starting the actual analysis was creating a DataFrame from our SQL database data, and splitting the data into smaller datasets based on seasons. 

* Feature selection: The 'rankings' column was our sole target variable, while all the other columns fell into the feature set. We also dropped the categorical columns of 'player', 'team', and 'season' from the feature set.

* Training and testing: After splitting the 2019-20 season from the rest of the dataset, we trained the data on all of the other seasons. We used train_test_split on scaled data from past seasons. We then applied the trained RandomForestModel to the 2019-20 dataset in order to predict the rankings. 

* RandomForestModel outcome: The model was difficult to analyze at first glance as the actual accuracy score was very low, however, all of the predicted rankings were within 5 points of the actual ranking. This required us to reevaluate how we looked at the model, as we were satisfied with the standard it performed to. Another benefit of the RandomForestModel is that it allowed us to look at how important each feature was to calculating the outcome. Although two of the lowest ranked data points were features we had previously considered dropping, actually dropping them from the model made no significant difference. 

* Database integration: We applied a connection string to our local SQL database in our Jupyter Notebook script to import the dataset for the model to work with. We also connected the transformed dataset back to our local database with the .to_sql method in order to create a new table. 


## Tools and Techniques

* Python: data preprocessing, machine learning model 
* Postgres: data storing
* HTML and Java: building visualizations and a dashboard 

## Challenges 

Personally, I foresee my biggest challenge being that there is not as much structure in this project, so in needing to find ways to make that for myself and create personal checkpoints. 

As a group, we've talked a lot about expecting our data questions and even the scope of our data to change as we go further into the project. 

We also need to figure out how to scale all of our data to improve the accuracy of our model
