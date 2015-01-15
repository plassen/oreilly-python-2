import unittest
import datetime
import time
from jotd import generate_jotd
import mysql.connector as msc
from database import login_info

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE messages (
    msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
    msgMessageID VARCHAR(128),
    msgDate DATETIME,
    msgRecipientName VARCHAR(128),
    msgRecipientAddress VARCHAR(128),
    msgText LONGTEXT
)"""

class TestJOTD(unittest.TestCase):
    """
    Test cases for the joke of the day module
    """
    
    def setUp(self):
        """
        Defines a test table 'messages' where messages with the jotd with
        the corresponding sending date are stored. 
        Also defines several recipients lists
        """
        self.recipients = {
                "test_case_1":[['pedro lopes','pedro.plassen@gmail.com']],
                "test_case_2":[['pedro lopes','pedro.plassen@gmail.com'],['tex kolorado','tex.kolorado@gmail.com']]
                }
        
        self.startdate = datetime.datetime.now()
        curs.execute("DROP TABLE IF EXISTS messages")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        
    def test_generate_1_jotd(self):
        """
        For all scenarios of recipient lists
        generate jotd for the duration of 1 day
        and validate the number of messages
        stored in the database
        """
        total_messages = 0
        duration = 1
        for tst_case in self.recipients.keys():
            total_messages += duration*len(self.recipients[tst_case])
            start = time.time()
            status = generate_jotd(recipients=self.recipients[tst_case], st=self.startdate, duration=duration)
            stop = time.time()
            interval = stop - start
            print("time to complete 1 day jtod: ", interval)
            curs.execute("SELECT count(*) FROM messages")
            row = curs.fetchone()
            messages_in_database = row[0]
            self.assertEqual(total_messages,messages_in_database,"expected messages vs messages in database should match")        
    
    def test_generate_10_jotd(self):
        """
        For all scenarios of recipient lists
        generate jotd for the duration of 10 days
        and validate the number of messages
        stored in the database
        """
        total_messages = 0
        duration = 10
        for tst_case in self.recipients.keys():
            total_messages += duration*len(self.recipients[tst_case])
            start = time.time()
            status = generate_jotd(recipients=self.recipients[tst_case], st=self.startdate, duration=duration)
            stop = time.time()
            interval = stop - start
            print("time to complete 10 day jtod: ", interval)
            curs.execute("SELECT count(*) FROM messages")
            row = curs.fetchone()
            messages_in_database = row[0]
            self.assertEqual(total_messages,messages_in_database,"expected messages vs messages in database should match")        
    
    def test_generate_50_jotd(self):
        """
        For all scenarios of recipient lists
        generate jotd for the duration of 50 days
        and validate the number of messages
        stored in the database
        """
        total_messages = 0
        duration = 50
        for tst_case in self.recipients.keys():
            total_messages += duration*len(self.recipients[tst_case])
            start = time.time()
            status = generate_jotd(recipients=self.recipients[tst_case], st=self.startdate, duration=duration)
            stop = time.time()
            interval = stop - start
            print("time to complete 50 day jtod: ", interval)
            curs.execute("SELECT count(*) FROM messages")
            row = curs.fetchone()
            messages_in_database = row[0]
            self.assertEqual(total_messages,messages_in_database,"expected messages vs messages in database should match")        
    
    def test_generate_100_jotd(self):
        """
        For all scenarios of recipient lists
        generate jotd for the duration of 100 days
        and validate the number of messages
        stored in the database
        """
        total_messages = 0
        duration = 100
        for tst_case in self.recipients.keys():
            total_messages += duration*len(self.recipients[tst_case])
            start = time.time()
            status = generate_jotd(recipients=self.recipients[tst_case], st=self.startdate, duration=duration)
            stop = time.time()
            interval = stop - start
            print("time to complete 100 day jtod: ", interval)
            curs.execute("SELECT count(*) FROM messages")
            row = curs.fetchone()
            messages_in_database = row[0]
            self.assertEqual(total_messages,messages_in_database,"expected messages vs messages in database should match")        
    
    def TearDown(self):
        curs.execute("DROP TABLE IF EXISTS messages")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        conn.close()
        
if __name__ == "__main__":
    unittest.main()