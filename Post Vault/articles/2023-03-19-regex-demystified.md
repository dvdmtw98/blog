---
title: 'Regex Demystified'
date: '2023-03-19 13:05:00 +0530'
categories: [Programming, Python]
tags: [programming, regex, python, software-development]
published: true
img_path: /assets/
---

![Regex Demystified Banner](images/regex-demystified/regex-demystified-banner.png)

Regex (also called Regular Expression or RegExp) is a sequence of characters that can be used to find or match patterns in text. Regexes are made up of special characters (metacharacters) that allow to define complex patterns in a terse and concise manner.

Regexes has a broad range of real world applications such as user input validation, parsing long structured files for important information, web scrapping, transforming text from one format to another as well as for find and replace operations.

To a user that comes across regex for the first time it will feel like they are trying to read incomprehensible garbled text, but once they start understanding the characters that make up the madness they will soon realize that they have just unlocked a super power that can literally save the day (no pun intended). This feeling is summed up perfectly by xkcd.

![Regex Saves the Day|450](https://imgs.xkcd.com/comics/regular_expressions.png)

One really nice thing about regex is that once we learn its syntax we can pretty much use it in any programming language (Python, JavaScript, Perl, Rust, PowerShell, etc.) with little to no modification.

Lets get started by learning the metacharacters that make up Regular Expressions. 

### Basic Concepts

#### Anchor Characters

The `^` and `$` characters are called anchor characters. They allow to match a pattern that occurs at the start or end of a string. Anchor characters are special as they does not consume any visible character instead they match on the invisible character that denotes the start or end a string. 

>**\^The**: Matches any string that starts with the word The  
>
>**end$**: Matches any string that ends with the word end  
>
>**^The end$**: Matches any string that starts with The and end with end  
>
>**dog**: Matches any string that contains the word dog (Does not have to be at the start or end)

#### Qualifiers

 `*`, `?`, `+` and `{}` are collectively called qualifiers. These characters are used to control the number of times a certain character should be matched by the regex engine.

>**abc\***: Matches a string that contains ab followed by c zero or more times
>
>**abc?**: Marches a string that contains ab followed by c zero or one time
>
>**abc+**: Matches a string that contains ab followed by c zero or more times
>
>**abc{2,}**: Matches a string that contains ab followed by c 2 or more times
>
>**abc{3}**: Matches a string that contains ab followed by c exactly 3 times
>
>**abc{2,5}**: Matches a string that contains ab followed by c at least 2 times up to a max of 5 times

#### OR Operator

`|` and `[]` are used to create OR logic

>**ab(c|d)**: Matches a string that contains ab followed by c or d
>
>**ab[cd]**: Matches a string that contains ab followed by c or d

The `()` in the above regex is a capture group, capture groups will be covered in the intermediate concepts section.

#### Character Classes

Character classes are shorthand notations to represent commonly used character sets. `\d`, `\w` and `\s` make up the mostly commonly used character classes.

>**\\d**: Matches a single digit character
>
>**\\w**: Matches a single word character (Alphanumeric characters and underscore)
>
>**\\s**: Matches a single whitespace character including newline character and tab

These character classes also have negated versions that match on the characters that are not matches by their positive counterpart

>**\\D**: Matches on a single non-digit character
>
>**\\W**: Match on a single non-word character (All characters leaving alphanumeric characters and underscore)
>
>**\\S**: Matches on any non-whitespace character

The `.` is an special character class that matches on all character leaving the new line character

>**.** : Matches on all characters (leaving newline)

There are also metacharacter to denote newlines and tabs

>**\\n**: Matches on newline characters
>
>**\\t**: Matches on tab characters

There are other more advanced character classes as well which are useful to match based on Unicode characters, Mathematical symbols, emojis or alphabets from other languages.

[Regex Tutorial - Unicode Characters and Properties](https://www.regular-expressions.info/unicode.html)

#### Regex Flags

Flags are toggles used to tell the regex engine to evaluate the input string in a certain way. Depending on the programming language being used there can be additional flags.

>**g** : Global Flag (Tells the regex engine to not stop evaluating the string after the first match was found)
>
>**i** : Insensitive Flag (Makes the whole expression case insensitive i.e. uppercase and lowercase characters will be considered the same)
>
>**m** : Multiline Flag (Makes the `^` and `$` anchor tags match the start and end of each line instead of the start and end of the string)
 
### Intermediate Concepts

#### Capture Groups

Groups are a very powerful feature of regex which allows us to find and store the pattern that matches the group so that it can be used later.

Capture Groups are created using `()`. They come in two variants: anonymous and named.

>**ab(cd)**: Matches on occurrences of string abcd. All occurrence of cd in the matches will be stored to be accessed later
>
>**ab(?\<foo>bc)**: Same as above but allows to access the capture using the name 'foo'
>
>**ab(?:bc)**: Creates an non-capturing group (i.e. bc will not be stored for later access)

#### Bracket Expression

While `[]` can be used as an OR expression its main usage is to create custom character classes. `^` when used inside an bracket expression as the first character negates the entire expression.  `-` that occur in-between characters are used to denote character ranges. 

>**[a-zA-Z]**: Matches on characters that is in the range a-z and A-Z
>
>**[a-fA-F0-9]**: Matches on characters that is in the range a-f, A-F and 0-9
>
>**[\^a-zA-Z]**: Matches on characters that is not in the range a-z and A-Z
>
>**[a-zA-Z\\^]**: Matches on character that is `^` or in the range a-z and A-Z

#### Boundary Anchor

Word Boundary or `\b` is a special type of anchor that makes on a invisible character called word boundary. A word boundary exists in the space between a word and a non-word character. There is also a negated version `\B` that matches on the invisible character that is present in the space between two word characters.

>**\\babc\\b**: Matches all occurrence of abc that is surrounded by a non-word characters
>
>**\\Babc\\B**: Matches all occurrences of abc that are surrounded by word characters (i.e. abc is contained inside a word)

#### Greedy & Lazy Match

The quantifies (`*`, `+`, `{}`) are evaluated greedily by the regex engines i.e. they try to find the largest string that matches the provided regex. Sometimes this is not what we want, in these cases we can tell the engine to evaluate the quantifiers lazily i.e. find the smallest match. This is done by using the `?` character right after the quantifier that should be evaluated lazily.

>**<.+?>**: Match on `<` followed by any character until `>` is found in a lazy manner i.e. smallest match

### Advanced Concepts

#### Lookahead and Lookbehind

Lookahead and Lookbehind expressions are used to match a string that is followed or preceded by a specific pattern. The pattern that follows or precedes the string we want to match is not included in the regex match.

There are negative versions of lookahead and lookbehind that matches a string when it is not followed or preceded by a specific pattern.

>**a(?=b)**: Matches all occurrences of a that are followed by b
>
>**(?<=b)a**: Matches all occurrences of a that are preceded by a
>
>**a(?!b)**: Matches all occurrences of a that are not followed by b
>
>**(?<!a)b**: Matches all occurrences of b that are not preceded by a

#### Backreference

Backreferences are special constructs that allow to reference a capture group that was defined previous in the regex string. Since backreferences are based on capture groups we can have anonymous as well as named backreferences.

>**(ab|c)\\1**: Matches all occurrences of aa, bb and cc i.e. the character matched by the capture group repeated again
>
>**(?\<foo>a|b|c)\\k\<foo>**: The same as above but using a named capture group

### Examples

Now lets solve some examples to put to use everything that we have already learned

#### Email Id Validation

Lets imagine that we have been provided with a list of email ids and we have been tasked with splitting the emails into three segments. The first part should contain everything before the `@` sign, the second part should contain the name of the email id provider and everything else after that should be captured in group 3.

[Email Id Validation Regex - regex101](https://regex101.com/r/CMS40h/1)

We could easily achieve the same using Python as follows:

```python
email_id_list = [
	'David.Varghese@gmail.com',
	'johnsnow123@yahoo.co.uk',
	'thepirateking@rediff-mail.com'
]

regex_pattern = r"([\w.-]+)@([a-zA-Z-]+)(\..+)"
for email_id in email_id_list:
	regex_result = re.search(regex_pattern, email_id).groups(0)
	print(regex_result)

# Output
('David.Varghese', 'gmail', '.com')
('johnsnow123', 'yahoo', '.co.uk')
('thepirateking', 'rediff-mail', '.com')
```

Since we want the email as three separate segments we need to use three capture groups

`[\w.-]+`: One or more occurrence of word character, period or hyphen  

`@` : The `@` character

`[a-zA-Z-]+`: One or more occurrence of uppercase, lowercase characters and hyphen

`\..+`: The period character followed by any character one or more time

#### Username Validation

This time lets imagine we are a frontend developer and our website has a input field for the user to enter a username we need to ensure that the username is 5 to 30 characters long. It must contain at least one uppercase character cannot end in hyphen or period and can only have alphanumeric characters, period and hyphen.

[Username Validation Regex - regex101](https://regex101.com/r/ZK2cXl/1)

```python
username_list = [
	'David Varghese',
	'JohnDoe-123',
	'Jane123Smith',
	'JamesGrey.'
]

regex_pattern = r"^(?=[A-Z]+)[a-z0-9A-Z-.]{5,30}(?<![-.])$"
for username in username_list:
	regex_result = re.match(regex_pattern, username)
	if regex_result:
		print(f"{username} -> Pass")
	else:
		print(f"{username} -> Fail")

# Output
David Varghese -> Fail
JohnDoe-123 -> Pass
Jane123Smith -> Pass
JamesGrey. -> Fail
```

`^` : Match pattern from start of string

`(?=[A-Z]+)`: Lookahead and match if one or more uppercase character found

`[a-z0-9A-Z-.]{5,30}`: Check if username contains only valid characters and is of the required length

`(?<![-.])`: Negative lookbehind to not match if input ends with `-` or `.`

`$`: Match pattern till end of string

#### Password Validation

We are working on the frontend of the same application from the last exercise this time we want to validate a password and by company policy we need to ensure that the password is at least 12 characters long can contain alphanumeric characters along with a few special symbols (can assume any 4-5 special characters). Additionally it is mandatory that at least on uppercase, lowercase, digit and special character is used. 

[Password Validation Regex - regex101](https://regex101.com/r/7lnV3N/1)

```python
password_list = [
	'mypassword@123',
	'superSecretPa$$word123',
	'sUp@rPa$$12'
]

regex_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$"
for password in password_list:
	regex_result = re.match(regex_pattern, password)
	if regex_result:
		print(f"{password} -> Pass")
	else:
		print(f"{password} -> Fail")

# Output
mypassword@123 -> Fail
superSecretPa$$word123 -> Pass
sUp@rPa$$12 -> Fail
```

`^`: Match from the start of the string

`(?=.*[a-z])`: Lookahead to check if there is a lowercase character

`(?=.*[A-Z])`: Lookahead to check if there is a uppercase character

`(?=.*\d)`: Lookahead to check if there is a digit

`(?=.*[@$!%*?&])`: Lookahead to check if there is a special character

`[A-Za-z\d@$!%*?&]{12,}`: Check if input contains only the allowed characters and has a length of at least 12

`$`: Match till the end of the string

### References

- [Learn Regex: A Beginner's Guide - SitePoint](https://www.sitepoint.com/learn-regex/)
- [Regular Expression Tutorial Table of Contents](https://www.regular-expressions.info/tutorialcnt.html)
- [Regex tutorial - A quick cheatsheet by examples \| by Jonny Fox \| Factory Mind \| Medium](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
- [Regular Expressions Clearly Explained with Examples \| by Jason Chong \| Towards Data Science](https://towardsdatascience.com/regular-expressions-clearly-explained-with-examples-822d76b037b4)
- [Regular Expressions (Regex) Tutorial: How to Match Any Pattern of Text - YouTube](https://www.youtube.com/watch?v=sa-TUpSx1JA)
- [Novice to Advanced RegEx in Less-than 30 Minutes + Python - YouTube](https://www.youtube.com/watch?v=GyJtxd14DTc)