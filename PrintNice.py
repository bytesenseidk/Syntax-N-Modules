# Documentation: https://pypi.org/project/tabulate/
from tabulate import tabulate

""" Instagram Example """
def print_formater():
    data = {"Name": ["James Smith", "Maria Garcia", "Jane Doe"],
            "Age": [27, 19, 99],
            "Gender": ["Male", "Female", "Female"]}
    return tabulate(data, headers="keys", tablefmt="github")

print(print_formater())


""" ########## [ Header and Content Focus ] ########### """
def pure_example(header):
    data = [["Header 1", "Header 2", "Header 3"],
            ["Element 1", "value_1", "value_2"],
            ["Element 2", "value_1", "value_2"], 
            ["Element 3", "value_1", "value_2"], 
            ["Element 4", "value_1", "value_2"]]
    return tabulate(data, headers=header)

pure_example("firstrow")
"""
Header 1    Header 2    Header 3
----------  ----------  ----------
Element 1   value_1     value_2
Element 2   value_1     value_2
Element 3   value_1     value_2
Element 4   value_1     value_2
"""


def real_example(header):
    data = {"Name": ["Alice", "Bob", "Jane"],
            "Age": [22, 44, 66]}
    return tabulate(data, headers=header)

real_example("keys")
"""
Name      Age
------  -----
Alice      22
Bob        44
Jane       66
"""


""" ################ [ Row Indices ] ################# """
def count_example():
    data = {"First": ["Alice", "Bob", "Jane"],
            "Last": ["Abbey", "Arwood", "Astley"]}
    return tabulate(data, headers="keys", showindex="always")

count_example()
"""
    First    Last
--  -------  ------
 0  Alice    Abbey
 1  Bob      Arwood
 2  Jane     Astley
"""


""" ################ [ Table Format ] ################ """
def deco_example(deco):
    data = [["Header 1", "Header 2", "Header 3"],
            ["Element 1", "value_1", "value_2"],
            ["Element 2", "value_1", "value_2"], 
            ["Element 3", "value_1", "value_2"], 
            ["Element 4", "value_1", "value_2"]]
    return tabulate(data, headers="firstrow", tablefmt=deco)

deco_example("github")
"""
╒════════════╤════════════╤════════════╕
│ Header 1   │ Header 2   │ Header 3   │
╞════════════╪════════════╪════════════╡
│ Element 1  │ value_1    │ value_2    │
├────────────┼────────────┼────────────┤
│ Element 2  │ value_1    │ value_2    │
├────────────┼────────────┼────────────┤
│ Element 3  │ value_1    │ value_2    │
├────────────┼────────────┼────────────┤
│ Element 4  │ value_1    │ value_2    │
╘════════════╧════════════╧════════════╛
"""

formats = ["plain", "simple", "github", "grid", "fancy_grid",
            "pipe", "orgtbl", "jira", "presto", "pretty", "psql",
            "rst", "mediawiki", "moinmoin", "youtrack", "html",
            "latex", "latex_raw", "latex_booktabs", "textile"]
