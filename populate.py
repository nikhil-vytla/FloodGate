import sqlite3, random
from math import *
from datetime import datetime

# DATABASE
conn = sqlite3.connect('data.db', check_same_thread=False)
db = conn.cursor()

db.execute('CREATE TABLE points (phone, type, severity, location, datetime)')
# db.execute('DROP TABLE points')

# center:{lat:34.1871,lng:-77.8824}

points = []
types = ['water', 'trash', 'algae', 'electricity']
sev = ['LOW', 'MID', 'HIGH']

for i in range(100):
	'''points.append({
		'phone': '+12014823830',
		'type': types[random.random(0, 3).round()],
		'severity': sev[random.random(0, 2).round()]
		'location': str(random.random(34.601797, 33.94196)) + ',' str(random.random(77.972885, 78.60183))
		
		})'''
		# 'location': str(random.random(34.10, 34.23)) + ',' str(random.random(77.2, 79.2))

	db.execute('INSERT INTO points VALUES (?, ?, ?, ?, ?)', ('+12014823830', types[random.randrange(0, 1, 1)], sev[random.randrange(0, 2, 1)], str(random.uniform(34.602, 33.942)) + ',' + str(random.uniform(-77.973, -78.602)), datetime.now()))

conn.commit()