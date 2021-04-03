""" Regular Expression Symbol Overview:
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

def find_emails():
    pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-xA-Z0-9-.]+")
    return pattern.findall(search_string)

def find_specific_email():
    pattern = re.compile(r"[a-z_.+-]+@[a-zA-Z0-9-]+\.[a-xA-Z0-9-.]+")
    return pattern.findall(search_string)

def find_phonenum():
    pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
    return pattern.findall(search_string)

def find_specific_phonenum():
    pattern = re.compile(r"[1-3]+.\d{3}.\d{4}")
    return pattern.findall(search_string)

if __name__ == "__main__":
    print("\t[ Regular Expression Results ]\n",
        f"All Emails:       {find_emails()}\n",
        f"Specific Email:   {find_specific_email()}\n",
        f"All Numbers:      {find_phonenum()}\n",
        f"Specific Number:  {find_specific_phonenum()}\n")


