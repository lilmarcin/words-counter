import easyocr

def count_words_and_characters(text_list):
    word_counter = 0
    character_counter = 0

    for text in text_list:
        split_text = text.split()
        word_counter += len(split_text)
        character_counter += len(text)

    return word_counter, character_counter

# reader = easyocr.Reader(['pl'])
# result = reader.readtext('images/example2.jpg', detail=0)
# print(result)

# word_counter, character_counter = count_words_and_characters(result)
# print("Words:", word_counter)
# print("Characters:", character_counter)
