#! python3
# Mad Libs generator

# Variables for nouns, verbs and adjectives + prompts
noun = input("Please enter a noun.\n").lower()
verb = input("Enter a verb.\n").lower()
verb2 = input("Enter another verb.\n").lower()
adjective = input("Enter an adjective.\n").lower()
location = input("Enter a location. (House, forest, etc.)")

# Sentences with the inputs added  
print(f"Once upon a time there was a {adjective} {noun}")
print(f"This {noun} loved to {verb} in the {location}.")
print(f"One time the {noun} {verb}d too fiercely and ended up {verb2}ing all day.")