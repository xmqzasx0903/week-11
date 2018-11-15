import CSV
import numpy as np
import matplotlib.pyplot as plt

# figure out what data we want to use
categories = [] # these are the colum headers in the CSV file
installs = [] # this is the installs row
ratings= [] # this is the ratings row

with open('data/googeplaystore.csv') as csvfile:
	reader = csv.reader(csv.file)
	line_count = 0

	# move the page column headers out of the actual data to get a clean dataset
	for row in reader:
		if line_count is 0: # this will be text, not data
			print('pushing categoriesinto a separate array')
			categories.append(row) # push the text into this array
			line_count += 1 # increment the line count for the next loop
		else:
			# garb the rating and push them into the rating array
			ratingsData = row[2]
			ratingsData = ratingsData.replace("NaN", "0")
			ratings.append(float(ratingsData)) # int will turn a string (place of text) into a munber
			# print('pushing ratings data into the ratings array')
			installsData = row[5]
			installsData = installsData.replace(",", "") # get rid of the commas
			
			# get rid of the trailing "+"
			installs.append(np.char.strip(installsData, "+"))
			line_count += 1

# get some values we can work with
# how many rating are 4=?
# how many are below 2?
# how many are in the middle?
np_ratings = np.array(ratings) # turn a plain Python list into a Numpy array
popular_apps = np_ratings > 4
print("popular_apps:", len(popular_apps))

percent_popular = int(len(np_ratings[popular_apps]) / len(np_ratings) * 100)
print(percent_popular)

unpopular_apps = np_ratings < 4
print("popular_apps:", len(unpopular_apps))

percent_unpopular = int(len(np_ratings[unpopular_apps]) / len(np_ratings) * 100)
print(percent_unpopular)

kinda_popular = int(100 - (percent_popular + percent_unpopular))
print(kinda_popular)

# do a visualization with our shiny new data
labels = "Sucks", "Weh", "Love it"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ['yekkowgreen', 'lightgreen', 'lightblue']
explode = (0.1, 0.1, 0.15)

ply.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('euqal')
plt.legend(labels, loc=1)
ply.title("Do we love us some apps?")
plt.xlabel("Use Rating - App Installs (10,000+ apps")
plt.show()
