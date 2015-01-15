
"""
Checks if all animals are fed
"""
import mysql.connector
from database import login_info

if __name__ == "__main__":
    
    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()
    cursor2 = db.cursor()
    
    cursor.execute("SELECT id, name FROM animal")
    all_animals = cursor.fetchall()
    
    for animal in all_animals:
        animal_id = animal[0]
        animal_name = animal[1]
        cursor2.execute("SELECT feed FROM food WHERE anid=%s", (animal_id,))
        food = cursor2.fetchall()
        if (food):
            print(animal_name + " is fed at least with " + food[0][0])
        else:
            print(animal_name+" is not fed!")