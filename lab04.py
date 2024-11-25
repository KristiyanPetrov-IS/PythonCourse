# Task 1
from pathlib import Path
ROOT_DIR = Path.cwd()

class ListFileError(Exception):
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        super().__init__()
    
    def __str__(self) -> str:
        return f"Incorrect file path: {self.filepath}!"

class InvalidLineError(Exception):
    def __init__(self, line: str) -> None:
        self.line = line
        super().__init__()

    def __str__(self) -> str:
        return f"Invalid line: {self.line}"
    
class InvalidItemError(Exception):
    def __init__(self, item: str) -> None:
        self.item = item
        super().__init__()

    def __str__(self) -> str:
        return f"Invalid item: {self.item}"
    
class InvalidQuantityError(Exception):
    def __init__(self, quantity: int | str, item: str) -> None:
        self.quantity = quantity
        self.item = item
        super().__init__()

    def __str__(self) -> str:
        return f"Invalid quantity: {self.quantity} for item: {self.item}"

class InvalidPriceError(Exception):
    def __init__(self, price: float | str, item: str) -> None:
        self.price = price
        self.item = item
        super().__init__()

    def __str__(self) -> str:
        return f"Invalid price: {self.price} for item: {self.item}"
    
import os
def validate_list(file_path: str) -> float:
    try:
        fd = open(file_path, 'r', encoding="utf8")
        total = 0.0
        content = fd.readlines()
        fd.close()
        for line in content:
            if not line.startswith('-'):
                raise InvalidLineError(line)

            line = line[1:]
            parts = line.split(':')
            if len(parts) != 3:
                raise InvalidLineError(line)

            item_name, quantity_str, price_str = parts
            if item_name == "" or item_name.isdigit():
                raise InvalidItemError(item_name)

            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    raise InvalidQuantityError(quantity, item_name)
            except ValueError:
                raise InvalidQuantityError(quantity_str, item_name)

            try:
                price = float(price_str)
                if price <= 0:
                    raise InvalidPriceError(price, item_name)
            except ValueError:
                raise InvalidPriceError(price_str, item_name)

            total += quantity * price
        return total
    except FileNotFoundError:
        raise ListFileError(file_path)
    except IOError:
        raise ListFileError(file_path)

# Task 1 checks
assert abs(validate_list(os.path.join(ROOT_DIR, "list1.txt")) - 11.25) < 0.001

