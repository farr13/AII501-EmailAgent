from Rules import allow_list, restrict_list, bad_word_list
import email
from email import policy
from email.parser import BytesParser

def reflex_Email_Sorter(Email):
    with open(Email, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
        text = msg.get_body(preferencelist=('plain')).get_content()
        print(text)

def main():
    reflex_Email_Sorter('TestEmails/Email_1.eml')

if __name__ == "__main__":
    main()