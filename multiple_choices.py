class Question:
    def __init__(self, prompt, answer):
        self.prompt= prompt
        self.answer= answer

questions_prompts = [
    "1+1=?\n(a) 2\n(b) 3\n(c) 4\n(d) 5\n",
    "2+2=?\n(a) 2\n(b) 3\n(c) 4\n(d) 5\n",
]

question_list = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
]

print("Choose the best answer:\n")
def run_test(question_list):
    score = 0
    for question in question_list :
        ans = input(question.prompt + "a/b/c/d? ")
        if ans.lower() == question.answer:
            print("Correct")
            score += 1
        else:
            print("Wrong")
    print("You got " + str(score) + " out of " + str(len(question_list))+ " questions right.")

run_test(question_list)