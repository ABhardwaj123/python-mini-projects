#emoji enhancer

sentence = input("enter sentence: ")

words = sentence.split()

new_sentence = ""

emoji_mapper = {
    "love": "❤️",
    "happy": "😀",
    "code": "💻",
    "tea": "☕",
    "music": "🎶",
    "food": "🍕",
    "friends" : "👨👩"
}


for word in words:

    cleaned_word = word.lower().strip(".,?!@#")
    
    emoji = emoji_mapper.get(cleaned_word , "")

    if emoji:
        new_sentence += word + emoji + " "
    else:
        new_sentence += word + " "



print(new_sentence)