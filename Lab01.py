""" Task 1 """
def gather_weather_forecast(location, hours_from_now, temperatures, rain_probabilities, pressures):
    forecasts = []
    for it in range(len(hours_from_now)):
        forecast =  {"hour": hours_from_now[it], "temperature": temperatures[it], "rain probability": rain_probabilities[it], "pressure": pressures[it]}
        forecasts.append(forecast)

    weather_forecast = {"location":location, "forecast":forecasts}
    return weather_forecast

""" Task 1 checks:"""
assert gather_weather_forecast("Test Island", [1], [22], [12], [1000]) == {
    "location": "Test Island",
    "forecast": [
        {"hour": 1, "temperature": 22, "rain probability": 12, "pressure": 1000},
    ]
}

assert gather_weather_forecast("Studentski Grad", [24, 48, 72], [20, 18, 15], [0, 50, 88], [1000, 990, 980]) == {
    "location": "Studentski Grad",
    "forecast": [
        {"hour": 24, "temperature": 20, "rain probability": 0, "pressure": 1000},
        {"hour": 48, "temperature": 18, "rain probability": 50, "pressure": 990},
        {"hour": 72, "temperature": 15, "rain probability": 88, "pressure": 980},
    ]
}

""" Task 2 - my assumption is that a email must contain exactly one '@' symbol"""
def emails_shortener(emails):
    email_domains = set()
    shortened_email_set = set()
    for email in emails:
        email_domains.add(email.split("@")[1])
    for domain in email_domains:
        emails_in_domain = []
        shortened_email = ""
        for email in emails:
            if email.split("@")[1] == domain:
                emails_in_domain.append(email.split("@")[0])
        if (len(emails_in_domain) > 1):
            shortened_email = "{"
            for it in range(len(emails_in_domain) - 1):
                shortened_email = shortened_email + emails_in_domain[it] + ","
            shortened_email = shortened_email + emails_in_domain[-1] + "}@" + domain
        else:
            shortened_email = emails_in_domain[0] + "@" + domain
        shortened_email_set.add(shortened_email)
    return shortened_email_set 

""" Task 2 checks:"""
assert emails_shortener([
    "pesho@abv.bg", 
    "gosho@abv.bg",
    "sasho@abv.bg",
]) == {
    "{pesho,gosho,sasho}@abv.bg"
}

assert emails_shortener([
    "tinko@fmi.uni-sofia.bg", 
    "minko@fmi.uni-sofia.bg", 
    "pesho@pesho.org",
]) == {
    "{tinko,minko}@fmi.uni-sofia.bg", 
    "pesho@pesho.org",
}

assert emails_shortener([
    "toi_e@pesho.org",
    "golemiq@cyb.org",
]) == {
    "toi_e@pesho.org",
    "golemiq@cyb.org",
}

""" Task 3 """
INVALID_FORMAT_MSG = "Невалиден формат"
INVALID_LETTERS_MSG = "Невалидни букви"
INVALID_CODE_MSG = "Невалиден регионален код"

ALLOWED_LETTERS = set("АВЕКМНОРСТУХ")

REGION_CODES = {
    "Е": "Благоевград",
    "А": "Бургас",
    "В": "Варна",
    "ВТ": "Велико Търново",
    "ВН": "Видин",
    "ВР": "Враца",
    "ЕВ": "Габрово",
    "ТХ": "Добрич",
    "К": "Кърджали",
    "КН": "Кюстендил",
    "ОВ": "Ловеч",
    "М": "Монтана",
    "РА": "Пазарджик",
    "РК": "Перник",
    "ЕН": "Плевен",
    "РВ": "Пловдив",
    "РР": "Разград",
    "Р": "Русе",
    "СС": "Силистра",
    "СН": "Сливен",
    "СМ": "Смолян",
    "СО": "София (област)",
    "С": "София (столица)",
    "СА": "София (столица)",
    "СВ": "София (столица)",
    "СТ": "Стара Загора",
    "Т": "Търговище",
    "Х": "Хасково",
    "Н": "Шумен",
    "У": "Ямбол",
}

