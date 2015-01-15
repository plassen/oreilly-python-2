import mysql.connector as msc
from email.utils import make_msgid
from database import login_info
from settings import *

def generate_jotd(recipients, st, duration):
    """
    Generates JOTD messages that are stored in a database
    with the date when they should be sent and the recipients to whom they are
    sent.
    """
    conn = msc.Connect(**login_info)
    curs = conn.cursor()
    
    if recipients:
        RECIPIENTS = recipients
    if st:
        STARTTIME = st
    if duration:
        DAYCOUNT = duration
        
    for d in range(1,DAYCOUNT+1):
        senddate = STARTTIME + datetime.timedelta(days=d)
        for r in RECIPIENTS:
            msgID = make_msgid()
            curs.execute("""INSERT INTO messages (msgMessageID, msgDate, msgRecipientName, msgRecipientAddress, msgText)
                        VALUES (%s, %s, %s, %s, %s)""", (msgID, senddate, r[0], r[1], 'This is a test message.'))
            conn.commit()
    conn.close()
    return 1