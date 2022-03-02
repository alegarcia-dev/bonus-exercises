import pandas as pd
import numpy as np

# Complete each exercise in plain python, with list comprehension, and with pandas

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

vowels = list('aeiou')

fruit_series = pd.Series(fruits)
number_series = pd.Series(numbers)

# Exercise 1 - Make a variable named uppercased_fruits and create a list of all of the list of strings in fruits and uppercases every string. Output should be ['MANGO', 'KIWI', etc...]

# - Plain Python
uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())
print(uppercased_fruits)

# - List Comprehension
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# - Pandas
uppercased_fruits = pd.Series(fruits).str.upper()
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# - Plain Python
capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())
print(capitalized_fruits)

# - List Comprehension
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# - Pandas
capitalized_fruits = fruit_series.str.capitalize()
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# - Plain Python
def count_vowels(word):
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    return count

fruits_with_more_than_two_vowels = []
for fruit in fruits:
    if count_vowels(fruit) > 2:
        fruits_with_more_than_two_vowels.append(fruit)
print(fruits_with_more_than_two_vowels)

# - List Comprehension
def count_vowels(word):
    return sum(ch in vowels for ch in word)

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]
print(fruits_with_more_than_two_vowels)

# - Pandas
fruits_with_more_than_two_vowels = fruit_series[fruit_series.str.count('[aeiou]') > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# - Plain Python
def count_vowels(word):
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    return count

fruits_with_only_two_vowels = []
for fruit in fruits:
    if count_vowels(fruit) == 2:
        fruits_with_only_two_vowels.append(fruit)
print(fruits_with_only_two_vowels)

# - List Comprehension
def count_vowels(word):
    return sum(ch in vowels for ch in word)

fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) == 2]
print(fruits_with_only_two_vowels)

# - Pandas
fruits_with_only_two_vowels = fruit_series[fruit_series.str.count('[aeiou]') == 2]
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters

# - Plain Python
fruits_with_more_than_5_chars = []
for fruit in fruits:
    if len(fruit) > 5:
        fruits_with_more_than_5_chars.append(fruit)
print(fruits_with_more_than_5_chars)

# - List Comprehension
fruits_with_more_than_5_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_5_chars)

# - Pandas
fruits_with_more_than_5_chars = fruit_series[fruit_series.str.len() > 5]
print(fruits_with_more_than_5_chars)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# - Plain Python
fruits_with_5_chars = []
for fruit in fruits:
    if len(fruit) == 5:
        fruits_with_5_chars.append(fruit)
print(fruits_with_5_chars)

# - List Comprehension
fruits_with_5_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_5_chars)

# - Pandas
fruits_with_5_chars = fruit_series[fruit_series.str.len() == 5]
print(fruits_with_5_chars)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# - Plain Python
fruits_with_less_than_5_chars = []
for fruit in fruits:
    if len(fruit) < 5:
        fruits_with_less_than_5_chars.append(fruit)
print(fruits_with_less_than_5_chars)

# - List Comprehension
fruits_with_less_than_5_chars = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_5_chars)

# - Pandas
fruits_with_less_than_5_chars = fruit_series[fruit_series.str.len() < 5]
print(fruits_with_less_than_5_chars)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# - Plain Python
num_chars_per_fruit = []
for fruit in fruits:
    num_chars_per_fruit.append(len(fruit))
print(num_chars_per_fruit)

# - List Comprehension
num_chars_per_fruit = [len(fruit) for fruit in fruits]
print(num_chars_per_fruit)

# - Pandas
num_chars_per_fruit = fruit_series.str.len()
print(num_chars_per_fruit)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# - Plain Python
fruits_with_letter_a = []
for fruit in fruits:
    if 'a' in fruit:
        fruits_with_letter_a.append(fruit)
print(fruits_with_letter_a)

# - List Comprehension
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)

# - Pandas
fruits_with_letter_a = fruit_series[fruit_series.str.contains('a')]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# - Plain Python
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# - List Comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# - Pandas
even_numbers = number_series[number_series % 2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# - Plain Python
odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)

# - List Comprehension
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

# - Pandas
odd_numbers = number_series[number_series % 2 != 0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# - Plain Python
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
print(positive_numbers)

# - List Comprehension
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

# - Pandas
positive_numbers = number_series[number_series > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# - Plain Python
negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)
print(negative_numbers)

# - List Comprehension
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)

# - Pandas
negative_numbers = number_series[number_series < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
