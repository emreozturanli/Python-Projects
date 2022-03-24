
# This ( https://data.police.uk/docs/ )  is the link for API documentation. You can go there and see the details.

import requests     #call requests module.

#********** FORCES **********

#which forces are there in UK relative with regions

regions_url = "https://data.police.uk/api/forces"
response1 = requests.get(regions_url)

print(response1.status_code)  # you can check the status and url to learn whether we
print(response1.url)         # get them succesfully or not.

response1.json() #now we can see what we get from API

#expected output:

# [{'id': 'avon-and-somerset', 'name': 'Avon and Somerset Constabulary'},
#  {'id': 'bedfordshire', 'name': 'Bedfordshire Police'},
#  {'id': 'cambridgeshire', 'name': 'Cambridgeshire Constabulary'},
#  {'id': 'cheshire', 'name': 'Cheshire Constabulary'},
#  {'id': 'city-of-london', 'name': 'City of London Police'},
#  {'id': 'cleveland', 'name': 'Cleveland Police'},
#  {'id': 'cumbria', 'name': 'Cumbria Constabulary'},
#  {'id': 'derbyshire', 'name': 'Derbyshire Constabulary'},
#  {'id': 'devon-and-cornwall', 'name': 'Devon & Cornwall Police'}]

# you have to see something like this. It is a little bit longer so I just write here a part from the beginnig.

#These are the forces in UK in a given region.

#********** CRIME CATEGORIES **********

# https://data.police.uk/api/crime-categories?date=2011-08

# "?" in the URL means that this data needs parameter.

#we assign our parameter to a value called "payload".

#payload is a dictionary!!!!!

crime_categories_url = "https://data.police.uk/api/crime-categories"
payload = {"date":"2020-01"}
response2 = requests.get(crime_categories_url,params=payload)

response2.json()  #crime categories in 2020-01 according to data from uk police

#expected output:

# [{'url': 'all-crime', 'name': 'All crime'},
#  {'url': 'anti-social-behaviour', 'name': 'Anti-social behaviour'},
#  {'url': 'bicycle-theft', 'name': 'Bicycle theft'},
#  {'url': 'burglary', 'name': 'Burglary'},
#  {'url': 'criminal-damage-arson', 'name': 'Criminal damage and arson'},
#  {'url': 'drugs', 'name': 'Drugs'},
#  {'url': 'other-theft', 'name': 'Other theft'},
#  {'url': 'possession-of-weapons', 'name': 'Possession of weapons'},
#  {'url': 'public-order', 'name': 'Public order'},
#  {'url': 'robbery', 'name': 'Robbery'},
#  {'url': 'shoplifting', 'name': 'Shoplifting'},
#  {'url': 'theft-from-the-person', 'name': 'Theft from the person'},
#  {'url': 'vehicle-crime', 'name': 'Vehicle crime'},
#  {'url': 'violent-crime', 'name': 'Violence and sexual offences'},
#  {'url': 'other-crime', 'name': 'Other crime'}]

#Now we have all crime types.

#********* CRIMES WITH NO LOCATION **********

# https://data.police.uk/api/crimes-no-location?category=all-crime&force=leicestershire&date=2017-03

crimes_url = "https://data.police.uk/api/crimes-no-location"
payload = {"category":"all-crime",
           "force":"city-of-london",
           "date":"2020-01"}
response3 = requests.get(crimes_url, params = payload)

response3.json()

#expected output:

# [{'category': 'anti-social-behaviour',
#   'location_type': None,
#   'location': None,
#   'context': '',
#   'outcome_status': None,
#   'persistent_id': '',
#   'id': 80721359,
#   'location_subtype': '',
#   'month': '2020-01'},
#  {'category': 'anti-social-behaviour',
#   'location_type': None,
#   'location': None,
#   'context': '',
#   'outcome_status': None,
#   'persistent_id': '',
#   'id': 80721946,
#   'location_subtype': '',
#   'month': '2020-01'}]

# again this is not the all of the output. it is a little bit longer so I cut the first part.
