
# Until now we have learned how to get datas from API Documentation.

# Now we will combine them and create a CrimeReport class so that we can easily call the datas that we want.


import requests
from collections import Counter

class CrimeReport():
    # our class will take 3 parameters region,date and category which is by default "all-crime".

    def __init__(self, region, date, category="all-crime"):
        self.region = region
        self.date = date
        self.category = category
        self.find_crimes = self.crimes()

    # in the next two methods we will just create two functions that we learned before.
    def crimes(self):
        crimes_url = "https://data.police.uk/api/crimes-no-location"
        payload = {"category":self.category,
           "force":self.region,
           "date":self.date}
        response = requests.get(crimes_url, params = payload)

        if response.status_code == 200:  #here we check our connection status
            return response.json()
        else:
            return None

    def report_crimes(self):  # We will find out how many of which crimes.
        crimes_list=[]

        if self.find_crimes is not None:  #if the crimes are not empty. so if there is a crime
            for crime in self.find_crimes:
                crimes_list.append(crime["category"])
            return Counter(crimes_list)

# Now we defined our class. Let's do some examples.

# Example 1:
# Let's learn crimes in city of london in 2020-03.

cr1 = CrimeReport("city-of-london", "2020-03")
cr1.report_crimes()

# Expected output:

# Counter({'anti-social-behaviour': 3,
#          'bicycle-theft': 1,
#          'burglary': 1,
#          'drugs': 5,
#          'other-theft': 3,
#          'shoplifting': 2,
#          'theft-from-the-person': 1,
#          'vehicle-crime': 2,
#          'violent-crime': 9,
#          'other-crime': 14})

# Example 2:
# Let's learn how many criminal-damage-arson cases are there in Norfolk in 2020-06.

cr2 = CrimeReport("norfolk", "2020-06","criminal-damage-arson")
cr2.report_crimes()

# Expected output:

# Counter({'criminal-damage-arson': 20})

# we learned that 20 criminal-damage-arson cases happened in Norfolk in 2020-06.
