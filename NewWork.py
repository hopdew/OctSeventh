x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s." % (binary, doNot)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)

# More stuff 10-8

print("Mary had a little lamb.)")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end7 + end8 + end9 + end10 + end11 + end12)

# More formatting
formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter % ("one", "two", "three", "four"))
print(formatter %  (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# Why %r instead of %s?

# Time for some strange stuff in the world of printing...
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFed\nMar\nApr\nMay\nJun\nJul\Aug"

print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
There's something going on here. 
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# What if I didn't like Jan being listed on the line with the rest of the
# text and away from the other months? How could I fix that?
    # backslash

# More escaping

tabbyCat = "\tI'm tabbed in."
ferret = "I'm split\non a line"
ok = "I'm \\ a \\ googooogoooooooo."
taskcat = """
I'll make a list:
\t* Oranges
\t* Obama
\t* Plants\n\t* Flower
"""

print(tabbyCat)
print(ferret)
print(ok)
print(taskcat)

# Escape seq                What does it do
# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N{name}
# \r
# \t
# \uzzz
# \Uxxxxxx
# \v
# \ooo
# \xhh

# what's the following code do:
#  while True:
#         for i in ["/","-","|","\\","|"]
#               print("%s\r" % i, ends='')

# can you replace """ with '''?
# Yes

fooso = '''Hows the wife
im aldlll
and no pie is no gain'''
andree = """ why ar eto being so lame 
what a dumb foosoo
im better"""
print(fooso)
print(andree)

# Asking Questions

racoon = input("How many racoons do you have?")
teeth = input("How many teeth do you have?")



print("So, you  have %r racoons and have %r teeth? Cool I guess." % (racoon, teeth))