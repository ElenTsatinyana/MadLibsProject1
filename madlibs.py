import random

print("Welcome to Mad Libs!")
print("Choose a story template:")
print("1 - Hospital Story")
print("2 - Camping Story")
print("3 - Magic Castle Story")

choice = input("Type 1, 2, or 3: ")

# ---------- TEMPLATE 1 ----------
if choice == "1":
    words = []

    prompts = [
        "Enter a number: ",
        "Enter a measure of time: ",
        "Enter a mode of transportation: ",
        "Enter an adjective: ",
        "Enter another adjective: ",
        "Enter a noun: ",
        "Enter a color: ",
        "Enter a part of the body: ",
        "Enter a verb: ",
        "Enter another number: ",
        "Enter another noun: ",
        "Enter another noun: ",
        "Enter another part of  body: ",
        "Enter a verb: ",
        "Enter another noun: ",
        "Enter an adjective: ",
        "Enter a silly word: "
    ]


    for prompt in prompts:
        words.append(input(prompt))

    story = (
        "It was about " + words[0] + " " + words[1] +
        " ago when I arrived at the hospital in a " + words[2] +
        ". The hospital is a " + words[3] +
        " place, there are a lot of " + words[4] + " " + words[5] +
        " here. There are nurses here who have " + words[6] +
        " " + words[7] + ". If someone wants to come into my room "
        "I told them that they have to " + words[8] +
        " first. I’ve decorated my room with " + words[9] +
        " " + words[10] + ". Today I talked to a doctor and they were "
        "wearing a " + words[11] + " on their " + words[12] +
        ". I heard that all doctors " + words[13] + " " + words[14] +
        " every day for breakfast. The most " + words[15] +
        " thing about being in the hospital is the " + words[16] +
        " " + words[5] + "!"
    )

# ---------- TEMPLATE 2 ----------
elif choice == "2":
    words = []

    prompts = [
        "Enter a person's name: ",
        "Enter a noun: ",
        "Enter a feeling adjective: ",
        "Enter a verb: ",
        "Enter another feeling adjective: ",
        "Enter an animal: ",
        "Enter another verb: ",
        "Enter a color: ",
        "Enter a verb ending in -ing: ",
        "Enter an adverb ending in -ly: ",
        "Enter a number: ",
        "Enter a measure of time: ",
        "Enter a color: ",
        "Enter another animal: ",
        "Enter a number: ",
        "Enter a silly word: ",
        "Enter another noun: "
    ]

    for prompt in prompts:
        words.append(input(prompt))

    story = (
        "This weekend I am going camping with " + words[0] +
        ". I packed my lantern, sleeping bag, and " + words[1] +
        ". I am so " + words[2] + " to " + words[3] +
        " in a tent. I am " + words[4] +
        " we might see a " + words[5] +
        ". While we’re camping, we are going to hike, fish, and " +
        words[6] + ". I have heard that the " + words[7] +
        " lake is great for " + words[8] +
        ". Then we will " + words[9] +
        " hike through the forest for " + words[10] +
        " " + words[11] +
        ". If I see a " + words[12] + " " + words[13] +
        ", I am going to bring it home as a pet! At night we will tell " +
        words[14] + " " + words[15] +
        " stories and roast " + words[16] +
        " around the campfire!!"
    )

# ---------- TEMPLATE 3 ----------
elif choice == "3":
    words = []

    prompts = [
        "Enter a person's name: ",
        "Enter an adjective: ",
        "Enter a color: ",
        "Enter an animal: ",
        "Enter a place: ",
        "Enter an adjective: ",
        "Enter a magical creature (plural): ",
        "Enter another adjective: ",
        "Enter another magical creature (plural): ",
        "Enter a room in a house: ",
        "Enter a noun: ",
        "Enter another noun: ",
        "Enter a plural noun: ",
        "Enter an adjective: ",
        "Enter another plural noun: ",
        "Enter a number: ",
        "Enter a measure of time: ",
        "Enter a verb ending in -ing: ",
        "Enter another adjective: ",
        "Enter another noun: "
    ]

    for prompt in prompts:
        words.append(input(prompt))

    story = (
        "Dear " + words[0] +
        ", I am writing to you from a " + words[1] +
        " castle in an enchanted forest. I found myself here one day "
        "after going for a ride on a " + words[2] + " " + words[3] +
        " in " + words[4] + ". There are " + words[5] + " " +
        words[6] + " and " + words[7] + " " + words[8] +
        " here! In the " + words[9] +
        " there is a pool full of " + words[10] +
        ". I fall asleep each night on a " + words[11] +
        " of " + words[12] +
        " and dream of " + words[13] + " " + words[14] +
        ". It feels as though I have lived here for " + words[15] +
        " " + words[16] +
        ". I hope one day you can visit, although the only way to get "
        "here now is " + words[17] +
        " on a " + words[18] + " " + words[19] + "!"
    )

else:
    print("Invalid choice. Please restart the game.")
    story = ""

# ---------- FINAL OUTPUT ----------
if story != "":
    print("\n--- Your Mad Libs Story ---\n")
    print(story)
