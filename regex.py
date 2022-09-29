import re
'''
match - match if the pattern is in the beginning of a line
search - seach matches the patten if it presents [ Only one pattern get matched ]
findall
sub
split
compile-finditer
'''

line="pet:cat i love cat pet:dog i love dog"
# matches=re.match(r"Pet:..{3}",line,re.I)
# print(matches.group())

# matches=re.search(r"Pet:...",line,re.I)
# print(matches.group())

# matches=re.findall(r"Pet:...",line,re.I)
# for x in matches:
#     print("Found :",x)

# print(re.sub("love","LIKE",line))
# print(line.replace('love','like'))
#
# print(re.split(" ",line))

myline="""
abcdefghijklmnopqrstuwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

~!@#$%^&*()_+

Ha HaHa

https://www.google.com
http://www.google.com
https://google.com
https://www.google.co.in

Raghul.Ramesh@gmail.com
RaghulRamesh@outlook.com
Raghul_Ramesh@yahoo.com
Ramesh@hotmail.com

675 545 3445
666-544-3221
123_343_1234
664.556.4546

+91-9898765499
9898765499
98987654999
989876549
8898765499
7898765499
6898765499
5898765499
4898765499
3898765499
2898765499
1898765499
"""
pattern=re.compile(r"(\+91\-)?\b[56789]\d{9}\b")
#pattern=re.compile(r"\d{3}[_\-\s\.]\d{3}[_\-\s\.]\d{4}")
#pattern=re.compile(r"(\w+\.)?\w+@\w+\.com")
#pattern=re.compile(r".")
#pattern=re.compile(r"\bHa\b")
#pattern=re.compile(r"https?://(www\.)?google\.com?(\.in)?")
matches=pattern.finditer(myline)
for x in matches:
    print(x.group())