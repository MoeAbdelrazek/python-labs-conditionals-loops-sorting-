# Python Labs: Conditionals, Loops, and Sorting with Error Handling
# Author: Mohamed Abdelrazek
# Description:
#   This script contains three activities that demonstrate:
#   1. Using conditional statements for discount logic.
#   2. Categorizing customer ratings with loops.
#   3. Sorting test scores and handling errors gracefully.


# Activity 1: Making Decisions with Conditional Statements


def send_discount(books_purchased, discount_threshold, bonus_threshold=None):
    # Decide which discount message to send to a customer
    if bonus_threshold is not None and books_purchased >= bonus_threshold:
        print("Big discount applied!")
    elif books_purchased >= discount_threshold:
        print("Discount applied!")
    else:
        print("No discount.")

# Activity 2: Using Loops for Repetitive Tasks

def categorize_ratings(rating_list):
    # Categorize customer ratings into Low, Medium, and High
    low = 0
    medium = 0
    high = 0

    for rating in rating_list:
        if 1 <= rating <= 4:
            low += 1
        elif 5 <= rating <= 7:
            medium += 1
        elif 8 <= rating <= 10:
            high += 1

    print(f"Low: {low}")
    print(f"Medium: {medium}")
    print(f"High: {high}")

# Activity 3: Sorting Test Scores with Error Handling


# Step 1: Create the list of students
students = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]

# Step 2: Create dictionary of test scores
test_performance = {
    "John": 87,
    "Lisa": 90,
    "Mary": 75,
    "Chris": 100,
    "Linda": 100,
    "Matt": 70
}

# Step 3: Extract scores into a list
scores = []
for student in students:
    scores.append(test_performance[student])

def bubble_sort(score_list):
    # Sort a list of scores in ascending order using Bubble Sort
    n = len(score_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if score_list[j] > score_list[j + 1]:
                # Swap if the element is greater than the next
                score_list[j], score_list[j + 1] = score_list[j + 1], score_list[j]
    return score_list

# Step 4: Sort the scores
sorted_scores = bubble_sort(scores)

# Step 5: Highest and Lowest Scores
highest_score = sorted_scores[-1]
lowest_score = sorted_scores[0]

def average_class_score(students, scores):
    # Calculate the average class score with error handling
    try:
        if len(students) == 0 or len(scores) == 0:
            raise ValueError("No students in class.")
        return sum(scores) / len(scores)
    except ValueError as e:
        print(e)
        return None

# Step 6: Calculate average score
average_score = average_class_score(students, sorted_scores)

# Main Execution (for testing/demo purposes)

if __name__ == "__main__":
    # Activity 1 Tests
    print("=== Activity 1: Discounts ===")
    send_discount(3, 5)           # No discount.
    send_discount(7, 5)           # Discount applied!
    send_discount(12, 5, 10)      # Big discount applied!

    # Activity 2 Tests
    print("\n=== Activity 2: Ratings ===")
    categorize_ratings([1, 3, 5, 7, 8, 9])  # Low:2, Medium:2, High:2

    # Activity 3 Tests
    print("\n=== Activity 3: Test Scores ===")
    print("Sorted Scores:", sorted_scores)
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Average Score: {average_score}")

    # Test empty class handling
    empty_class = []
    empty_scores = []
    error_average = average_class_score(empty_class, empty_scores)
    print("Empty class average:", error_average)