# NBA Playoffs 

Reference: [NBA Team Box Scores Page](https://www.nba.com/stats/teams/boxscores-traditional)


<h3 style="text-align: center;">Review</h3>
In a previous project certain features were used to predict winners of a matchup game.
Follow the [code](basketball.ipynb) for more details.


Below are the discoveries and challenges successfully overcome:

Multiple Exception Errors such as:

- Element Click Intercepted Exception
- Element Not Interactable Exception
- Stale Element Reference Exception
- Timeout Exception

Data Cleaning and Preprocessing: From the previous project, we needed to correct some team names since they had different establishment and ownerships. This dataset had already been fixed, but need to update the team abbreviations.

Visual graphs were displayed to get a general idea of each teams performance overall

Machine Learning: Decision Tree Regression model was used to explore and compate the accuracy comparable to Logistic Regression.
Lasso, Ridge and Elastic Net regressions will need the regression. DTR results doesn't change since the results aren't monotonic
Analysis and Figures: Part 1 Since each model will have its own factors to predict the win rate of each team, we will analyze the differences based on their actual win rate. There will be correlation between the features and should tell us whether they are helpful or a drawback to a team winning. Charts would display which model has a better prediction on win rates based on their selected features.

Conclusion
Every data scientist knows the best way to anaylze data is starting with a dataset that has been cleansed and contains essnetial features to answer pending questions. What I learned is feature importance would've saved me tons of time to see which feaatures aare really used for prediction. That way we could make this anaylsis a little more interesting by extracting data from similar source. But alas, with our machine learning models, we were able to get a a minimum of 96% in accuracy.