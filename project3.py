EASY_ANSWERS = ["soccer","hands","one","country"]  

MEDIUM_ANSWERS = ["Greg","functional","gymnastics","ten thousand"]

HARD_ANSWERS = ["Jai alai","cesta","goatskin","188"]

LIST_OF_BLANKS = ["__1__","__2__","__3__","__4__"]


EASY_QUESTION = ("\nIn the sport of __1__ you try and score in the oppoents goal using any body part except your __2__. Team are played with eleven players on a side, ten field players and a golie. Each goal is worth __3__ point and the match runs ninety minutes with no timeouts. It is the most popular game in the world and is played and watched in almost every __4__ and is often refered to as the beautiful game.")


MEDIUM_QUESTION = "\nCrossfit is a sport that was created by __1__ Glassman back in 2000 in Carson City California. It is focused on constantly varied, high-intensity, __2__ movement workout style that incorperates olympic Lifting, __3__, body weight, strongman, and others. In the begining there were only 13 boxes and in just nine short year that number has exploded to more than __4__ boxes world wide." 


HARD_QUESTION = "\n__1__ is a sport involving a ball bounced off a walled space by accelerating it to high speeds using a __2__. Balls weigh 125-140g and are covered with __3__ and can reach speeds of __4__ mph. It is played in teams of two and the first team to 7 or 9 wins."
		


def say_hello(hello): #function to take in one input and returns and output to say hello.
  name = raw_input("Hi, what is your name?")
  return hello + name
 

def take_quiz_question(): #function asking if you would like to take the quiz.
  greeting = raw_input("\nWould you like to take a quiz?")
  if greeting == "yes" or greeting == "yes":
    return "Great."
  else:
    print ("\nThat is not a valid choice please try again.")
    return take_quiz_question()


def quiz_difficulty(): #function asking what level of the quiz you would like to take.
  while True:
    difficulty = raw_input("\nPlease select easy, medium, hard:").lower()
    if difficulty in ["easy","medium","hard"]:
      print ("\nGreat, you will have three trys to answer each question")
      return difficulty
    else:
      print ("\nThat is not a valid choice please try again.")
      

  
def read_user_answer(solution): #A fucntion that is a input and outputs wheather you got the queston correct or not.
  for i in range(3):
    answer = raw_input("\nWhat is your guess?")
    if answer == solution:
      print "\nCorrect!\n"
      return answer
  if answer != solution :
    print "\nSorry that is not the correct answer.\n"
    return answer
    
  


def replace_blank(paragraph, blank, answer): #A functon that takes in 3 inputs and outputs the appended version of the paragraph with the blanks in it.
    replaced = []
    paragraph = paragraph.split()
    for word in paragraph:
      replacement = blank
      if replacement != None:
        user_input = answer
        word = word.replace(replacement, user_input)
        replaced.append(word)
      else:
        replaced.append(word)
    replaced = " ".join(replaced)
    return(replaced) 
  
 

def replaced(paragraph, list_of_blanks, list_of_solutions): #A function that takes in three inouts and oututs the paragraphs with the answers filled in.
  for i in range(len(list_of_blanks)):
    print(paragraph)
    answer = read_user_answer(list_of_solutions[i])
    if answer != list_of_solutions[i]:
      print "Game Over"  
      return 
    paragraph = replace_blank(paragraph, list_of_blanks[i], list_of_solutions[i])




print say_hello("Hi, ")
print take_quiz_question()
difficulty = quiz_difficulty()

if difficulty == "easy":
  replaced(EASY_QUESTION, LIST_OF_BLANKS, EASY_ANSWERS)
if difficulty == "medium":
  replaced(MEDIUM_QUESTION, LIST_OF_BLANKS, MEDIUM_ANSWERS)
if difficulty == "hard":
  replaced(HARD_QUESTION, LIST_OF_BLANKS, HARD_ANSWERS)

