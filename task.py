# Happy or Sad Sentence Detector

print("================================")
print("   HAPPY OR SAD DETECTOR")
print("================================")

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Convert the sentence into lowercase
sentence = sentence.lower()

# List of happy and sad words
happy_words = ["happy", "joy", "love", "good", "wonderful",
               "excited", "great", "smile", "awesome"]

sad_words = ["sad", "cry", "bad", "angry", "lonely",
             "upset", "hurt", "terrible", "unhappy"]

# Count happy and sad words
happy_count = 0
sad_count = 0

words = sentence.split()

for word in words:
    word = word.strip(".,!?;:")

    if word in happy_words:
        happy_count += 1

    elif word in sad_words:
        sad_count += 1

# Display the result
print("\n========== RESULT ==========")

if happy_count > sad_count:
    print("Happy Sentence 😊")

elif sad_count > happy_count:
    print("Sad Sentence 😢")

else:
    print("Neutral Sentence 😐")

print("============================")
