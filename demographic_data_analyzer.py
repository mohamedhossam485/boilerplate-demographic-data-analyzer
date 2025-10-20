import pandas as pd

def calculate_demographic_data(print_data=True):
    # read dataset (file is provided by FCC starter)
    df = pd.read_csv("adult.data.csv")

    # 1) People count by race (Series)
    race_count = df["race"].value_counts()

    # 2) Average age of men
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # 3) % with Bachelor's degree
    percentage_bachelors = round(
        (df["education"].eq("Bachelors").mean() * 100), 1
    )

    # 4) Advanced education mask
    higher_ed = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_ed = ~higher_ed

    # % of >50K with higher education
    higher_education_rich = round(
        (df.loc[higher_ed, "salary"].eq(">50K").mean() * 100), 1
    )

    # % of >50K without higher education
    lower_education_rich = round(
        (df.loc[lower_ed, "salary"].eq(">50K").mean() * 100), 1
    )

    # 6) Min hours per week
    min_work_hours = int(df["hours-per-week"].min())

    # 7) % of >50K among people who work min hours
    min_workers = df["hours-per-week"].eq(min_work_hours)
    rich_percentage = round(
        (df.loc[min_workers, "salary"].eq(">50K").mean() * 100), 1
    )

    # 8) Country with highest % of >50K
    country_counts = df.groupby("native-country")["salary"].count()
    country_rich = df[df["salary"] == ">50K"].groupby("native-country")["salary"].count()
    pct_by_country = (country_rich / country_counts * 100).dropna()
    highest_earning_country = pct_by_country.idxmax()
    highest_earning_country_percentage = round(pct_by_country.max(), 1)

    # 9) Most popular occupation for >50K in India
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        ["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of >50K:", highest_earning_country)
        print("Highest percentage of >50K:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    # return exactly what FCC tests expect
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }

