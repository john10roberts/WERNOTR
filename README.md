# WE_R_NOT_R
 Group Project Repository

Project Members:
John Roberts,
Miguel Montoya,
Molly Sprecher,
Scott Karan

Our plan is to train a machine model using a dataset of NBA player statistics (in the Resources folder) in the hope that our model will be able to accurately predict the individual players rankings in the league. We will then compare our models results with the rankings in the games NBA 2K in order to test our models accuracy. We are planning on just focusing on the top 100 players, but we will expand this to more players if viable. The model will most likely be a supervised model and will be using python for the code. 

For our database we are planning on using Postgres and will most likely dislay the results on a webpage using Javascript and HTML. For challenges, the most difficult for me will just be working without a roadmap as all of the challenges have provided to steps in order to accomplish the task. One concern we had in our intital discussion was if there will be enough work for the whole group, and if we wanted to expand on our intial idea, how would go about doing that. That covers our first week of the group project. All of the groups members are really nice and I look forward to working with them over the next few weeks!

# Segment 2
For the second part of the project I mainly focused on creating the html page for our dashboard. It has a simple search option to be able to look up players using any of their player data from our dataset. Once we've finished refining the machine model, the final exported data will be loaded onto the page. For now there is just the data from the 2019-20 season. For the most part our dataset was very clean, but one issue was that in order for that data to be loaded onto the page, it needed to be in javascript and around 6 of the columns in the dataset were throwing errors when converted into js. So, I went and found which columns these were and changed them in jupyter notebook. While I don't I have a machine model on my computer yet, I still went ahead and set up a postgres server and imported our data for use further down the road.

For the machine model, both Molly and John have been tackling that issue, but each in different ways. John focused on creating a neural network model where as Molly is using the randomforestclassifier. The idea here is to approach the problem in different ways and use the best points from each model. The of this model is to be able to predict rankings of players in future seasons and this question informed how the data was split into testing and training data. We are using the using the all seasons prior to the 2019-20 season as the training data and then using the 2019-20 data as the test data to see if the model is accurate. One concern we do have is that due to covid, the 2019-20 season won't be representative of a normal season due to cancellations of games, but since it wasn't used as training data it hopefully won't hurt the overall accuracy of the model. 
