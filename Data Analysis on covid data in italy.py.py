#The Liabraries required
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#To import the dataset
data = pd.read_csv(r"D:\Project\covid19_italy_region.csv")
#To get the basic statistics of the data
data.describe()
#To create a scatterplot
sns.relplot(x="TotalPositiveCases",y="Deaths",data=data)
#To create a line graph
sns.relplot(x='TotalPositiveCases',y='HomeConfinement',kind='line',data=data)