def is_valid(license_plate):
    if 7 <= len(license_plate) <= 8:
        region_code = license_plate[:-6]
        extra_letters = license_plate[-2:]
        numbers = license_plate[-6:-2]
        if not numbers.isdigit():
            return (False, INVALID_FORMAT_MSG)
        if not extra_letters.isalpha():
            return (False, INVALID_FORMAT_MSG)
        if not region_code.isalpha():
            return (False, INVALID_FORMAT_MSG)
        
        #FIXME row 150 fails otherwise, but did not see in instructions
        if extra_letters[0] == extra_letters[1]:
            return (False, INVALID_LETTERS_MSG)
        
        for letter in extra_letters:
            if letter not in ALLOWED_LETTERS:
                return (False, INVALID_LETTERS_MSG)
        
        if region_code not in REGION_CODES.keys():
            return (False, INVALID_CODE_MSG)
        
        return (True, REGION_CODES[region_code])
    else:
        return (False, INVALID_FORMAT_MSG)

""" Task 3 checks:"""
assert is_valid("СА1234АВ") == (True, "София (столица)")
assert is_valid("С1234АВ") == (True, "София (столица)")
assert is_valid("ТХ0000ТХ") == (True, "Добрич")
assert is_valid("ТХ000ТХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000Т") == (False, INVALID_FORMAT_MSG)
assert is_valid("ТХ0000ТХХ") == (False, INVALID_FORMAT_MSG)
assert is_valid("У8888СТ") == (True, "Ямбол")
assert is_valid("Y8888CT") == (False, INVALID_LETTERS_MSG)
assert is_valid("ПЛ7777АА") == (False, INVALID_LETTERS_MSG)
assert is_valid("РВ7777БВ") == (False, INVALID_LETTERS_MSG)
assert is_valid("ВВ6666КН") == (False, INVALID_CODE_MSG)

""" Task 4 """
TURTLE_MOVES = {"up","down","left","right"}

class Turtle:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.moves = []
        self.configuration = {}

    def get_current_position(self):
        return (self.x, self.y)
    
    def move(self, *command_lst):
        for command in command_lst:
            if command in TURTLE_MOVES:
                self.moves.append(command)
                if command == "up":
                    self.y = self.y + 1
                if command == "down":
                    self.y = self.y - 1
                if command == "right":
                    self.x = self.x + 1
                if command == "left":
                    self.x = self.x - 1
            else:
                print("Invalid command: " + command)

    def configure_turtle(self, **kwargs):
        self.configuration = kwargs
        config_log = "Current configuration:"
        for key, value in self.configuration.items():
            config_log = config_log + " " + str(key) + ":" + str(value) + " |"
        return config_log
    
    def check_for_drawing(self, moves_to_check):
        found_drawing = False
        for i in range(len(self.moves) - len(moves_to_check) + 1):
            if moves_to_check == self.moves[i:i + len(moves_to_check)]:
                found_drawing = True
        return found_drawing
            
        
    def __str__(self):
        return "Turtle is at position (" + str(self.x) + "," + str(self.y) + ") and has moved " + str(len(self.moves)) + " times since start"
    
""" Task 4 checks:"""
# Test Case 1: Test Turtle Initialization with default coordinates (0, 0)
t1 = Turtle()
assert t1.x == 0 and t1.y == 0, "Initial position should be (0,0)"
assert str(t1) == "Turtle is at position (0,0) and has moved 0 times since start", "String representation is incorrect"

# Test Case 2: Test move method with valid moves
t1.move('up', 'right', 'down', 'left')
assert t1.x == 0 and t1.y == 0, "Turtle should return to (0,0) after up, right, down, left"
assert len(t1.moves) == 4, "Turtle should have 4 moves recorded"
assert str(t1) == "Turtle is at position (0,0) and has moved 4 times since start", "String representation after 4 moves is incorrect"

# Test Case 3: Test move method with invalid move
t1.move('right', 'testing', 'right', 'left')
assert len(t1.moves) == 7, "Invalid move should not be added to the move list"
assert str(t1) == "Turtle is at position (1,0) and has moved 7 times since start", "Invalid move should not affect the position or count of moves"

# Test Case 4: Test Turtle Initialization with custom coordinates
t2 = Turtle(3, 4)
assert t2.x == 3 and t2.y == 4, "Initial position should be (3,4)"
assert str(t2) == "Turtle is at position (3,4) and has moved 0 times since start", "String representation with custom initial coordinates is incorrect"

