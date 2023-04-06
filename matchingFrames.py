from thefuzz import fuzz, process

'''
Fuzzy string matching is similar to using regex operation, equal operands and comparators. Similar to wildcards
'''

string1 = "Hello World"
string2 = "hello world"
string3 = "hello world !"
print(string1 == string2) ## checking for exact equality amongst strings
#Could potentially convert strings to a standard form and compare 
print(string1.lower() == string2) ## checking for exact equality amongst strings with conversion
print(string1.lower() == string3) ## strings are similar but due to no exact match we miss out on a potential high similarity match


string4 = "Just a thefuz experiment"
string5 = "just a thefuz experiment"
print(f'The similarity between both the sentences using fuzzy logic is {fuzz.ratio(string4, string5)}%')


string6 = "Just a thefuz experiment"
string7 = "just a thefuz experiment and some code"
print(f'The similarity between both the sentences using fuzzy logic is {fuzz.ratio(string6, string7)}%')
print(f'The similarity between both the sentences using fuzzy logic is {fuzz.partial_ratio(string6, string7)}%')
# partial ratio looks at substrings within our string

string8 = "The quick brown fox jumped of the lazy hen"
string9 = "The lazy hen was jumped over by the quick brown fox"
print(f'The similarity between both the sentences using fuzzy logic is {fuzz.ratio(string8, string9)}%')
print(f'The similarity between both the sentences using fuzzy logic is {fuzz.partial_ratio(string8, string9)}%')
print(f'The similarity between both the sentences using fuzzy logic is {fuzz.token_sort_ratio(string8, string9)}%')

#Matching from a array
arrFuzzTest = ["Programming", "Kotlin Language", "Java Language", "Spark Framework", "React Framework", "English language"]
print(process.extract("Language", arrFuzzTest, limit=3))