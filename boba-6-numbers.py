# author thierryn
# date #nov 5 2025
#
# make a algorithm to gather data

# to find most popular

# bubble  tea places
#
import os

NUM_VOTERS = 5


# version 1
def vote_listed_choices():
    """dispay all choices
    5 user votes for their choice
    resluts will be printed"""
    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. heytea",
        "E. Coco",
        "F. Fresh T",
    ]
    # bucket for votes
    blenz = 0
    bubble_queen = 0
    sun_tea = 0
    heytea = 0
    coco = 0
    fresh_t = 0
    spoiled_votes = 0
    for _ in range(NUM_VOTERS):
        # clear screen
        os.system("clear")
        # show all choices
    print("Vote for your favourite from the list.")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)
    # ask user for their choice
    vote = input("Your vote").strip(".,/?!")
    # keep track with tally
    if vote == "a":
        blenz = blenz + 1
    elif vote == "b":
        bubble_queen += 1
    elif vote == "c":
        sun_tea += 1
    elif vote == "d":
        heytea += 1
    elif vote == "e":
        coco += 1
    elif vote == "f":
        fresh_t += 1
    else:
        spoiled_votes += 1
    # data analysis
    # give raw score
    print("Voting Results ---")
    print(f"Blenz: {blenz} votes")
    print(f"Bubble Queen: {bubble_queen} votes")
    print(f"Sun Tea: {sun_tea} votes")
    print(f"hey tea: {heytea} votes")
    print(f"CoCo: {coco} votes")
    print(f"Fresh T: {fresh_t} votes")
    print(f"Spoiled votes: {spoiled_votes} votes")
    # give score as percentage
    print("Vote share percentage ---")
    total = blenz + bubble_queen + sun_tea + heytea + coco + fresh_t + spoiled_votes
    print(f"Blenz: {blenz / total * 100} %")
    print(f"Bubble Queen: {bubble_queen / total * 100} %")
    print(f"Sun Tea: {sun_tea / total * 100} %")
    print(f"hey tea: {heytea / total * 100} %")
    print(f"CoCo: {coco / total * 100} %")
    print(f"Fresh T: {fresh_t / total * 100} %")
    print(f"Spoiled votes: {spoiled_votes / total * 100} votes")


# version2
# ask user for favourite boba place
# keep tally
# data analysis
# give raw scores
# give socres as a percentage
def vote_open_choice():
    """Keeps track dynamically of user's choice.
    Note: choices must match text exactly (case is not sensitive)"""

    votes = {}  # holds vote information    key     -> value
    #                           place   -> num votes

    for _ in range(NUM_VOTERS):
        # Ask the user what their fave
        os.system("clear")
        cur_vote = (
            input("What's your favourite local bubbble tea cafe? ")
            .lower()
            .strip(",.?! ")
        )

        # Checks if current place is in the votes dictionary
        # If it doesn't exist, initialize the key-value pair
        if cur_vote not in votes:
            votes[cur_vote] = 1
        else:
            votes[cur_vote] += 1

    # Print the results
    print("-------------------------------------")
    print("Results:")

    # By default, iterating over a dictionary gives you the keys
    for place in votes:
        # Print the raw score and percentage for each key in the dictionary
        percentage = votes[place] / NUM_VOTERS * 100

        print(
            f"{place.capitalize()} votes: {votes[place]} | percentage: {percentage}% of the vote"
        )

    print("-------------------------------------")


def chip_rater():
    """Help gather data about chip crispness
    and quality."""
    questions = [
        "How cripsy is the chip out of 5? 0 is mushy, 5 is super crisp.",
        "How would you rate the taste out of 5? 0 is unpalatable, 5 is gourmet.",
        "How fresh would you rate the chip out of 5? 0 is stale, 5 is pristine.",
        "How would you rate the size of the chip out of 5?",
    ]

    # Bucket to hold total ratings
    total_ratings = 0

    # Give the test subject instructions
    print("Take one chip from the bag.")
    print("Eat it mindfully.")
    print("Give your rating.")

    # Ask questions to the subject
    for question in questions:
        print(question)

        # get their rating for that question
        # out of five
        rating = int(input().strip(",.?! "))

        total_ratings += rating

    # Print out the average rating out of five
    average = total_ratings / len(questions)

    print(f"The average rating is {average} *s!")


def main():
    vote_listed_choices()
    chip_rater()
    vote_open_choice()


if __name__ == "__main__":
    main()
