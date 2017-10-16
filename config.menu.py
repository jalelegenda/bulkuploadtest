"""This script will generate a CSV document for bulk upload feature testing"""

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
        "Heading": "Enter account numbers to use "+\
              "(leave empty to end; if no ID is entered a random ID will be used):",
        "Type": "INSERT",
        "Options": {},
        "Data": [],
        "Validate": r'1[0-9]{9}$'
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
