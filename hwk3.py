# !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!!
# You should not use the print() or input() functions anywhere in this file!
# !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!! !!WARNING!!



# Function 1: Same First Digit
#
# Define a function called same_first_digit() that takes in three numbers and
# returns True if they all have the same first digit and False otherwise.
#
# Hint: Mold data according to the way you are going to use it: it's a shame
#       you can't index into a number...
def same_first_digit(number_one, number_two, number_three):
    if number_one == number_two and number_two == number_three:
        return True
    else:
        return False


# Function 2: String Reversal
#
# Write a function called reverse() that takes in a string and gives back the
# the string with its characters in inverted order.
#
# Don't be a tool and just call the built-in function reversed()
def reverse(word):
    i=len(word)
    new_word=''
    while i>=0:
        new_word+=word[i-1]
        i-=1
    return new_word
# Function 3: Palindrome Detection
#
# Write a function called is_palindrome() which takes in a single string
# parameter.  The function should return True if the string is a palindrome and
# False otherwise.  A palindrome is a string which can be read in the same way
# both forward and backward, "mom" for example.  The case of the string should
# not affect correctly detecting a palindrome; neither should any spaces,
# commas, or apostrophes in the string.
#
# HINT: If only you could get rid of all the characters you don't care about
# some how.
#
# HINT: If only there was some way to obtain a backwards version of a string...
def is_palindrome(word):
    word.replace(' ','')
    if word.reverse==word:
        return True
    else:
        return False


# Function 4: String to ASCII Codes
#
# Write a function called str_to_ascii() that takes in a string and returns a
# list of integers where each integer is the ASCII code for the corresponding
# character in the string at that position.
#
# EX: str_to_ascii('abc') --> [97, 98, 99]
#
# HINT: If you dont know what ASCII is, Google "ASCII table"
#
# HINT: There is a built in function that can do the char --> ASCII code
#       conversion for you; you just have to find it.
def str_to_ascii(word):
    number=[]
    for i in word:
        number+=ord(i)
    return number



# Function 5: Get Piece Value
#
# Write a function called get_piece_value() which takes in the name of a chess
# piece as a string and returns a numeric value corresponding to the piece
# after this scheme:
#
# | piece  | value |
# |--------+-------|
# | pawn   |     1 |
# | bishop |     3 |
# | knight |     3 |
# | rook   |     5 |
# | queen  |     9 |
#
# If a string is given as input which is not the name of a valid piece, your
# function should return None.  Make sure this function works for strings with
# any combination of letter case as long as they are spelled right.
#
# To get the intended practice for this problem, don't use *any* if statements

def get_piece_value(chess_piece):
    piece_values = {
        'pawn': 1,
        'bishop': 3,
        'knight': 3,
        'rook': 5,
        'queen': 9
    }
    return piece_values.setdefault(chess_piece.lower, None)

# Function 6: Formatting Dates
#
# Write a function called format_date() which takes in a single parameter which
# is a string of the format yyyymmdd (like 20190209) and returns a string of
# the format "February 9th, 2019"
#
# Hint: One part of the date string is really easy, and one part has a
#       surprising number of edge cases

def format_date(date):
    formatted_year=date[0:4]
    numbered_months = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    formatted_month=numbered_months[date[4:6]]
    formatted_day=int(date[6:8])
    if formatted_day == 1 or formatted_day == 21 or formatted_day == 31:
       formatted_day = str(formatted_day) + 'st'
    elif formatted_day == 2 or formatted_day == 22:
       formatted_day = str(formatted_day) + 'nd'
    elif formatted_day == 3 or formatted_day == 23:
       formatted_day = str(formatted_day) + 'rd'
    else:
       formatted_day = str(formatted_day) + 'th'

    return formatted_month + ' ' + formatted_day + ', ' + formatted_year
