def main():
    """Script entry point"""
    #Init file
    file_handle = open(config.conf["FILE_NAME"], "w+")
    file_handle.write("Action,AccountNumber,VehicleRegistration,Make,"\
        +"Model,Colour,CountryOfRegistration,DartfordClass,GroupName\n")

    prog_menu = construct_menu()

    user_choice = sys.stdin.readline().strip()

    if user_choice not in string.digits or (int(user_choice) < 1 or int(user_choice) > 8):
        sys.exit()
    else:
        process_input(prog_menu[int(user_choice)], file_handle)

def construct_menu():
    """Construct menu for user"""
    print("Select command or press any other key to exit:")
    menu_num, prog_menu = 1, {}
    for plate in config.conf["PLATE_REPEAT"]:
        for command in config.conf["COMMANDS"]:
            print(str(menu_num) + ". " + plate + ", " + command)
            prog_menu.update({menu_num: [plate, command]})
            menu_num = menu_num + 1
    return prog_menu

#Functions
def process_input(menu, file_handle):
    """Process user input"""
    print("Processing...")
    plate = generate_plate(menu[0], file_handle)
    print(menu[1])
    comm = generate_command(menu[1])
    group = generate_group()
    for _ in range(1, 2500):
        line = construct_line(comm, ACCOUNT_ID, plate, group)
        print(line)
        file_handle.write(line)


def generate_plate(menu_item, file_handle):
    """Generate a random plate number with two letters and 3 numbers"""
    plate = ''.join(random.choice(string.ascii_lowercase)for _ in range(2))\
    .join(random.choice(string.digits)for _ in range(3))
    if plate in file_handle.read() and menu_item == config.conf["PLATE_REPEAT"][0]:
        plate = generate_plate(menu_item, file_handle)
    else:
        return plate

def generate_command(menu_item):
    """generate TollCRM command based on user input"""
    for cmnd in COMMAND:
        if cmnd.value in menu_item:
            return str(cmnd)
        else:
            return COMMAND[random.randrange(1, 3)]

def generate_group():
    """Generate a random group name"""
    groups = ["Drinks", "Drunks", "Druggies"]
    group = groups[random.randrange(0, 2)]
    return group

def construct_line(command, accountid, platenum, groupname):
    """generate entry for writing to file"""    
    line = command + config.conf["DELIMITER"]\
    + accountid + config.conf["DELIMITER"]\
    + platenum + config.conf["DELIMITER"]\
    + config.conf["DELIMITER"]\
    + config.conf["DELIMITER"]\
    + config.conf["DELIMITER"]\
    + config.conf["DELIMITER"]\
    + config.conf["DELIMITER"]\
    + config.conf["DELIMITER"]\
    + "\n"
    if groupname is not None:
        line = command + groupname
    return line

main()
