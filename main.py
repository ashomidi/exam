class Exam():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


question_prompts = [
    "Which country has won the most FIFA World Cup titles in football (soccer)?\n(a) Brazil\n(b) Germany\n(c) Italy\n",
    "Who holds the record for the most Olympic gold medals in swimming?\n(a) Michael Phelps\n(b) Mark Spitz\n(c) Ian Thorpe\n",
    "Which tennis player has the most Grand Slam singles titles in history?\n(a) Roger Federer\n(b) Rafael Nadal\n(c) Novak Djokovic\n",
    "In which year did Usain Bolt set the world record for the men's 100 meters sprint?\n(a) 2008\n(b) 2009\n(c) 2012\n",
    "Who is considered the greatest basketball player of all time?\n(a) Michael Jordan\n(b) LeBron James\n(c) Kobe Bryant\n"
]

questions = [
    Exam(question_prompts[0], "a"),
    Exam(question_prompts[1], "a"),
    Exam(question_prompts[2], "a"),
    Exam(question_prompts[3], "b"),
    Exam(question_prompts[4], "a")
]

def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['a', 'b', 'c']:
            return user_input
        else:
            print("Invalid input. Please enter 'a', 'b', or 'c'.")

def run_test(prompts):
    score = 0
    for question in prompts:
        answer = get_user_input(question.question)
        if answer == question.answer.lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print("Your score: {}/{}".format(score, len(question_prompts)))

run_test(questions)

