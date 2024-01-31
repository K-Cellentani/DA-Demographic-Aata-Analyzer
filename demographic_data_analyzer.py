import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    mask = df['education'] == 'Bachelors'
    percentage_bachelors = round(len(df[mask]) / len(df['education']) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    df['EducationLevel'] = df['education'].apply(lambda x: 'Advanced' if x in ['Bachelors', 'Masters', 'Doctorate'] else 'Not Advanced')
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask = df['EducationLevel'] == 'Advanced'
    neg_mask = ~mask
  
    higher_education = df[mask]
    lower_education = df[neg_mask]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask = df['hours-per-week'] == min_work_hours
    min_workers = df[mask]
    num_min_workers = len(df[mask])
    num_min_rich_workers =len(min_workers[min_workers['salary'] == '>50K'])

    rich_percentage = num_min_rich_workers / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    df['rich'] = df['salary'].apply(lambda x: 1 if x == '>50K' else 0)
    country_stat = df.groupby('native-country')['rich'].mean() * 100
    highest_earning_country = country_stat.idxmax()
    highest_earning_country_percentage = round(country_stat[highest_earning_country],1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask = df['native-country'] == 'India'
    country_india = df[mask]
    mask = country_india['salary'] == '>50K'
    india_rich = country_india[mask]
    india_rich_occupation = india_rich.groupby('occupation')['salary'].count()
    top_IN_occupation = india_rich_occupation.idxmax()

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
