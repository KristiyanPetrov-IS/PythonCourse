# Task 1

from collections import Counter
def isAnagram(s, t):
    return Counter(s) == Counter(t)

# Task 1 - Tests

assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False


# Task 2

row1 = set("qwertyuiop")
row2 = set("asdfghjkl")
row3 = set("zxcvbnm")
def findWords(words):
    def allOnSameRow(word):
        letters_in_word = set(word.lower())
        return letters_in_word.issubset(row1) or letters_in_word.issubset(row2) or letters_in_word.issubset(row3)
    return list(filter(allOnSameRow, words))

# Task 2 - Tests

words = ["Hello","Alaska","Dad","Peace"]
assert findWords(words) == ["Alaska","Dad"]
words = ["omk"]
assert findWords(words) == []
words = ["adsdf","sfd"]
assert findWords(words) == ["adsdf","sfd"]


# Task 3

def majorityElement(nums):
    count = Counter(nums)
    return count.most_common(1)[0][0]

# Task 3 - Tests

nums = [3,2,3]
assert majorityElement(nums) == 3
nums = [2,2,1,1,1,2,2]
assert majorityElement(nums) == 2


# Task 4

from collections import defaultdict
def checkStraightLine(coordinates):
    differences = defaultdict(list)
    x1, y1 = coordinates[0] 
    x2, y2 = coordinates[1]
    for (x, y) in coordinates[1:]:
        key = ((y - y1) * (x2 - x1)) - ((x - x1) * (y2 - y1))
        differences[key].append(1)
    return len(differences.keys()) == 1

# Task 4 - Tests

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
assert checkStraightLine(coordinates) == True
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
assert checkStraightLine(coordinates) == False


# Task 5

def kWeakestRows(mat, k):
    soldier_count = [(sum(row), i) for i, row in enumerate(mat)]
    soldier_count.sort()
    return list(map(lambda row: row[1], soldier_count[:k]))

# Task 5 - Tests

mat = [[1,1,0,0,0],
[1,1,1,1,0],
[1,0,0,0,0],
[1,1,0,0,0],
[1,1,1,1,1]] 
k = 3
assert kWeakestRows(mat, k) == [2,0,3]
mat = [[1,0,0,0],
[1,1,1,1],
[1,0,0,0],
[1,0,0,0]] 
k = 2
assert kWeakestRows(mat, k) == [0,2]