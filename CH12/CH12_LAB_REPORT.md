# Chapter 12 Algorithm Analysis: K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction
## Student Information
Name: [Annabel Shaw] 
Date: [5/3/26] 

## Algorithm Understanding
1) **What type of problem is this algorithm solving?** [prediction problem]

2) **How does KNN regression differ from KNN classification?** [Classification is visual regression is opnoins]

3) **What does the "K" in KNN represent, and why did we choose k=4 for this problem?** [K represents the number chosen like x. k=4 is the 4 closest accounts, 4 is a good number to compare to.]

4) **In your own words, explain how the model produces a prediction for a new day.** [It uses the k(4) nearest days based on the parameters given, then advantages the number of loafs needed on those past days to determine a hypothetical amount of loafs needed.]

## Implementation Questions
1) **Why do we separate the DataFrame into features (X) and target (y) before training?** [so the program can check the data on a graph structure]

2) **Why must the input to model.predict() be a 2D array (e.g., [[4, 1, 0]]) instead of a 1D array ([4, 1, 0])?** [To have the ability to transverse the graph layout.]

3) **What does .fit(X, y) actually do for a KNN model? (Hint: it's' different from most other ML algorithms.)** [KNN stores the data to only the souroning area each time other models have the data saved to the memory directly — KNN is a "lazy learner" that mostly just stores the data]

4) **Why do we use .values when extracting columns from the DataFrame?** [To extract the array data of the previous days.]

## Extension: Choosing K
1) **What would happen if we set k=1? What are the risks?** [k=1 would only check the values of the single closest nabor which would mean the prediction would only have one data point to rely on. Making the production weaker overall.]

2) **What would happen if we set k=20 (the size of the entire dataset)? What does the model become?** [The model will use every previous day as a data point. Giving an accurate number and negating all conditions set earlier.]

3) **How would you decide what value of k is best for a given dataset?** [The best k value would be chosen after fine tuning the number to compare and contrast what value set works best in practes.]

# Extension: Distance and Feature Scaling
1) **KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?** [The weather range could leave more room for error.]

2) **Give an example of two days where the weather feature would unfairly dominate the distance calculation.** [Comparing day 0 to day 5]

2) **How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)** [Changing the weather to a 1/0 scale of yes/ no stormy.]

# Reflection Questions
1) **What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.** [Limitation of regression kNN is the size of previous data, an un-experienced data point previously would make it so the prediction may be poor(EX: a new movie that hasn't been rated by many people yet).]

2) **Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?** [The predictions should get more accurate as data gets added.]

3) **What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?** [Some points that may help the predictions is a 1-4 quarterly slide, and separating weekend and holiday into two counters.]

4) **KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?** [The trade off would be faster On time, for it will only check the k nearest. Neighbors and not every data point.]

5) **The autograder expects a prediction of approximately 70.5 loaves for today's' conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?** [I believe the 4 closest days historically are 3,15,19, and 9, however my average is 74.25 not the 70.5 it is supposed to be.]

6) **Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?** [The algorithm may find a pattern the baker might not have been noticing throughout the sales to reduce waste and wait for the bakery's orders.]

7) **If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**[Inclooding prepared loafs in the count may help reduce wasted loafs in the future.]