# Test Case 5: Test move method with different valid moves
t2.move('up', 'up', 'right')
assert t2.x == 4 and t2.y == 6, "Turtle should be at (4,6) after moving up twice and right"
assert len(t2.moves) == 3, "Turtle should have 3 moves recorded"
assert str(t2) == "Turtle is at position (4,6) and has moved 3 times since start", "String representation after custom moves is incorrect"

# Test Case 6: Test configure_turtle method
config_message = t2.configure_turtle(color="green", thickness=2, size=10)
assert config_message == "Current configuration: color:green | thickness:2 | size:10 |", "Configuration message is incorrect"

# Test Case 7: Test check_for_drawing method with existing drawing
t2.move('down', 'down', 'left')
assert t2.check_for_drawing(['up', 'right', 'down']) is True, "Drawing sequence should match recorded moves"
assert t2.check_for_drawing(['up', 'up', 'right', 'left']) is False, "Invalid drawing sequence should not match recorded moves"

# Test Case 8: Test get_current_position method 
assert t2.get_current_position() == (3, 4), "Current position should be (3,4) after initial moves"


""" Task 5 """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __str__(self):
        return str(self.name) + " (" + str(self.age) + ")"
    
    def __gt__(self, other):
        return self.age > other.age
    
class FamilyTree:
    def __init__(self, root):
        self.root = root
        self.children = []

    def __str__(self, descendent = 0):
        tree = ""
        tree = tree + "    " * descendent
        tree = tree + "> " + str(self.root) + "\n"
        for child in self.children:
            tree = tree + child.__str__(descendent + 1)
        return tree 

    def count_descendants(self):
        sum_descendants = len(self.children)
        for child in self.children:
            sum_descendants = sum_descendants + child.count_descendants()
        return sum_descendants

    def add_child_tree(self, child):
        self.children.append(child)

""" Task 5 checks:"""
# tests

# Create dummies of class Person
john = Person("John", 50)
emily = Person("Emily", 30)
jake = Person("Jake", 18)
dan = Person("Dan", 3)
fiona = Person("Fiona", 7)

# Create family trees for each person
john_familiy_tree = FamilyTree(john)
emily_familiy_tree = FamilyTree(emily)
jake_familiy_tree = FamilyTree(jake)
dan_familiy_tree = FamilyTree(dan)
fiona_familiy_tree = FamilyTree(fiona)

# ---- Testing add_child_tree functionality ----

# Add children to John
john_familiy_tree.add_child_tree(jake_familiy_tree)
john_familiy_tree.add_child_tree(emily_familiy_tree)

# Add children to Emily
emily_familiy_tree.add_child_tree(dan_familiy_tree)
emily_familiy_tree.add_child_tree(fiona_familiy_tree)

assert john_familiy_tree.children[1] == emily_familiy_tree
assert john_familiy_tree.children[0] == jake_familiy_tree
assert emily_familiy_tree.children[0] == dan_familiy_tree
assert emily_familiy_tree.children[1] == fiona_familiy_tree

# ---- Testing __init__ functionality ----

assert john.name == "John"
assert john.age == 50


assert jake.name == "Jake"
assert jake.age == 18


assert john_familiy_tree.root == john
assert len(john_familiy_tree.children) == 2

assert jake_familiy_tree.root == jake
assert len(jake_familiy_tree.children) == 0

assert emily_familiy_tree.root == emily
assert dan_familiy_tree.root == dan
assert fiona_familiy_tree.root == fiona


# ---- Testing __str__functionality ----
expected_repr = "> John (50)\n    > Jake (18)\n    > Emily (30)\n        > Dan (3)\n        > Fiona (7)\n"
assert str(john_familiy_tree) == expected_repr

# # ---- Testing __gt__functionality ---- 
assert john > emily
assert john > jake
assert emily > jake
assert jake > dan

# # ---- Testing __gt__functionality ---- 
assert john_familiy_tree.count_descendants() == 4
assert jake_familiy_tree.count_descendants() == 0
assert emily_familiy_tree.count_descendants() == 2