assert int(validate_list(os.path.join(ROOT_DIR, "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join(ROOT_DIR, "list3.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list4.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list5.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list6.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list7.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list8.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list9.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list10.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join(ROOT_DIR, "list11.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

print("✅ All OK! +1 point")


# Task 2
import os
class LAIKA:
    def __init__(self, directory: str, caesar_key: int) -> None:
        self.directory = directory
        self.caesar_key = caesar_key
    
    def encode(self, text: str, num_sublist_el: int) -> list[str]:
        result = [''] * len(text)
        left = 0
        right = len(text) - 1  
        for i in range(len(text)):
            if i % 2 == 0: 
                result[left] = text[i]
                left += 1
            else:  
                result[right] = text[i]
                right -= 1
        return [''.join(result[i:i + num_sublist_el]) for i in range(0, len(result), num_sublist_el)]

    def decode(self, encoded_sublists: list[str]) -> str:
        full_encoded_message = ''.join(encoded_sublists)
        result = [''] * len(full_encoded_message)
        for i in range(0, len(full_encoded_message), 2):
            result[i] = full_encoded_message[i//2]
            if i+1 < len(full_encoded_message):
                result[i+1] = full_encoded_message[len(full_encoded_message) - 1 - i // 2]
        return ''.join(result)

    def encode_to_files(self, text: str, num_sublist_el: int) -> str:
        encoded_text_sublists = self.encode(text, num_sublist_el)
        file_names = []
        for data in encoded_text_sublists:
            file_name = self.caesar_cipher(data)
            file_names.append(file_name)

            if os.path.exists(os.path.join(self.directory, file_name)):
                raise FileExistsError(f"File {file_name} already exists.")

        for i, data in enumerate(encoded_text_sublists):
            fd = open(os.path.join(self.directory, file_names[i]), 'w')
            next_file = file_names[i + 1] if i < len(encoded_text_sublists) - 1 else ''
            fd.write(next_file + '\n' + data)
            fd.close()

        return file_names[0]

    def decode_from_files(self, first_filename: str) -> str:
        sublists = []

        if not os.path.exists(os.path.join(self.directory, first_filename)):
            raise FileNotFoundError("No encoded files found.") 
        fd = open(os.path.join(self.directory, first_filename), 'r')
        content = fd.readlines()
        fd.close()
        sublists.append(content[1])
        
        while content[0].strip() != "":
            if not os.path.exists(os.path.join(self.directory, content[0].strip())):
                raise FileNotFoundError("Encoded file {content[0]} not found.") 
            fd = open(os.path.join(self.directory, content[0].strip()), 'r')
            content = fd.readlines()
            fd.close()
            sublists.append(content[1])
        
        return self.decode(sublists)

    def caesar_cipher(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                result.append(chr(start + (ord(char) - start + self.caesar_key) % 26))
            else:
                result.append(char)
        return ''.join(result)


# Task 2 checks
l = LAIKA(ROOT_DIR, 3)

# encode
assert l.encode("abcdefg", 2) == ["ac", "eg", "fd", "b"]
assert l.encode("abcdefg", 3) == ["ace", "gfd", "b"]
assert l.encode("abcdefg", 5) == ["acegf", "db"]
assert l.encode("abcdefghijkl", 1) == ["a", "c", "e", "g", "i", "k", "l", "j", "h", "f", "d", "b"]
assert l.encode("abcdefghijkl", 2) == ["ac", "eg", "ik", "lj", "hf", "db"]
assert l.encode("abcdefghijkl", 3) == ["ace", "gik", "ljh", "fdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 4) == ["aceg", "iklj", "hfdb"]
assert l.encode("abcdefghijkl", 12) == ["acegikljhfdb"]
assert l.encode("abcdefghijkl", 24) == ["acegikljhfdb"]
# decode
assert l.decode(["ac", "eg", "fd", "b"]) == "abcdefg"
assert l.decode(l.encode("abcdefg", 3)) == "abcdefg"
assert l.decode(l.encode("abcdefg", 5)) == "abcdefg"
assert l.decode(l.encode("abcdefghijkl", 1)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 2)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 3)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 4)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 12)) == "abcdefghijkl"
assert l.decode(l.encode("abcdefghijkl", 24)) == "abcdefghijkl"

# encode_to_files
root_dir = os.path.join(ROOT_DIR, "task_2")
l1 = LAIKA(root_dir, 4)
assert l1.encode_to_files("abcdefghijkl", 3) == "egi"

assert sorted(os.listdir(root_dir)) == ["egi", "jhf", "kmo", "pnl"]

with open(os.path.join(root_dir, "egi")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "kmo"
assert content == "ace"

with open(os.path.join(root_dir, "jhf")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == ""
assert content == "fdb"

with open(os.path.join(root_dir, "kmo")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "pnl"
assert content == "gik"

with open(os.path.join(root_dir, "pnl")) as fp:
    next_file = fp.readline().strip()
    content = fp.readline().strip()

assert next_file == "jhf"
assert content == "ljh"


# decode_from_files
assert l1.decode_from_files("egi") == "abcdefghijkl"

try:
    l1.encode_to_files("abcdefghijkl", 3)
except FileExistsError:
    assert True
except Exception:
    assert False

try:
    l1.decode_from_files("non-existing-file")
except FileNotFoundError:
    assert True
except Exception:
    assert False

print("✅ All OK! +2 points")