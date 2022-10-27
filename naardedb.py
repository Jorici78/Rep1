import mariadb # package laden. Kan zijn dat het dat niet doet omdat ie die package nog niet heeft. Zie cmd prompt voor dat geval.

print("hoi")
print("we gaan verder")

mydb = mariadb.connect(
  host="localhost",  #port erbij indien mac
  user="root",
  password="",
  database="Jorisdb"
) # Database laden (verwijzen naar PHP (admin via SQL))

antwoord = input("Welk type sport wil je doen?")
mycursor = mydb.cursor() # geen hele interessante command, maar moet je wel even uitvoeren. maakt het zoeken mogelijk door de database waarmee je hierboven de link hebt gelegd. Oftewel de zoeker toewijzen aan de gelinkte database. Maakt zoeken mogelijk
# mycursor.execute("SELECT * FROM sport") # * staat voor "alles", als in we willen alles van onze record set 'sport' ophalen. Met deze bestand creeer je de record set, haal je de data op.
# mycursor.execute("SELECT * FROM sport WHERE type='balsport'")
mycursor.execute("SELECT * FROM sport WHERE type='"+antwoord+"'")

myresult = mycursor.fetchall() # Met deze command vraag je de record set op.

print(myresult)

for i in range(10):
	print("hoi")

for i in myresult:
	print("doei")

for i in myresult:
	print(i[2])
	if i[2] == "tennis":
		print("wel even water meenemen")

for x in range(5):
	print(x)

mycursor.execute("SELECT type, intensiteit FROM sport")
myresult = mycursor.fetchall()
print(myresult)