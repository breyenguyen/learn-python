# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damage_convert(list_of_damages):
    updated_damages = []
    for damage in list_of_damages:
        if damage != 'Damages not recorded':
            if "M" in damage:
                damage = damage.replace('M','')
                updated_damages.append(float(damage)*1000000)
            if "B" in damage:
                damage = damage.replace('B','')
                updated_damages.append(float(damage)*1000000000)
        else:
            updated_damages.append(damage)
    return updated_damages

updated_damages = damage_convert(damages)
#print(updated_damages)

# write your construct hurricane dictionary function here:
def create_hurricane_dict(names, months, years, winds, areas_affected, damages, deaths):
    hurricane_dictionary = {}
    for i in range(len(names)):
        hurricane_dictionary.update({names[i]:{'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':winds[i], 'Areas Affected':areas_affected[i],'Damages':damages[i], 'Deaths':deaths[i]}})
    return hurricane_dictionary

hurricane_dictionary = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricane_dictionary)

# write your construct hurricane by year dictionary function here:
# here i forgot that we've created a dictionary already so I repeated the same thing over again
def create_hurricane_dict_year(names, months, years, winds, areas_affected, damages, deaths):
    hurricane_dict_by_year = {}
    for i in range(len(years)):
        if years[i] not in hurricane_dict_by_year:
            hurricane_dict_by_year[years[i]] = []
            hurricane_dict_by_year[years[i]].append({'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':winds[i], 'Areas Affected':areas_affected[i],'Damage':damages[i], 'Deaths':deaths[i]})
        elif years[i] in hurricane_dict_by_year:
            hurricane_dict_by_year[years[i]].append({'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind':winds[i], 'Areas Affected':areas_affected[i],'Damage':damages[i], 'Deaths':deaths[i]})
    return hurricane_dict_by_year

hurricane_dict_by_year = create_hurricane_dict_year(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricane_dict_by_year)

# write your count affected areas function here:
def affected_area_count(areas_affected):
    affected_area_count = {}
    for group in areas_affected:
        for area in group:
            if area not in affected_area_count:
                affected_area_count[area] = 1
            elif area in affected_area_count:
                affected_area_count[area] += 1
    return affected_area_count

affected_area_count = affected_area_count(areas_affected)
#print(affected_area_count)

# write your find most affected area function here:
def hit_hardest_area(affected_area_count):
    max_key = ''
    max_value = 0
    for key, value in affected_area_count.items():
        if value > max_value:
            max_key = key
            max_value = value
    return "{} is the area affected by the most hurricanes. It was hit {} times.".format(max_key, max_value)

print(hit_hardest_area(affected_area_count))

# write your greatest number of deaths function here:
def deadliest_hurricane(hurricane_dict):
    max_death = 0
    deadliest_hurricane = ''
    for key, value in hurricane_dict.items():
        if value.get('Deaths') > max_death:
            deadliest_hurricane = key
            max_death = value.get('Deaths')
    return "The deadliest hurricane is {}, which claimed {} lives.".format(deadliest_hurricane, max_death)

print(deadliest_hurricane(hurricane_dictionary))

# write your catgeorize by mortality function here:
def dict_by_mortality(hurricane_dict):
    hurricane_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for value in hurricane_dict.values():
        if value.get('Deaths') > 10000:
            hurricane_by_mortality[5].append(value)
        elif value.get('Deaths') > 1000:
            hurricane_by_mortality[4].append(value)
        elif value.get('Deaths') > 500:
            hurricane_by_mortality[3].append(value)
        elif value.get('Deaths') > 100:
            hurricane_by_mortality[2].append(value)
        elif value.get('Deaths') > 0:
            hurricane_by_mortality[1].append(value)
        else:
            hurricane_by_mortality[0].append(value)
    return hurricane_by_mortality

hurricane_by_mortality = dict_by_mortality(hurricane_dictionary)
#print(hurricane_by_mortality)

# write your greatest damage function here:
def costliest_hurricane(hurricane_dict):
    greatest_damage = 0
    costliest_hurricane = ''
    for key, value in hurricane_dict.items():
        if value.get('Damages') != 'Damages not recorded':
            if float(value.get('Damages')) > greatest_damage:
                costliest_hurricane = key
                greatest_damage = float(value.get('Damages'))
    return "The costliest hurricane is {}, which costed {} dollars.".format(costliest_hurricane, greatest_damage)
print(costliest_hurricane(hurricane_dictionary))

# write your catgeorize by damage function here:
def dict_by_damage(hurricane_dict):
    hurricane_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for value in hurricane_dict.values():
        if value.get('Damages') != 'Damages not recorded':
            if float(value.get('Damages')) > 50000000000:
                hurricane_by_damage[5].append(value)
            elif float(value.get('Damages')) > 10000000000:
                hurricane_by_damage[4].append(value)
            elif float(value.get('Damages')) > 1000000000:
                hurricane_by_damage[3].append(value)
            elif float(value.get('Damages')) > 100000000:
                hurricane_by_damage[2].append(value)
            elif float(value.get('Damages')) > 0:
                hurricane_by_damage[1].append(value)
            else:
                hurricane_by_damage[0].append(value)
    return hurricane_by_damage

hurricane_by_damage = dict_by_damage(hurricane_dictionary)
print(hurricane_by_damage[1])
