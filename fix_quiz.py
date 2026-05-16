#!/usr/bin/env python3
"""Fix quiz data: remove duplicate A/B/C/D prefixes + convert all questions/options to English"""
import json

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse the data - the file is a JS file with "const LESSONS = [...]"
# Extract the JSON array
start = content.find('[')
end = content.rfind(']') + 1
lessons = json.loads(content[start:end])

# Lesson 1: "Tom Gets Up" - Remove A./B./C./D. prefixes from options, convert to English
lessons[0]['questions'] = [
    {
        "question": "What does Tom do first in the morning?",
        "options": ["Get up", "Open his eyes", "Eat bread", "Go to school"],
        "answer": "Open his eyes"
    },
    {
        "question": "What does Tom eat and drink for breakfast?",
        "options": ["Rice", "Bread and milk", "Eggs", "Fruit"],
        "answer": "Bread and milk"
    },
    {
        "question": "How does Tom go to school?",
        "options": ["Take a car", "Ride a bike", "Walk", "Take a bus"],
        "answer": "Walk"
    },
    {
        "question": "Who does Tom see at school?",
        "options": ["Teacher", "His friend Ann", "His mom", "Classmates"],
        "answer": "His friend Ann"
    },
    {
        "question": "How does Tom feel about school?",
        "options": ["Doesn't like it", "Very happy", "Very tired", "Very bored"],
        "answer": "Very happy"
    }
]

# Lesson 2: "At the Park" - Questions only (options already English)
lessons[1]['questions'] = [
    {
        "question": "Where does Tom go?",
        "options": ["Park", "School", "Home", "Lake"],
        "answer": "Park"
    },
    {
        "question": "What does Tom see at the park?",
        "options": ["A cat", "A dog", "A car", "A book"],
        "answer": "A dog"
    },
    {
        "question": "What does the dog do?",
        "options": ["It played with Tom", "It ran fast", "It ate food", "It slept"],
        "answer": "It ran fast"
    },
    {
        "question": "Why is Tom happy at the end?",
        "options": ["He played with the dog", "He saw a bird drink water", "He went home", "He ate food"],
        "answer": "He saw a bird drink water"
    },
    {
        "question": "What kind of time does Tom think this is?",
        "options": ["Bad time", "Good time", "Long time", "Short time"],
        "answer": "Good time"
    }
]

# Lesson 3: "A New Friend" - Questions only (options already English)
lessons[2]['questions'] = [
    {
        "question": "Where is Tom?",
        "options": ["At school", "At the park", "At home", "At the store"],
        "answer": "At the park"
    },
    {
        "question": "Who does Tom see?",
        "options": ["A new girl", "A new boy", "An old man", "A dog"],
        "answer": "A new boy"
    },
    {
        "question": "What is the new boy's name?",
        "options": ["Tom", "Max", "Ben", "Kim"],
        "answer": "Ben"
    },
    {
        "question": "What do they do together?",
        "options": ["Played a game", "Read a book", "Watched TV", "Ate lunch"],
        "answer": "Played a game"
    },
    {
        "question": "How does Tom feel at the end?",
        "options": ["Sad", "Angry", "Happy", "Tired"],
        "answer": "Happy"
    }
]

# Lesson 4: "Helping Mom" - Both questions and options are Chinese -> English
lessons[3]['questions'] = [
    {
        "question": "Where does Tom go after school?",
        "options": ["School", "Friend's house", "Home", "Store"],
        "answer": "Home"
    },
    {
        "question": "How does mom look?",
        "options": ["Happy", "Tired", "Angry", "Sad"],
        "answer": "Tired"
    },
    {
        "question": "What does Tom do to help his mom?",
        "options": ["Cook food", "Clean the table and put food away", "Wash clothes", "Sweep the floor"],
        "answer": "Clean the table and put food away"
    },
    {
        "question": "What does mom say to Tom?",
        "options": ["You are a good boy", "Go play", "Don't bother me", "Go do homework"],
        "answer": "You are a good boy"
    },
    {
        "question": "How does Tom feel?",
        "options": ["Tired", "Hungry", "Happy", "Sleepy"],
        "answer": "Happy"
    }
]

# Lesson 5: "A Rainy Day" - Questions only (options already English)
lessons[4]['questions'] = [
    {
        "question": "Why can't Tom go outside?",
        "options": ["He is tired.", "The rain is too strong.", "He likes to stay home.", "He has no shoes."],
        "answer": "The rain is too strong."
    },
    {
        "question": "What does Tom do at home?",
        "options": ["He watched TV.", "He read a book.", "He played with a toy.", "He cooked food."],
        "answer": "He read a book."
    },
    {
        "question": "Where does Tom go at the end of the story?",
        "options": ["He went to school.", "He went outside.", "He went to bed.", "He went to the park."],
        "answer": "He went to bed."
    },
    {
        "question": "How does Tom feel about this day?",
        "options": ["It is bad.", "It is nice inside.", "It is boring.", "It is too long."],
        "answer": "It is nice inside."
    }
]

# Re-serialize
new_json = json.dumps(lessons, indent=2, ensure_ascii=False)

# Replace the old array with the new one
new_content = content[:start] + new_json + content[end:]

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ data.js updated successfully!")

# Verify
print(f"\nLesson 1, Q1: {lessons[0]['questions'][0]['question']}")
print(f"  Options: {lessons[0]['questions'][0]['options']}")
print(f"  Answer matches option 1: {lessons[0]['questions'][0]['options'][1] == lessons[0]['questions'][0]['answer']}")

print(f"\nLesson 4, Q3: {lessons[3]['questions'][2]['question']}")
print(f"  Options: {lessons[3]['questions'][2]['options']}")
print(f"  Answer matches: {lessons[3]['questions'][2]['options'][1] == lessons[3]['questions'][2]['answer']}")

# Verify all answers match an option
for i, lesson in enumerate(lessons):
    for j, q in enumerate(lesson['questions']):
        if q['answer'] not in q['options']:
            print(f"⚠️  Lesson {i+1}, Q{j+1}: Answer '{q['answer']}' not in options!")
        else:
            # Find correct index
            idx = q['options'].index(q['answer'])
            print(f"✓ Lesson {i+1}, Q{j+1}: answer at index {idx}")
