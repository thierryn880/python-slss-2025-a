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


def main():
    vote_listed_choices()
    chip_rater()


if __name__ == "__main__":
    main()


# version2
# ask user for favourite boba place
# keep tally
# data analysis
# give raw scores
# give socres as a percentage
def chip_rater():
    """help gather data about chp crispness and quality"""


questions = [
    "how crispy is the chip out of 5. 0 is mushy, 5 is super crisp",
    "how woud you rate the taste out of 5 . 0 is buns, 5 is excellent",
    "how fresh would you rate it out of 5. 0 is moldy, 5 is just made",
]
# bucket for ratings
total_ratings = 0
# give the test subject instuctions
print("take one from the bag chip")
print("eat it")
print("give your rating.")

# ask questions to subject
for question in questions:
    print(question)
    # for each question
    # get their rating out of 5
    rating = input().strip(".,?!")
    total_ratings += rating

    # print out the average out of 5
    average = total_ratings / len(questions)
    print(f"Average rating: {average} out of 5")
