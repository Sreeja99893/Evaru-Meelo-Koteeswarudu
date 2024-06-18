# display the instruction for Meelo Evaru Koteeswarudu.
# arrange the questions in list.
# give the amount accoding to correct answers

# Quiz questions
questions = [
    {
        "question": "Starting from the earliest hours of the day, arrange these everyday greetings in correct order?",
        "options": ["A. Good Morning", "B. Good Evening", "C. Good Night", "D. Good Afternoon"],
        "answer": ["A", "D", "B", "C"],
        "type": "multiple"
    },
    {
        "question": "Arrange these land measurements in decreasing order?",
        "options": ["A. Acre", "B. Cent", "C. Hectare", "D. Yard"],
        "answer": ["C", "A", "B", "D"],
        "type": "multiple"
    },
    {
        "question": "Starting from the biggest, arrange the following birds in normal size",
        "options": ["A. Pichuka", "B. Rabandhu", "C. Nippukodi", "D. Pigeon"],
        "answer": ["C", "B", "D", "A"],
        "type": "multiple"
    },
    {
        "question": "How would you consult to know your horoscope?",
        "options": ["A. Astrologer", "B. Astronomist", "C. Economist", "D. Agronomist"],
        "answer": ["A"],
        "type": "single"
    },
    {
        "question": "In Internet slang, 'LOL' and 'ROFL' are used to express?",
        "options": ["A. Sadness", "B. Laughter", "C. Anger", "D. Confusion"],
        "answer": ["B"],
        "type": "single"
    },
    {
        "question": "Which of these is not a correct equation?",
        "options": ["A. 1m = 100 cm", "B. 1ft = 12 inches", "C. 1L = 1000ml", "D. 1kg = 100g"],
        "answer": ["D"],
        "type": "single"
    },
    {
        "question": "As per Hindu mythology, who is the wife of King Nala?",
        "options": ["A. Lopamudra", "B. Mandodari", "C. Menaka", "D. Damayanti"],
        "answer": ["D"],
        "type": "single"
    },
    {
        "question": "Which is the 4th planet from the sun in our solar system?",
        "options": ["A. Mercury", "B. Mars", "C. Jupiter", "D. Earth"],
        "answer": ["B"],
        "type": "single"
    },
    {
        "question": "In which of the following cities is Jallianwala Bagh located?",
        "options": ["A. Ludhiana", "B. Bathinda", "C. Jalandhar", "D. Amritsar"],
        "answer": ["D"],
        "type": "single"
    },
    {
        "question": "As of June 2014, who among the following is the highest wicket-taker in Test cricket for India?",
        "options": ["A. Harbhajan Singh", "B. Anil Kumble", "C. Kapil Dev", "D. Zaheer Khan"],
        "answer": ["B"],
        "type": "single"
    },
    {
        "question": "The ISRO Space Center in Sriharikota is named after which of these scientists?",
        "options": ["A. Abdul Kalam", "B. Vikram Sarabhai", "C. Homi J. Bhabha", "D. Satish Dhawan"],
        "answer": ["D"],
        "type": "single"
    },
    {
        "question": "The Parliament of Great Britain is housed in which of these buildings?",
        "options": ["A. Palace of Westminster", "B. The Tower of London", "C. Buckingham Palace", "D. Old Bailey"],
        "answer": ["A"],
        "type": "single"
    },
    {
        "question": "Arrange the following words in order to form the first line of a Telugu film song?",
        "options": ["A. Ledoye", "B. Kudi", "C. Ademayithe", "D. Porapatu"],
        "answer": ["B", "C", "D", "A"],
        "type": "multiple"
    },
    {
        "question": "Arrange these tithis in order of their occurrence in the fortnight?",
        "options": ["A. Dasami", "B. Navami", "C. Saptami", "D. Ashtami"],
        "answer": ["C", "D", "B", "A"],
        "type": "multiple"
    },
    {
        "question": "Arrange the following places from north to south",
        "options": ["A. Srisailam", "B. Hanumakonda", "C. Tirupati", "D. Basara"],
        "answer": ["D", "B", "C", "A"],
        "type": "multiple"
    },
]

# Prize structure
prizes = [
    {"question_number": 1, "value": 1000, "amount_lost": 0},
    {"question_number": 2, "value": 2000, "amount_lost": 0},
    {"question_number": 3, "value": 3000, "amount_lost": 0},
    {"question_number": 4, "value": 5000, "amount_lost": 0},
    {"question_number": 5, "value": 10000, "amount_lost": 0},
    {"question_number": 6, "value": 20000, "amount_lost": 10000},
    {"question_number": 7, "value": 40000, "amount_lost": 10000},
    {"question_number": 8, "value": 80000, "amount_lost": 10000},
    {"question_number": 9, "value": 160000, "amount_lost": 10000},
    {"question_number": 10, "value": 320000, "amount_lost": 10000},
    {"question_number": 11, "value": 640000, "amount_lost": 320000},
    {"question_number": 12, "value": 1250000, "amount_lost": 320000},
    {"question_number": 13, "value": 2500000, "amount_lost": 320000},
    {"question_number": 14, "value": 5000000, "amount_lost": 320000},
    {"question_number": 15, "value": 10000000, "amount_lost": 320000},
]


# Function to ask questions and check answers
def ask_question(question_data, question_number):
    print(f"\nQuestion {question_number}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)

    if question_data["type"] == "single":
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer in question_data["answer"]:
            print("Correct! Moving to the next question.\n")
            return True
        else:
            print(f"Incorrect. The correct answer is: {', '.join(question_data['answer'])}\n")
            return False

    elif question_data["type"] == "multiple":
        user_input = input("Enter your answers in order separated by commas (e.g., A,C,D,B): ").strip().upper()
        user_answers = [ans.strip() for ans in user_input.split(",")]

        if user_answers == question_data["answer"]:
            print("Correct! Moving to the next question.\n")
            return True
        else:
            print(f"Incorrect. The correct answers are: {', '.join(question_data['answer'])}\n")
            return False


# Main quiz loop
def run_quiz():
    question_number = 0
    while question_number < len(questions):
        if ask_question(questions[question_number], question_number + 1):
            question_number += 1
        else:
            break

    if question_number == 0:
        prize_money = 0
    elif question_number == 5:
        prize_money = 0
    elif question_number == 6:
        prize_money = 10,000
    elif question_number == 10:
        prize_money = 10,000
    elif question_number == 11:
        prize_money = 3,60,000
    elif question_number == 15:
        prize_money = 3,60,000
    else:
        prize_money = prizes[question_number - 1]["amount_lost"]

    print(f"\nYou answered {question_number} questions correctly.")
    print(f"You have won: ₹{prize_money}/-")
    print("Thanks for playing Quiz..!👏🏼 ")
    print("Thanks For Coming Evaru Meelo Koteeswarudu..✨")


# Start the quiz
run_quiz()
