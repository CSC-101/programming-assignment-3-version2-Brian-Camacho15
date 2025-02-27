import data
import build_data
#Part 1
#Create function called population_total that takes parameter list[CountyDemographics and returns the total 2014 population which is an integer.
#Input:test
#OutPut:318857056
def population_total(counties:list[data.CountyDemographics])-> int:
    population_tot=0
    for count  in counties:
        population_tot += count.population.get('2014 Population')
    return population_tot
#Part 2
#Create Function called filter_by_state that takes the list of county demographics and str and returns a list of countydemographics
#input: test, "CA"
#Output: 38802500
def filter_by_state(counties:list[data.CountyDemographics], string:str)-> list[data.CountyDemographics]:
    number_of_counties=[]

    for count in counties:
        if count.state == string:
            number_of_counties.append(count)

    return number_of_counties

#Part 3
#Create function called population_by_education that takes in parameter list of county demographics and the education key of interest.
#inpupt: test, "Bachelor\'s Degree or Higher
#Output: 87911.145
def population_by_education(counties:list[data.CountyDemographics], key:str)-> float:
    education_pop=0
    for count in counties:
        if key in count.education:
            education_percent= count.education.get(key)/100
            population_total(counties)
            education_pop += (count.population.get('2014 Population')*education_percent)

    return education_pop

#Create function called Population_by_ethnicity which takes list of county demographics and a key of ethnicity interst.
#input: test, "Highschool" highschool is not in the data set so we should get back 0
#Output: 0
def population_by_ethnicity(counties:list[data.CountyDemographics], key:str)-> float:
    ethnicity_pop=0
    for count in counties:
        if key == count.ethnicities:
            ethnicity_perc= count.ethnicities.get(key)/100
            count_pop= count.population.get('2014 Population')
            ethnicity_pop += count_pop * ethnicity_perc
    return ethnicity_pop
#Create fucntion called population_below_poverty that takes a lists of county demographics data set and returns float value
#Input: test:, "Two or more races
#Output: 48996488
def population_below_poverty(counties:list[data.CountyDemographics])-> float:
    below_poverty=0
    for count in counties:
        poverty_perc= count.income.get('Persons Below Poverty Level')/100
        count_pop= count.population.get('2014 Population')
        below_poverty += count_pop * poverty_perc
    return below_poverty

#Part4
#Create Function called percent by education that takes a list of countydemographics and a key and returns a float value
#Input: test, "Middle School" NOt in scope of education
#Output: 0
def percent_by_education(counties:list[data.CountyDemographics], key:str)-> float:
    population_totals= population_total(counties)
    percent_education= population_by_education(counties, key)/population_totals
    return percent_education *100
#Create Function called percent_by_ethnicity that takes a list of countydemographics and a key and returns a float value
def percent_by_ethnicity(counties:list[data.CountyDemographics], key:str)-> float:
    population_totals= population_total(counties)
    percent_ethnicity= population_by_ethnicity(counties, key)/population_totals
    return percent_ethnicity *100
#Create Function called percent_by_ethnicity that takes a list of countydemographics and a key and returns a float value
def percent_below_poverty_level(counties:list[data.CountyDemographics])->float:
    population_totals=population_total(counties)
    percent_below= population_below_poverty(counties)/population_totals
    return percent_below *100
#Part 5
#Create fucntion called educaiton_greater_than that takes a list of county demographics, a key, and a num value, that returns a list of county demographics that are above the num value given from the user.
#Input: test, "Bachlor\'s Degree or Higher, 10
#Output: list[data.demographics] with Bachleor Degree or higher more than 10 percent
def education_greater_than(counties:list[data.CountyDemographics], key:str, num:float)-> list[data.CountyDemographics]:
    greater_than=[]
    for count in counties:
        if count.education.get(key) > num:
            greater_than.append(count)
    return greater_than
#Create function called education that takes a list of county demographics, a key, and a num value, that returns a list of county demographics that are below the num value given from the user.
#Input: test, "Bachlor\'s Degree or Higher, 10
#Output: list[data.demographics] with Bachleor Degree or higher less than 10 percent
def education_less_than(counties:list[data.CountyDemographics], key:str, num:float)-> list[data.CountyDemographics]:
    less_than=[]
    for count in counties:
        if count.education.get(key) < num:
            less_than.append(count)
    return less_than
#Create function called ethincity_greather_than that takes a list of county demographics, a key, and a num value, that returns a list of county demographics that are above the num value given from the user.
#Input: test, "Two or More Races", 10
#Output: list[data.demographics] with "Two or More Races greater than 10 percent
def ethnicity_greater_than(counties:list[data.CountyDemographics], key:str, num:float)-> list[data.CountyDemographics]:
    greater_than=[]
    for count in counties:
        if count.ethnicities.get(key) > num:
            greater_than.append(count)
    return greater_than
#Create function called ethnicity_less_than that takes a list of county demographics, a key, and a num value, that returns a list of county demographics that are below the num value given from the user.
#Input: test, "Two or More Races", 10
#Output: list[data.demographics] with "Two or More Races less than 10 percent
def ethnicity_less_than(counties:list[data.CountyDemographics], key:str, num:float)-> list[data.CountyDemographics]:
    less_than=[]
    for count in counties:
        if count.ethnicities.get(key) < num:
            less_than.append(count)
    return less_than
#Create function called below_poverty_level_greater_than that takes a list of county demographics and a num value, that returns a list of county demographics that are above the num value given from the user.
#Input: test, "Persons Below Poverty Level", 10
#Output: list[data.demographics] with "Persons Below Poverty Level" greater than 10 percent
def below_poverty_level_greate_than(counties:list[data.CountyDemographics], num:float)-> list[data.CountyDemographics]:
    greater_than=[]
    for count in counties:
        if count.income.get("Persons Below Poverty Level") < num:
            greater_than.append(count)

    return greater_than
#Create function called below_poverty_level_less_than that takes a list of county demographics and a num value, that returns a list of county demographics that are below the num value given from the user.
#Input: test, "Persons Below Poverty Level", 10
#Output: list[data.demographics] with "Persons Below Poverty Level" less than 10 percent
def below_poverty_level_less_than(counties:list[data.CountyDemographics], num:float)-> list[data.CountyDemographics]:
    less_than=[]
    for count in counties:
        if count.income.get("Persons Below Poverty Level") > num:
            less_than.append(count)

    return less_than









