import numpy as np
import pandas as pd

#generating random dataset using numpy


years = np.random.uniform(1 , 10 , 100).round(2)
#generating years of experience with a constant difference

salary = (30000 + years * (10000) + np.random.normal(0 , 4000 , size=100)).round(2)
#in np.random.normal , we normalise the data by passing(mean , standard deviation , data size)

df = pd.DataFrame({
    "YearsOfExperience" : years,
    "Salary": salary
})

df.to_csv("dataset.csv" , index=False)
