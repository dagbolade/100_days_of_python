# setting her standards
class HerStandards:
    # set attributes
    def __init__(self, age_range, interests, occupation, education_level, hobbies, biblical_standards):
        self.age_range = age_range
        self.interests = interests
        self.occupation = occupation
        self.education_level = education_level
        self.hobbies = hobbies
        self.biblical_standards = biblical_standards

    # create another class attributes for biblical standards
class BiblicalStandards:
        # set attributes
    def __init__(self, righteousness, wisdom, faithfulness, love, patience, strength, kindness, gentleness,
                 self_control):
        self.righteousness = righteousness
        self.wisdom = wisdom
        self.faithfulness = faithfulness
        self.love = love
        self.patience = patience
        self.strength = strength
        self.kindness = kindness
        self.gentleness = gentleness
        self.self_control = self_control

# create a class profile for him
class GuyProfile:
    # set attributes
    def __init__(self, name,age, interests, occupation, education_level, hobbies, biblical_attributes):
        self.age = age
        self.name = name
        self.interests = interests
        self.occupation = occupation
        self.education_level = education_level
        self.hobbies = hobbies
        self.biblical_attributes = biblical_attributes

# create a function to check if he meets her standardss
def is_match(guy, standards):
    # check if the guy's age is within the
    # age range of the standards
    age_match = standards.age_range[0] <= guy.age <= standards.age_range[1]
    interests_match = any(interest in guy.interests for interest in standards.interests)
    occupation_match = guy.occupation in standards.occupation
    education_level_match = guy.education_level in standards.education_level
    hobbies_match = any(hobby in guy.hobbies for hobby in standards.hobbies)


    # count the number of biblical standards that the guy meets
    biblical_attributes_match_count = sum(
        getattr(guy.biblical_attributes, attr) == getattr(standards.biblical_standards, attr)
        for attr in vars(standards.biblical_standards)
    )
    biblical_match = biblical_attributes_match_count >= 4  # At least 4 attributes match

    return age_match and interests_match and occupation_match and education_level_match and hobbies_match and biblical_match

# create a function to ask for the guy's profile
def get_guy_profile():
    name = input("Enter your name: ").lower()
    age = int(input("Enter your age: "))
    interests = input("Enter your interests separated by commas (e.g., music, travel): ").split(", ")
    occupation = input("Enter your occupation: ")
    education = input("Enter your highest level of education (e.g., Bachelor's, Master's, PhD): ")
    hobbies = input("Enter your hobbies separated by commas (e.g., yoga, painting): ").split(", ")
    # New biblical attributes input
    righteousness = input("Are you righteous? (y/n): ").lower() == "y" or "yes"
    wisdom = input("Are you wise? (y/n): ").lower() == "y" or "yes"
    faithfulness = input("Are you faithful? (y/n): ").lower() == "y" or "yes"
    strength = input("Are you strong? (y/n): ").lower() == "y" or "yes"
    kindness = input("Are you kind? (y/n): ").lower() == "y" or "yes"
    gentleness = input("Are you gentle? (y/n): ").lower() == "y" or "yes"
    self_control = input("Do you have self control? (y/n): ").lower() == "y" or "yes"
    love = input("Are you loving? (y/n): ").lower() == "y" or "yes"
    patience = input("Do you have patience (y/n): ").lower() == "y" or "yes"


    biblical_attributes = BiblicalStandards(righteousness, wisdom, faithfulness, love, patience, strength, kindness, gentleness,
                 self_control)
    return GuyProfile(name, age, interests, occupation, education, hobbies, biblical_attributes)

# standards for her
her_standards = HerStandards(
    age_range=(25, 35),
    interests=["music", "travel", "reading", "cooking", "hiking"],
    occupation=["engineer", "doctor", "lawyer", "teacher", "Data Scientist", "Software Engineer"],
    education_level=["Bachelor's", "Master's", "PhD"],
    hobbies=["yoga", "painting", "cooking", "gym"],
    biblical_standards=BiblicalStandards(
        righteousness=True,
        wisdom=True,
        faithfulness=True,
        love=True,
        patience=True,
        strength=True,
        kindness=True,
        gentleness=True,
        self_control=True
    )
)

# get the guy's profile
guy_profile = get_guy_profile()

# check if the guy meets her standards
# Finding match
if is_match(guy_profile, her_standards):
    print(f"{guy_profile.name}, you are a match!")
else:
    print(f"Sorry, {guy_profile.name}, you are not a match.")


