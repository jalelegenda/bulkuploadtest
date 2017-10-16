"""Menus for the DFFC Bulk upload CSV generator"""

STEPS =\
[
    {
        "Heading": "Select command composition of the file:",
        "Type": "SELECT",
        "Options": {
            1: "Random",
            2: "ADD",
            3: "ASSIGN",
            4: "DELETE"
        },
        "Data": [],
        "Validate": r'[1-4]{1}$'
    },

    {
        "Heading": "Select the plate repeating pattern:",
        "Type": "INSERT",
        "Options": {},
        "Data": [],
        "Validate": r'[a-zA-Z]{2,4}[0-9]{2,4}$'
    },

    {
        "Heading": "Select the number of different plates:",
        "Type": "SELECT",
        "Options": {
            1: "All random",
            2: "100 different plates",
            3: "10 different plates",
            4: "1 plate"
        },
        "Data": [],
        "Validate": r'[1-4]{1}$'
    }
]
