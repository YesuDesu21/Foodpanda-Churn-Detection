<h1>Foodpanda Churn Prediction</h1>

Made by YesuDesu

====================

<h2>Overview</h2>
This project was initially planned to be a food recommendation web application. But after figuring out what the
nature of the dataset is, I realized that it is not suitable for recommendation but instead predictions like binary classification.

<h2>Explanatory Data Analysis</h2>

![alt text](/results/image-3.png)

![alt text](/results/image-4.png)

![alt text](/results/image-5.png)

<h2>Feature Engineering</h2>
For feature engineering and selection, I decided to create a new feature by taking the time duration (days) of last order date and order date.
I also tried to multiply order frequency and quantity.

![alt text](/results/image-6.png)

<h2>Algorithms used</h2>
The algorithms I used for training the model and evaluation are: 
- Random Forest Tree Classifier for the classification and churn prediction
- For feature validation to see if the feature is suitable for the model, I used two methods which is the Feature Importance (Gini Impurity) and Permutation Importance. I learned that feature importance is more biased with continous data than permutation importance, therefore it is more accurate to look at the permutation importance.
- I also used classification report to see the accuracy of the model.
- I used the confusion matrix to see how many true positives and negatives are there with each training iteration.

<h2>Results</h1>

Results using Classification Report:
1. Features: 'rating','delivery_status','churned'
![alt text](/results/image.png)

2. 'rating','delivery_status','churned','payment_method'
![alt text](/results/image-1.png)

3.![alt text](/results/image-2.png)

<h2>Problem</h2>

After how many iterations of feature selection and validation, I found out that the data is most likely synthetic and the model cannot learn from the dataset. 

<b>Redflags:</b>
1. A comment from a contributor mentioned that the dataset is equally distributed (as seen from my EDA).
2. After how many iterations of feature selection and hyperparameter tuning, the accuracy level ranges from 49% to 55% which means that
the model did not learn and is simply guessing.
3. Even with the evaluation metrics used as a basis for feature selection, each training result does not have much difference. And sometimes most features reach negative importance.
4. Some columns such as order_date and last_order_date is logically wrong. Upon observation, there are a lot of dates in last_order_date where the year is much more present than order_date, assuming that the format is supposed to be order_date is past, and last_order_date is much more present. With this, some dates are the other way around and I had to swap the data from each column (assuming that it was a mis-input).

Lessons learnt from this project is to research whether or not the dataset is reliable before performing deep analysis.