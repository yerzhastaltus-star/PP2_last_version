#1
import re

s = input()

# ^a  the string must begin with 'a'
# .* then anything can follow (any characters, any length)
# b   but somewhere after that there must be 'b'
# So we are checking: does it start with 'a' and contain 'b' after?
x = re.findall("^a.*b", s)

if x:
    print("Match")
else:
    print("No match")
    
#2import re

s = input()

# ^a  must start with 'a'
# b{2,3}  then exactly 2 or 3 letters 'b'
# So valid examples: abb, abbb
# Invalid: ab (only one b), abbbb (too many b's)
x = re.findall("^ab{2,3}", s)

if x:
    print("Match")
else:
    print("No Match")
    
#3
import re

s = input()

# ^[a-z]+ start with lowercase letters
# [_]   then exactly one underscore
# [a-z]+   then lowercase letters again
# Basically we are checking something like: hello_world
x = re.findall("^[a-z]+[_][a-z]+", s)

print(x)

if x:
    print("Match")
else:
    print("No Match")
#4
import re

s = input()

# ^[A-Z]  first letter must be capital
# [a-z]+  after that, only lowercase letters
# This matches proper words like: London, Paris
x = re.findall("^[A-Z][a-z]+", s)

print(x)

if x:
    print("Match")
else:
    print("No Match")
#5
import re

s = input()

# a there must be letter 'a'
# .+ at least one character after 'a'
# b$ and the string must end with 'b'
# So it checks: starts somewhere with 'a' and ends with 'b'
x = re.findall("a.+b$", s)

print(x)

if x:
    print("Match")
else:
    print("No Match")
#6
import re

s = input()

# [ ,.]  find space OR comma OR dot
# replace them with colon :
# So we are cleaning punctuation and making it uniform
r = re.sub("[ ,.]", ":", s)

print(r)
#7
import re

s = input()

# [_]   find underscore
# ""    replace it with nothing
# So we simply remove underscores
r = re.sub("[_]", "", s)

print(r)
#8
import re

s = input()

# [A-Z]  find a capital letter
# [a-z]*  followed by lowercase letters (if any)
# This extracts words like: Hello, World, Astana
result = re.findall(r'[A-Z][a-z]*', s)

print(result)
#9
import re

s = input()

# (?<!^)  make sure we are NOT at the start of the string
# ([A-Z]) find capital letter
# " \1"   add space before that letter
# This turns: HelloWorld → Hello World
result = re.sub(r"(?<!^)([A-Z])", r" \1", s)

print(result)
#10
import re

s = input()

# (?<!^)  not at the beginning
# ([A-Z]) find capital letter
# add underscore before it
# then convert everything to lowercase
# This turns: HelloWorld → hello_world
result = re.sub(r"(?<!^)([A-Z])", r"_\1", s).lower()

print(result)