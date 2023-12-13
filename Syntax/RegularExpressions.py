r""" Regular Expression Symbol Overview:
.       - Any Character Except New Line          []      - Matches Characters in brackets
\d      - Digit (0-9)                            [^ ]    - Matches Characters NOT in brackets
\D      - Not a Digit (0-9)                      |       - Either Or
\w      - Word Character (a-z, A-Z, 0-9, _)      ( )     - Group
\W      - Not a Word Character                   Quantifiers:
\s      - Whitespace (space, tab, newline)       *       - 0 or More
\S      - Not Whitespace (space, tab, newline)   +       - 1 or More
\b      - Word Boundary                          ?       - 0 or One
\B      - Not a Word Boundary                    {3}     - Exact Number
^       - Beginning of a String                  {3,4}   - Range of Numbers (Minimum, Maximum)
$       - End of a String
"""
import re

search_string = """
    some_email15@mail.com     anoter.email@gmail.org     Jane_Doe99@college.tech.edu
    834-998-5415              123-456-7894               999-999-9999
    """
all_mails = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-xA-Z0-9-.]+")
specific_mail = re.compile(r"[a-z_.+-]+@[a-zA-Z0-9-]+\.[a-xA-Z0-9-.]+")
all_phonenumbers = re.compile(r"\d{3}.\d{3}.\d{4}")
specific_phonenumber = re.compile(r"[1-3]+.\d{3}.\d{4}")

print("Results:\n"
    f"All E-mails:          {all_mails.findall(search_string)}\n"
    f"Specific E-mail:      {specific_mail.findall(search_string)}\n"
    f"All Phonenumbers:     {all_phonenumbers.findall(search_string)}\n"
    f"Specific Phonenumber: {specific_phonenumber.findall(search_string)}")
