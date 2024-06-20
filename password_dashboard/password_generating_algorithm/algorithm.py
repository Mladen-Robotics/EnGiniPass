import random
import copy
from datetime import date
from password_dashboard.password_generating_algorithm.cathegories import cathegories

# passwords_list = []

months_list = {
    "Jan.": 1,
    "Feb.": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "Aug.": 8,
    "Sept.": 9,
    "Oct.": 10,
    "Nov.": 11,
    "Dec.": 12
}

website_name = "Spagetti cat"
cathegory = "Cooking"
# cathegory_list = next((x for x in cathegories if x['title'] == cathegory), None)
# cathegory_tags= cathegory_list['tags']
cathegory_list = []
cathegory_tags = []
containing_words = ['cat' 'spagetti']
user_name = "Martin"
user_surname = "Mihalkov"
# entered_birthday = False
user_birthday = False


building_blocks = []

day = 0
month = 0
year = 0

def editDate():
    global day, month, year
    if (user_birthday == True):
        print(f"Month: {month}")
        month = [list(months_list.keys())[list(months_list.values()).index(month)].replace(".", "").lower(),list(months_list.keys())[list(months_list.values()).index(month)]]
        age = date.today().year - int(year)
        if (date.today().month < months_list[month[1]]):
            age -= 1
        elif (date.today().month == month[1] and date.today().day < day):
            age -= 1
        year = [str((year)), year[(len(year) - 2):], age]

        if day in month:
            month.remove(day)
        if age in month:
            month.remove(age)
        if day in year:
            year.remove(age)
        if age in year:
            year.remove(age)

difficulty_level = 1


def checkInput(day, month, year):
    current_containing_words = copy.deepcopy(containing_words)
    if (user_name != ""):
        building_blocks.append("user_name")
    for i in current_containing_words:
        if (i.lower() == user_name.lower()):
            current_containing_words.remove(i)
    if current_containing_words != []:
        building_blocks.append("containing_words")
    if (user_surname != ""):
        building_blocks.append("user_surname")
        for i in current_containing_words:
            if (i.lower() == user_surname.lower()):
                current_containing_words.remove(i)
    if (user_birthday == True):
        building_blocks.append("day")
        building_blocks.append("month")
        building_blocks.append("year")
    print(f"Building blocks::::::: {building_blocks}")
    if (random.choice([True, False]) == True or len(building_blocks) < 2) and cathegory != "Other":
        building_blocks.append("cathegory")


def getRandomValues(day, month, year):
    global cathegory
    global cathegory_list
    global cathegory_tags
    global cathegories
    cathegory_list = next((x for x in cathegories if x['title'] == cathegory), None)
    print(f"CCCCCCCC::::::::::::::::: {cathegory_list}")
    cathegory_tags= cathegory_list['tags']
    edited_year = ""
    edited_month = ""
    random_cathegory = ''
    if user_birthday == True:
        edited_month = random.choice(month)
        edited_year = random.choice(year)

    if "cathegory" in building_blocks:
        print(f"000:{cathegory_tags}")
        print(f"Current word:::::::::::::: {cathegory_tags}")
        random_cathegory = random.choice(cathegory_tags)

    return generatePassword(random_cathegory, edited_year, edited_month)


def generatePassword(random_cathegory, edited_year, edited_month):
    global building_blocks
    current_containing_words = copy.deepcopy(containing_words)
    password = ""
    seperators = ["!", "_"]
    while building_blocks != []:
        building_blocks = random.sample(building_blocks, len(building_blocks))
        random_block = building_blocks[0]

        if (random_block == "user_name"):
            password += modifyBlock(user_name, difficulty_level)
            password += random.choice(seperators)
        elif (random_block == "cathegory"):
            print(f"Random cathegory tag::::::::::::::::: {random_cathegory}")
            password += modifyBlock(random_cathegory, difficulty_level)
            password += random.choice(seperators)

        elif (random_block == "user_surname"):
            password += modifyBlock(user_surname, difficulty_level)
            password += random.choice(seperators)
        elif (random_block == "day"):
            password += str(day)
            password += random.choice(seperators)

        elif (random_block == "month"):
            password += str(edited_month)
            password += random.choice(seperators)
        elif (random_block == "year"):
            password += str(edited_year)
            password += random.choice(seperators)

        if (current_containing_words != []):
            random_word = random.choice(current_containing_words)
            password += modifyBlock(random_word, difficulty_level)
            password += random.choice(seperators)

            current_containing_words.remove(random_word)

        building_blocks.remove(random_block)

    return password


def modifyBlock(random_block, difficulty_level):
    options = []
    modified_block = ""

    if (difficulty_level == 1):
        for i in range(5):
            options.append("same")
        options.append("modified")
    elif (difficulty_level == 2):
        for i in range(3):
            options.append("same")
        for i in range(3):
            options.append("modified")
    elif (difficulty_level == 3):
        for i in range(5):
            options.append("modified")
        options.append("same")
    wordDuplicates = {
        'a': ["A", "/\\", "/-\\", "0\\"],
        'b': ['B', '|3'],
        'c': ['(', '<', 'C'],
        'd': ['|)', 'cl', 'D'],
        'e': ['E'],
        'f': ['ph', 'F'],
        'g': ['G'],
        'h': ['#', 'H'],
        'i': ['!', '1', '|', 'I'],
        'j': [';', 'J'],
        'k': ['|<', 'K'],
        'l': ['|_', 'L'],
        'm': ['M', '/\\/\\'],
        'n': ['n', 'N'],
        'o': ['0', 'O'],
        'p': ['p', 'P'],
        'q': ['Q'],
        'r': ['r', 'R'],
        's': ['$'],
        't': ['T'],
        'u': ['u', 'U'],
        'v': ['v', 'V'],
        'w': ['w', 'W'],
        'x': ['x', 'X'],
        'y': ['y', 'Y'],
        'z': ['Z']
    }
    for i in random_block:
        random_choise = random.choice(options)
        if (random_choise == "same"):
            modified_block += i
        else:
            if (i.lower().isnumeric() == False):
                modified_block += random.choice(wordDuplicates[i.lower()])
            else:
                modified_block += i
    return modified_block


def newPassword():
    print(f"Website name {website_name}")
    print(f"Cathegory {cathegory}")
    print(f"Containing words {containing_words}")
    print(f"User name {user_name}")
    print(f"User surname {user_surname}")
    print(f"Entered birthday {user_birthday}")
    print(f"Difficulty level {type(difficulty_level)}")
    checkInput(day, month, year)
    return getRandomValues(day, month, year)


# for i in range(3):
#     passwords_list.append(newPassword())

# print(passwords_list)
