import random

def load_responses(filename):
    with open(filename, 'r') as file:
        responses = file.readlines()
    # Remove any extra whitespace or newlines
    responses = [response.strip() for response in responses]
    return responses

def magic_8_ball(responses):
    while True:
        question = input("Ask a yes/no question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            response = random.choice(responses)
            print(f"Magic 8 Ball says: {response}")

if __name__ == "__main__":
    responses = load_responses('C:/Users/jphaw/Desktop/8ball_responses.txt')
    magic_8_ball(responses)