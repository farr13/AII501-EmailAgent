from Rules import allow_list, restrict_list, bad_word_list
import email
from email import policy
from email.parser import BytesParser

def check_allow_list(sender: str):
    for domain in allow_list:
        if domain in sender:
            return True
    return False

def check_restrict_list(sender: str):
    for domain in restrict_list:
        if domain in sender:
            return True
    return False

def reflex_Email_Sorter(Email: str):
    with open(Email, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
        text = msg.get_body(preferencelist=('plain')).get_content()
    if check_allow_list(msg['From']):
        return "notspam"
    elif check_restrict_list(msg['From']):
        return "spam"
    else:
        count = 0
        for word in bad_word_list:
            if word in text:
                count += 1
            if count >= 5:
                return "spam"
    return "notspam"

def performAction(Action: str):
    if Action == "spam":
        print("Sending to Spam Directory")
    elif Action == "notspam":
        print("Sending to Email Directory")
    else:
        print("Error")

def main():
    list_of_emails = ['TestEmails/Email_1.eml', 
                      'TestEmails/Email_2.eml', 
                      'TestEmails/Email_3.eml', 
                      'TestEmails/Email_4.eml', 
                      'TestEmails/Email_5.eml', 
                      'TestEmails/Email_6.eml', 
                      'TestEmails/Email_7.eml', 
                      'TestEmails/Email_8.eml']
    for email in list_of_emails:
        Action = reflex_Email_Sorter(email)
        performAction(Action)

if __name__ == "__main__":
    main()