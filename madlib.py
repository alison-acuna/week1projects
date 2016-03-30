noun_1 = input("Choose a noun: ")
noun_plural = input("Choose a plural noun: ")
noun_2 = input("Choose another noun: ")
place = input("Choose a place: ")

mad_lib = """
Be kind to your 1-footed {noun1}
For a duck may be somebody`s {noun3},
Be kind to your {noun2} in {place}
"""

print(mad_lib.format(noun1=noun_1, noun3=noun_plural, noun2=noun_2, place=place))
