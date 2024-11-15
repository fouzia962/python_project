# List of questions, options, and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a. Paris", "b. Berlin", "c. Madrid", "d. Rome"],
        "answer": "a"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a. Earth", "b. Mars", "c. Venus", "d. Jupiter"],
        "answer": "b"
    },
    {
        
        "question": "What is 5 + 7?",
        "options": ["a. 10", "b. 11", "c. 12", "d. 13"],
        "answer": "c"
    },
    {
        "question": "Which animal gives both milk and eggs ?",
        "options": ["a. Giraffe", "b. Rabbit", "c. Rat", "d. Platypus"],
        "answer": "d"
    },
    {
        "question": "Which is known as the deepest Ocean?",
        "options": ["a. Atlantic Ocean", "b. Pacific Ocean", "c. Indian Ocean", "d. Arctic Ocean"],
        "answer": "b"
    },
    {
        "question": "What is the world's most populated country?",
        "options": ["a. USA", "b. Russia", "c. China", "d. India"],
        "answer": "d"
    },
    {
        "question": "What is the capital of Russia?",
        "options": ["a. Dhaka", "b. Berlin", "c. Moscow", "d. Mascat"],
        "answer": "c"
    },
    {
        "question": "Which city is known as Pink City?",
        "options": ["a. Jaipur", "b. Udaipur", "c. Jodhpur", "d. Raipur"],
        "answer": "a"
    },
    {
        "question": "What is Full form of RAM?",
        "options": ["a. Rapid acces Memory", "b. Randam acces Memory", "c. Read only Memory", "d. Random acces Memory"],
        "answer": "d"
    },
    {
        "question": "What is the capital of Maharashtra?",
        "options": ["a. Dispur ", "b. Panji", "c. Mumbai", "d. Raipur"],
        "answer": "c"
    },
    {
        "question": "Which planet is known as the Green Planet?",
        "options": ["a. Earth", "b. Mars", "c. Venus", "d. Uranus"],
        "answer": "d"
    },
    {
        "question": "What is 50 + 70?",
        "options": ["a. 100", "b. 115", "c. 120", "d. 137"],
        "answer": "c"
    },
    {
        "question": "Who is known as the Father of Zoology?",
        "options": ["a. Aristotle", "b. Theophrastus", "c. John Doe", "d. Mustan"],
        "answer": "a"
    },
    {
        "question": "Who Wrote 'Romeo and Juliet'?",
        "options": ["a. Charles Dicken", "b. John", "c.Shakespear", "d. Jane Austen"],
        "answer": "c"
    },
    {
        "question": "What is the boling point of water?",
        "options": ["a. 100", "b. 110", "c. 120", "d. 130"],
        "answer": "a"
    }
]

# Function to run the quiz
def run_quiz():
    score = 0
    total_questions = len(questions)

    for question in questions:
        # Display the question and options
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        # Get the user's answer
        answer = input("Please choose an answer (a/b/c/d): ").lower()

        # Check if the answer is correct
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}. \n")

    # Display final score
    print(f"Your final score is {score} out of {total_questions}.")

# Start the quiz
print("Welcome to the Quiz!\n")
name=input("Enter your Name")
print("Hello Dear "+ name+ "\nWish you a good luck for this Quiz. \n")
run_quiz()
