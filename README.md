# NBA Playoffs 

Reference: [NBA Team Stats Page](https://www.nba.com/stats/teams/traditional/)

<h3 style="text-align: center;">Basketball Introduction</h3>

In this project we will use machine learning models in order to predict the winners of each game and ultimately the tournament. We will be using data that includes the following:players stats, historical data, and team performance metrics. Our goal is to be as accurate as possible using these datasets and ultimately make the best prediction for the winner of the tournament. 

**Data collection:** 
To get an actual data (target variable: W/L) from an event that occurred, I retrieved all games played for each Season.

There were multiple Exception Errors we had to overcome such as:
-  Element Click Intercepted Exception
- Element Not Interactable Exception
- Stale Element Reference Exception
- Timeout Exception


Further into the project, I wanted to prepare the tournament much like the real deal with each team playing within their conference.
So I had to resive the Selenium code to capture Teams' designated category.


**Data Cleaning and Preprocessing:**
From the previous project, we needed to correct some team names since they had different establishment and ownerships.
This dataset had already been fixed, but need to update the team abbreviations.

Visual graphs were displayed to get a general idea of each teams performance overall

**Machine Learning: Part 1**
While this dataset contains 66172 indicies and 30 total features, a Decision Tree Regression model was used.
I chose this model because this I wanted to explore and compate the accuracy of other models than Logistic Regression. <br/>

From the result, I observed that there were absolute no error in this model's prediction. Thinking that this could be strange especially while working with a complexed dataset. <br/>

More analysis to come...

Lasso, Ridge and Elastic Net regressions will need the regression. DTR results doesn't change since the results aren't monotonic
---

**Analysis and Figures: Part 1**
Since each model will have its own factors to predict the win rate of each team, we will analyze the differences based on their actual win rate.
There will be correlation between the features and should tell us whether they are helpful or a drawback to a team winning.
Charts would display which model has a better prediction on win rates based on their selected features.

**Machine Learning: Part 2**
-- Tournament Explanation
**Analysis and Figures: Part 2**
-- Maybe show competing teams in a tree?

**Final Conclusion:**
We may tweak certain parameters and hyperparameters to develop better model presentation.
As we dive into more research, there are possible algorithms that we may come across and would be intriguing to use aside from those used within the course.
More analysis will be explored while going through this experimentation.

<h3 style="text-align: center;">Conclusion</h3>
We want to showcase the powerful tool of machine learning by leveraging data and different techniques used for prediction. Those predictions can later be used to make accurate conclusions. 





New Orleans Hornets (2002-03 ~ 2004-05)
NOH as New Orleans/Oklahoma City Hornets (2005-06 ~ 2006-07)
NOOGCH  back to NOH (2007-08 ~ 2012-13)
NOH as New Orleans Pelicans  (2013-14 ~ )

Charlotte  Hornets (1996-96 ~ 2002-03)
CH as Charleotte Bobcats (2004-05 ~ 2013-14)
CB as CH (2014-15 ~ End)



