import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    #df = None
    df = pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df['age'][df['sex'] == 'Male'].mean()
    average_age_men = round(average_age_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df[ df['education']=='Bachelors'])/len(df)
    percentage_bachelors = round(percentage_bachelors*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K

    higher_education=df[(df['education']== 'Bachelors')|(df['education']== 'Masters')|(df['education']== 'Doctorate')]
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']
    higher_education_rich = round((len(higher_education_rich) / len(higher_education))*100 ,1)


    lower_education=df[(df['education']!= 'Bachelors')&(df['education']!= 'Masters')&(df['education']!= 'Doctorate')]
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    lower_education_rich = round((len(lower_education_rich) / len(lower_education))*100 ,1)   

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_worktime = df['hours-per-week'] == 1
    my_frame = df[min_worktime]
    len(my_frame)
    a = len(my_frame[my_frame['salary'] == '>50K'])
    
    num_min_workers = len(my_frame[my_frame['salary'] == '>50K'])
    rich_percentage = round((a / len(my_frame) )*100,2)

    # What country has the highest percentage of people that earn >50K?
    
    highest_earning_country = None
    #filters
    salary_big = df['salary'] == '>50K'
    salary_small = df['salary'] == '<=50K'
    new = pd.DataFrame()
    new['big']  = df['native-country'][salary_big].value_counts()
    new['small'] = df['native-country'][salary_small].value_counts()
    new['total'] = new['big']  + new['small']
    new['rich'] = new['big'] / new['total']
    new.sort_values(by='rich',ascending=False).head(10)
    #new.loc[new['rich'] == new['rich'].max()].index.values
    print(new.loc[new['rich'] == new['rich'].max()].index.values[0])
    highest_earning_country = str(new.loc[new['rich'] == new['rich'].max()].index.values[0])


    highest_earning_country_percentage = round(new['rich'].max() * 100 ,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
    india = df['native-country'] == 'India'
    popular_in_india = pd.DataFrame(df[india]['occupation'].value_counts())
    df[india]['occupation'].value_counts()
    top_IN_occupation = popular_in_india[popular_in_india['occupation'] == popular_in_india['occupation'].max()].index.values[0]



    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
