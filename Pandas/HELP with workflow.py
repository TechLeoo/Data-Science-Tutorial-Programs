print(
                """
                \n
                DATA CLEANING STAGE
                
1) Get the dataset ---> True.
2) Initial eda ---> {self.__eda}.

    
DATA CLEANING STEPS:
    
1) Drop columns (OPTIONAL: Do this if you have irrelevant columns) ---> {self.__dropped_column}.
2) Categorical to numerical (OPTIONAL: Do this if you have categorical data in the columns) ---> {self.__data_transformation}.
3) Fix missing values (OPTIONAL: Do this if you have missing values in your columns) ---> {self.__fixed_missing}.
4) Removing outliers ---> {self.__remove_outlier}.
5) EDA ---> {self.__eda}.
6) EDA vizualizations ---> {self.__eda_visual}.
7) All columns have the right data type.

    
FURTHER DATA PREPARATION:
    
1) Select dependent and independent variables ---> {self.__dependent_independent}.
2) Scaling independent variables ---> {self.__scaled}.
3) Splitting the data into train and test dataset ---> {self.__split_data}.
    
    
BUILDING YOUR MODEL:
1) Model training ---> {self.__model_training}.
2) Model prediction ---> {self.__model_prediction}.
3) Model evaluation ---> {self.__model_evaluation}.
4) Model testing ---> {self.__model_testing}.
    
                This process highlights what a typical machine learning workflow should look like. For beginners, this should assist you getting your model ready. 
\n\n\n
                """
                )