import csv, itertools

users = {}
minSupportCount = 500

with open('data/anonymous-msweb.data') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	lastUserId = None
	for row in reader:
		if row[0] == 'C':
			lastUserId = row[1]

		if row[0] == 'V':
			if lastUserId not in users:
				users[lastUserId] = []
		
			users[lastUserId].append(row[1])

l = {}

for userId in users.keys():
	pages = users[userId]
	
	for page in pages:
		if page not in l:
			l[page] = 0
		
		l[page] += 1

for page in l.keys():
	counter = l[page]
	if counter < minSupportCount:
		l.pop(page)



l2 = {}
for a in itertools.combinations(l.keys(), 2):
	for userId in users.keys():
		pages = users[userId]

		if set(a).issubset(set(pages)):
			if a not in l2:
				l2[a] = 0

			l2[a] += 1

for page in l2.keys():
	counter = l2[page]
	if counter < minSupportCount:
		l2.pop(page)

l3 = {}
for a in itertools.combinations(l2.keys(), 3):
	for userId in users.keys():
		pages = users[userId]

		if set(a).issubset(set(pages)):
			if a not in l3:
				l3[a] = 0

			l3[a] += 1

for page in l3.keys():
	counter = l3[page]
	if counter < minSupportCount:
		l3.pop(page)

print len(users)
print len(l2)
print len(l3)
