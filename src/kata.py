import math
from collections import deque


def simple_assembler(program: str) -> dict:
    """
    Interprets a simple assembly-like language and returns the final state of registers.

    Supported instructions:
      mov x y - copies y (constant or register) into register x
      inc x   - increases register x by 1
      dec x   - decreases register x by 1
      jnz x y - jumps to instruction y steps away if x is not zero

    :param program: List of strings, each representing an instruction
    :return: Dictionary with register names as keys and their integer values
    """
    registers = {}
    pc = 0  # Program counter

    while pc < len(program):
        instruction = program[pc].strip()
        if not instruction or instruction.startswith(
            ";"
        ):  # Skip empty or comment lines
            pc += 1
            continue

        parts = instruction.split()
        op = parts[0]

        if op == "mov":
            x, y = parts[1], parts[2]
            # If y is a register, get its value; otherwise, assume it's an integer
            val = registers[y] if y in registers else int(y)
            registers[x] = val

        elif op == "inc":
            x = parts[1]
            registers[x] += 1

        elif op == "dec":
            x = parts[1]
            registers[x] -= 1

        elif op == "jnz":
            x, y = parts[1], parts[2]
            # Evaluate x: register or constant
            x_val = registers[x] if x in registers else int(x)
            # Evaluate y: register or constant
            y_val = registers[y] if y in registers else int(y)

            if x_val != 0:
                pc += y_val  # Jump relative to current position
                continue  # Skip incrementing pc

        # Move to next instruction
        pc += 1

    return registers


def calc(expr: str):
    ex = list(expr.replace(" ", ""))

    def peek():
        return ex[0] if ex else ""

    def get():
        return ex.pop(0)

    def number():
        result = get()
        while peek() >= "0" and peek() <= "9" or peek() == ".":
            result += get()
        return float(result)

    def factor():
        if peek() >= "0" and peek() <= "9":
            return number()
        elif peek() == "(":
            get()  # '('
            result = expression()
            get()  # ')'
            return result
        elif peek() == "-":
            get()
            return -factor()
        return 0  # error

    def term():
        result = factor()
        while peek() == "*" or peek() == "/":
            if get() == "*":
                result *= factor()
            else:
                result /= factor()
        return result

    def expression():
        result = term()
        while peek() == "+" or peek() == "-":
            if get() == "+":
                result += term()
            else:
                result -= term()
        return result

    return expression()


def all_permuted(array_length):
    if array_length == 0:
        return 1
    elif array_length == 1:
        return 0

    # Using iterative dynamic programming approach
    derangements = [0] * (array_length + 1)
    derangements[0] = 1  # !0 = 1
    derangements[1] = 0  # !1 = 0

    for i in range(2, array_length + 1):
        derangements[i] = (i - 1) * (derangements[i - 1] + derangements[i - 2])

    return derangements[array_length]


def knight(from_pos, to_pos):
    """
    Returns the minimum number of moves a knight needs to get
    from one position to another on a chessboard.

    Args:
        from_pos (str): Starting position in algebraic notation (e.g. 'a3')
        to_pos (str): Target position in algebraic notation (e.g. 'b5')

    Returns:
        int: Minimum number of moves, or 0 if start == end
    """
    if from_pos == to_pos:
        return 0

    # Convert algebraic notation to (row, col) where a1 = (0,0), h8 = (7,7)
    def algebraic_to_coords(pos):
        col = ord(pos[0].lower()) - ord("a")  # a->0, b->1, ..., h->7
        row = int(pos[1]) - 1  # 1->0, 2->1, ..., 8->7
        return row, col

    start = algebraic_to_coords(from_pos)
    target = algebraic_to_coords(to_pos)

    # Check if positions are valid
    def is_valid(r, c):
        return 0 <= r < 8 and 0 <= c < 8

    if not (is_valid(start[0], start[1]) and is_valid(target[0], target[1])):
        raise ValueError("Invalid chess position")

    # Knight moves: 8 possible L-shaped moves
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    # BFS to find shortest path
    queue = deque([(start[0], start[1], 0)])  # (row, col, moves)
    visited = set()
    visited.add(start)

    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and (nr, nc) not in visited:
                if (nr, nc) == target:
                    return dist + 1
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return 0  # This should never happen on 8x8, but safety fallback


def first_non_repeating_letter(s):
    """
    Returns the first character in the string that is not repeated,
    ignoring case when determining repetition, but preserving the
    original case in the returned character.

    If all characters are repeated, returns an empty string.

    Args:
        s (str): Input string (can include Unicode characters)

    Returns:
        str: The first non-repeating character, or "" if none exists
    """
    # Create a case-insensitive count of characters
    char_count = {}
    for char in s:
        key = char.lower()  # Case-insensitive counting
        char_count[key] = char_count.get(key, 0) + 1

    # Traverse the original string and find the first char with count == 1
    for char in s:
        if char_count[char.lower()] == 1:
            return char

    return ""


