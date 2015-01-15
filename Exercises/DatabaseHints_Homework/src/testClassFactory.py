
import unittest
import mysql.connector as msc
from database import login_info
from classFactory import build_row

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name VARCHAR(128),
    email VARCHAR(128)
)"""

class DBTest(unittest.TestCase):
    
    def setUp(self):
        curs.execute("DROP TABLE IF EXISTS user")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        curs.execute("INSERT INTO user (id, name, email) VALUES (1, 'John Doe', 'john@doe.com')")
        conn.commit()
        curs.execute("INSERT INTO user (id, name, email) VALUES (2, 'Jane Doe', 'jane@doe.com')")
        conn.commit()
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
        
    def test_repr(self):
        self.assertEqual(repr(self.c),
                         "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")
        
    def test_retrieve_without_condition(self):
        """should return a list of DataRow objects?"""
        pass
       
    def test_retrieve_with_condition(self):
        first_row = self.c.retrieve(curs, "id = 1")
        self.assertEqual(first_row.id, 1, "Should return a row with a id equal to 1")
        
    def tearDown(self):
        curs.execute("DROP TABLE IF EXISTS user")
        
if __name__ == "__main__":
    unittest.main()