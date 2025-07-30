import json


def load_quiz_data(file_path):
    
    try:
        with open(file_path, 'r') as file:
            quiz_data = json.load(file)
            return quiz_data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")
        return None
    
def ask_question(question):
    print(question['question'])
    options = ['A', 'B', 'C', 'D']
    for opt in options:
        print(f"{opt}. {question[opt]}")
    
    answer = input("Please select the correct option (A-D): ").strip().upper()
    
    if answer in options:
        return answer == question['answer']
    else:
        print("Invalid input. Please enter a letter between A and D.")
        return False
    
def main():
    quiz_data = load_quiz_data('quiz.json')
    
    if not quiz_data:
        return
    
    score = 0
    total_questions = len(quiz_data)
    
    for question in quiz_data:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")
    
    print(f"Quiz completed! Your score: {score}/{total_questions}")


if __name__ == "__main__":
    main()