def isPP(n):
    """
    Checks if n is a perfect power (n = m^k, k >= 2).
    Returns [m, k] if true, otherwise None.
    """
    if n < 2:
        return None  # By definition, perfect powers in this context are >= 2

    # We'll try exponents k starting from 2 upwards.
    # The maximum exponent k we need to try is log2(n), because 2^k <= n
    max_k = math.floor(math.log(n, 2)) + 1  # Safe upper bound

    for k in range(2, max_k + 1):
        # Compute m = n^(1/k), rounded to nearest integer
        m = round(n ** (1 / k))

        # We only need to check m and possibly m-1 or m+1 due to rounding
        # But usually m is either floor or ceil
        for candidate in (m - 1, m, m + 1):
            if candidate < 2:
                continue
            if candidate**k == n:
                return [candidate, k]

    return None


def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x) ** 2)
    return int(ret)


def hex_string_to_RGB(hex_string):
    # your code here
    hex_color = hex_string.lstrip("#").upper()

    # Extract the red, green, and blue components
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Return as a dictionary
    return {"r": r, "g": g, "b": b}


def last_digit(a: int, b: int) -> int:
    """
    Returns the last decimal digit of a^b.
    Handles very large a and b efficiently using modular arithmetic.
    Assumes 0^0 = 1.
    """
    # Special case: 0^0 is defined as 1
    if b == 0:
        return 1  # since a^0 = 1 for any a, and problem says 0^0 = 1

    # Get the last digit of the base
    last_digit_a = a % 10

    # If the base ends with 0, then a^b ends with 0 for b > 0
    if last_digit_a == 0:
        return 0
    if last_digit_a == 1:
        return 1

    # Define cycles for last digits of powers
    cycles = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],  # 2^1=2, 2^2=4, 2^3=8, 2^4=6, 2^5=2...
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }

    cycle = cycles[last_digit_a]
    cycle_length = len(cycle)

    # Reduce exponent modulo cycle length
    # But note: if b mod cycle_length == 0, we want cycle[cycle_length - 1]
    # because it's the last element in the cycle
    reduced_exp = b % cycle_length
    index = reduced_exp - 1 if reduced_exp != 0 else cycle_length - 1

    return cycle[index]


def number_of_pairs(gloves):
    """
    Determine the number of pairs of gloves that can be formed
    from the given list of glove colors.

    Each pair consists of two gloves of the same color.

    Args:
        gloves (list): List of strings representing glove colors

    Returns:
        int: Number of pairs that can be formed
    """
    if not gloves:
        return 0

    # Count frequency of each color
    color_count = {}
    for color in gloves:
        color_count[color] = color_count.get(color, 0) + 1

    # Count pairs: for each color, number_of_pairs = count // 2
    total_pairs = 0
    for count in color_count.values():
        total_pairs += count // 2

    return total_pairs


class RomanNumerals:
    # 罗马数字符号映射表（按值降序排列，便于转换）
    ROMAN_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    # 罗马数字到整数的映射
    ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # 有效的减法对
    SUBTRACTIVE_PAIRS = {"IV", "IX", "XL", "XC", "CD", "CM"}

    @staticmethod
    def to_roman(val: int) -> str:
        """
        将整数转换为罗马数字

        Args:
            val: 要转换的整数 (1-3999)

        Returns:
            str: 对应的罗马数字字符串

        Raises:
            ValueError: 如果输入不在有效范围内
            TypeError: 如果输入不是整数
        """
        # 输入验证
        if not isinstance(val, int):
            raise TypeError(f"Expected integer, got {type(val).__name__}")

        if not 1 <= val <= 3999:
            raise ValueError(f"Value {val} is out of range (1-3999)")

        result = []
        remaining = val

        # 使用贪心算法进行转换
        for number, symbol in RomanNumerals.ROMAN_SYMBOLS:
            while remaining >= number:
                result.append(symbol)
                remaining -= number

        return "".join(result)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        将罗马数字转换为整数

        Args:
            roman_num: 罗马数字字符串

        Returns:
            int: 对应的整数值

        Raises:
            ValueError: 如果输入不是有效的罗马数字
            TypeError: 如果输入不是字符串
        """
        # 输入验证
        if not isinstance(roman_num, str):
            raise TypeError(f"Expected string, got {type(roman_num).__name__}")

        roman_num = roman_num.strip().upper()

        if not roman_num:
            raise ValueError("Empty Roman numeral string")

        # 验证字符有效性
        invalid_chars = set(roman_num) - set(RomanNumerals.ROMAN_VALUES.keys())
        if invalid_chars:
            raise ValueError(f"Invalid Roman numeral characters: {invalid_chars}")

        total = 0
        i = 0
        n = len(roman_num)

        # 解析罗马数字
        while i < n:
            # 检查是否是减法对（两个字符的组合）
            if i + 1 < n:
                pair = roman_num[i : i + 2]
                if pair in RomanNumerals.SUBTRACTIVE_PAIRS:
                    # 处理减法对
                    first_val = RomanNumerals.ROMAN_VALUES[roman_num[i]]
                    second_val = RomanNumerals.ROMAN_VALUES[roman_num[i + 1]]
                    total += second_val - first_val
                    i += 2
                    continue

            # 处理单个字符
            total += RomanNumerals.ROMAN_VALUES[roman_num[i]]
            i += 1

        # 验证转换结果的一致性（可选，确保没有无效的罗马数字）
        if RomanNumerals.to_roman(total) != roman_num:
            raise ValueError(f"Invalid Roman numeral sequence: {roman_num}")

        return total
