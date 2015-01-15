import unittest
import email_builder
from email.mime.multipart import MIMEMultipart

class TestEmailBuilder(unittest.TestCase):
    """
    Test cases for the email_builder function
    """
    
    def setUp(self):
        self.to = "john@doe.com"
        self.message = "this is a test"
        self.file1 = "file_1.txt"
        self.file2 = "file_2.txt" 
        
    def test_email_builder(self):
        msg = email_builder.build_email(self.to, self.message, attachments=[self.file1, self.file2])
        self.assertEqual(msg['To'], self.to, "email addresses should be equal")
        for element in msg.walk():
            if element.get_content_type() == 'text/plain':
                self.assertEqual(element.get_payload(), self.message, "messages should be equal")
            else:
                content_disposition = element.get("Content-Disposition", None)
                if content_disposition:
                    dispositions = content_disposition.strip().split(";")
                    if bool(content_disposition and dispositions[0].lower() == "attachment"):
                        self.assertIn(element.get_payload(decode=True),[self.file1, self.file2], "should be one of these files")
                
    def TearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()