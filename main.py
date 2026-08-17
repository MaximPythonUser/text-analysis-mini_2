def count_vowels(string):
    VOWELS = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1



    return count


print(count_vowels("hello, world!"))
print(count_vowels("Python is a very powerful language."))
