"""
The resume module provides a resume (shocking!) for interested parties.
"""
import json
import collections

try:
    import secret_ingredient
    from shifu import WuxiFingerHold
except ImportError:
    message = ("WARNING: You don't have the necessary libraries installed to "
               "defeat Tai Lung!")
    print("\n", "#" * len(message), message, "#" * len(message), sep="\n")


class BigFatPanda:
    """Represents the human Michael Dunn, aka BigFatPanda."""

    contact_information = {
        "cell": "574.213.0726",
        "email": "mike@eikonomega.com",
        "github": "www.github.com/eikonomega",
        "linkedin": "http://www.linkedin.com/in/eikonomega"}

    def __init__(self, insult_or_compliment):
        """
        Instantiate representation and provide an opportunity for
        an initial compliment or insult.
        """
        self.personal_adjective = insult_or_compliment
        print(
            "\nCongrats, you just created your very own {} BigFatPanda "
            "developer action figure.".format(insult_or_compliment))

    def summary(self):
        """
        Provide the traditional 'summary' section of a resume.
        """

        introduction = (
            "My real name is Michael Dunn, though I generally go by "
            "BigFatPanda (BFP or Panda for short). \n\n"
            "I'm an experienced Python programmer and instructor (though my "
            "experiences seem to keep teaching me about how much more there "
            "is to know). \n\n"
            "I've responded to your request because I feel like it's time to "
            "start a new chapter in my life and career. \n\n"
            "As far as work is concerned, I want to create beautiful code, "
            "work for company whose primary goal is producing software, "
            "help others to grow, and contribute to the open-source community "
            "and the people around me.")

        day_job = (
            "\nI currently work on the Identity & Access Management team "
            "(aka Team Awesome!) at the University of Notre Dame as the "
            "lead Python developer.  In this role I've had many opportunities "
            "to expand my programming knowledge, apply it and share "
            "it with others.")

        message = ("INTRO TO BIG FAT PANDA")
        print("\n", "#" * len(message), message, "#" * len(message), sep="\n")

        print(introduction, day_job, sep="\n")

    def work_history(self):
        """Provide the traditional 'work history' section."""

        notre_dame = collections.OrderedDict()
        notre_dame["Systems Engineer Professional"] = {
            "timeframe": "Summer 2013 - Current",
            "highlights": [
                "1. Recruited by team due to work with Python/Vagrant.",

                "2. Quickly established myself as an coaching resource "
                "for others on the team for coding strategies and "
                "questions.",

                "3. Introduced the use of Git, Circus, and Ansible "
                "to the team and shepherded there use into our "
                "standard practices.",

                "4. Served as a member of PyCon 2014 program committee.",

                "5. Contributed to a number of popular open-source "
                "projects including Circus, Nose, Djangobook.",

                "6. Developed and taught a semester-long course "
                "in Python for IT professionals with no previous "
                "experience. I love feedback: https://github.com/"
                "bigfatpanda-training/pandas-practical-python-primer",

                "7. Gained significant experience with AWS."
            ]
        }

        notre_dame["Application Development Professional"] = {
            "timeframe": "Late Summer 2011 - Summer 2013",
            "highlights": [
                "1. Introduced OO programming to database programs.",

                "2. Created a jUnit-like TDD framework for PL/SQL.",

                "3. Obtained project management certification.",

                "4. Created a framework for reorganizing our disaster "
                "of a SVN repo.",

                "5. Served as the primary developer on multiple projects.",

                "6. Created Python utility programs to handle common "
                "file management and file transfer tasks within "
                "many of our processes which eliminated the need "
                "for programmers to role their own functions. "
                "Codebase -> smaller, Productivity -> up.",

                "7. Started the Common Code Repository, which provided "
                "a single location for commonly used database "
                "functions to reduce code duplication."
            ]
        }

        independent = {
            "The Doula Exchange": {
                "timeframe": "November 2012 - December 2014",
                "highlights": [
                    "1. Wasn't getting enough Python/fun development stuff "
                    "during the day, so I decided to start my own "
                    "company in my off-time.",

                    "2. Created the Doula Exchange to help prospective "
                    "parents find caring Doulas near them.",

                    "3. Did everything. Code, design, advertising, "
                    "customer service, etc.",

                    "4. Signed up over 300 doulas before shutting down."
                ]
            }
        }

        concordia_university_irvine = {
            "Director of Enrollment Management Information Systems": {
                "timeframe": "October 2010 - August 2011",
                "highlights": [
                    "1. Primary administrator for two CRM systems.",
                    "2. PHP/Oracle/MySQL Development."
                ]
            },

            "Director of Student Retention Data Systems": {
                "timeframe": "April 2009 - October 2010",
                "highlights": [
                    "1. Led the rollout of student retention CRM system.",

                    "2. Developed a enrollment projection "
                    "system which tracked historical retention rates "
                    "for various student cohorts and projected "
                    "future program enrollments with such a high "
                    "degree of accuracy that it replaced the "
                    "University's former financial model.",

                    "3. Developed predictive models that identified "
                    "individual students within the freshmen class "
                    "which were at high risk for attrition."
                ]
            },

            "Director of Housing Services": {
                "timeframe": "August 2007 - June 2009",
                "highlights": [
                    "1. Developed a custom Housing Services application "
                    "which interfaced with the university's Banner "
                    "ERP system. The application brought automation "
                    "to a variety of operations that had previously "
                    "been done manually (communications, billing, "
                    "housing assignments, etc) and allowed for "
                    "data-driven decision making regarding future "
                    "housing scenarios.",

                    "2. Handled all administrative functions for on-campus "
                    "housing operations that served more than 1000 "
                    "undergraduate students.",

                    "3. Managed a significant budget(100k+)"
                ]
            },

            "Assistant Director of Residential Education": {
                "timeframe": "August 2006 - July 2007",
                "highlights": [
                    "During the academic year, I experienced supervision "
                    "trial by fire overseeing 16 part-time college students. "
                    "I didn't do well. In fact, they hated me. I realized "
                    "that I had a LOT to learn about managing people.",

                    "During the summer, when classes we're not in session, "
                    "the university hosted conferences and I managed the "
                    "housing portion of this - which was basically "
                    "like managing a hotel.",

                    "This time, I supervised 12 full-time student employees and"
                    "I had learned my lessons about management. The team and "
                    "worked out hearts out that there doing some pretty heroic "
                    "things in what was the biggest conference season ever "
                    "for the university."
                ]
            }
        }

        biola_university = {
            "Web Designer/Developer": {
                "timeframe": "December 2001 - May 2004",
                "highlights": [
                    "This was my first 'real job' in the industry. Here I "
                    "cut my teeth on web design and application development.",
                    "1. As a student, was responsible for the design of much "
                    "of www.biola.edu, including the homepage.",
                    "2. Wrote applications in Macromedia Flash! "
                    "(yea flashback!)"
                ]
            }
        }

        print("\n", "#" * 30, "Notre Dame", "#" * 30,
              json.dumps(notre_dame, indent=2), sep="\n")

        print("\n", "#" * 30, "Independent", "#" * 30,
              json.dumps(independent, indent=2), sep="\n")

        print("\n", "#" * 30, "Concordia University", "#" * 30,
              json.dumps(concordia_university_irvine, indent=2), sep="\n")

        print("\n", "#" * 30, "Biola University", "#" * 30,
              json.dumps(biola_university, indent=2), sep="\n")


# If you're not a coder.  Don't worry about this part.
# It just runs the program. :)
if __name__ == "__main__":
    adjective = input(
        "\nHow would you describe a panda? ")

    bfp = BigFatPanda(adjective)

    cycle = True
    while cycle:
        str_choice = input(
            "\nWhat do you want to do?\n"
            "1: BigFatPanda Summary\n"
            "2: Work History\n"
            "3: Quit\n")

        try:
            choice = int(str_choice)
        except ValueError:
            print("\nThat's not a valid choice.  1, 2, or 3 please.")
            continue
        else:
            if choice not in [1, 2, 3] or choice is None:
                print("\nThat's not a valid choice.  1, 2, or 3 please.")
                continue

        if choice == 1:
            bfp.summary()
        elif choice == 2:
            bfp.work_history()
        elif choice == 3:
            cycle = False
