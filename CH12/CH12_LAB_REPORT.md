Name: [Annabel Shaw] Date: [5/3/26] Algorithm Analysis: K-Nearest Neighbors (KNN) 
            Regression for Bakery Loaf Prediction

        Algorithm Understanding
What type of problem is this algorithm solving? [prediction problem]

How does KNN regression differ from KNN classification? [Classifacation is visual regression is opnoins]

What does the "K" in KNN represent, and why did we choose k=4 for this problem? [K represents the number chosen like x. k=4 is the 4 closest acounds, 4 is a good number to compare to.]

In your own words, explain how the model produces a prediction for a new day. [it uses the k(4) nearset days based on the paramters given, then advages the number of loafs needed on those past days to deturment a hypothedacl amout of loafs needed.]

        Implementation Questions
Why do we separate the DataFrame into features (X) and target (y) before training? [so the prgram can check the data on a graph structer]

Why must the input to model.predict() be a 2D array (e.g., [[4, 1, 0]]) instead of a 1D array ([4, 1, 0])? [To have the ability to transvers the graph layout.]

What does .fit(X, y) actually do for a KNN model? (Hint: it's' different from most other ML algorithms.) [KNN stores the data to only the souroning area each time other modlles have the data saved to the memory directly — KNN is a "lazy learner" that mostly just stores the data]

Why do we use .values when extracting columns from the DataFrame? [To extract the aray data of the prevos days.]

        Extension: Choosing K
What would happen if we set k=1? What are the risks? [k=1 would only cheack the values of the single closest nabor wich would mean the prediction would only have one data point to rely on. Making the prodiction weeker overall.]

What would happen if we set k=20 (the size of the entire dataset)? What does the model become? [the moddle will use every prevous day as a data point. Giving an unacurat number and negagting all conditions set earler.]

How would you decide what value of k is best for a given dataset? [The best k value would be chosen after fine tuning the number to compare and contrast what value set works best in practes.]

        Extension: Distance and Feature Scaling
KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem? [The wether range could leave more room for error.]

Give an example of two days where the weather feature would unfairly dominate the distance calculation. [Compareing day 0 to day 5]

How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".) [Changing the wether to a 1/0 scale of yes/ no stormy.]

        Reflection Questions
What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction. [limatation of regression kNN is the size of prevous data, an un experance data point prevously would make it so the prediction may be poor(EX: a new movie that hasnt been rated by many pepole yet).]

Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead? [The predictions sould get more acurat as data gets added.]

What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions? [Some points that may help the predictions is a 1-4 quorterly slider, and seprating weekend and holloday into two counters.]

KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time? [The trad off would be faster On time, for it will onlt cheak the k nearest. nabors and not every data point.]

The autograder expects a prediction of approximately 70.5 loaves for today's' conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5? [I belive the 4 closest days historivly are 3,15,19, and 9, however my advage is 74.25 not the 70.5 it is suposed to be.]

Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts? [The algorithum may find a patern the baker might not have been notacing throughout the sales to reduse waset and wait of the bakerys orders.]

If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach? [Inclooding preped loafs in the count may help reduce wasted loafs in the future.]
