class Question:
    def __init__(self, text, answer):
        print("\nNew function")
        self.text = text
        self.answer = answer


new_question = Question("texti1", "pergjigjia1")
print(new_question.text)
print(new_question.answer)

new_question2 = Question("texti2", "pergjigjia2")
print(new_question2.text)
print(new_question2.answer)