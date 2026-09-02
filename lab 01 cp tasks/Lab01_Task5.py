knowledge_base = {
    "python": "Python is used in AI Lab.",
    "grading": "Grading is based on lab work.",
    "project": "Project is about AI.",
    "attendance": "Attendance is important."
}

def match_rule(question, knowledge_base):
    for word in knowledge_base:
        if word in question.lower():
            return knowledge_base[word]
    return None

def session_report(*questions, **stats):
    print("\nSession Report")
    
    for q in questions:
        print(q)
    
    print("Matched:", stats["matched"])
    print("Unmatched:", stats["unmatched"])


name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name)
print("Welcome to AI Lab")

questions = []
matched = 0
unmatched = 0

while True:
    question = input("\nAsk a question or type exit: ")

    if question.lower() == "exit":
        break

    questions.append(question)
    answer = match_rule(question, knowledge_base)
    
    if answer:
        print(answer)
        matched = matched + 1
    else:
        print("Sorry, I don't know.")
        unmatched = unmatched + 1
session_report(*questions, matched=matched, unmatched=unmatched)