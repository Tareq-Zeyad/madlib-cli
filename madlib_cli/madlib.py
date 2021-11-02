
import re

text = "assets/sample-text.txt"


def read_text(path):
    """
    Reading the file from assets folder and returns the text. 
   """
    try:
        file = open(path)
        lines = file.readlines()
        file.close()
        finalString = f"{lines[0]}{lines[2]}{lines[4]}"
        return finalString

    except FileNotFoundError as err:
        print(f"file not found: {err}")


def parse_text(textString):
    """
    Remove words inside of brackets and replace them with incremented numbers, which returns strings.
    """
    regex = '\{.*?\}'
    strippedString = re.sub(regex, "{}", textString)
    return strippedString


def merge_text(parsedText, userInput):
    _string = f"{str(parsedText)}"
    formatedString = _string.format(*userInput)
    return formatedString


def begin_game(_text):
    gameText = read_text(_text)
    print(f"""
    Hello, User!
    Lets play a game, its called madlib, you have to fill in 20 words in order to complete the story, here is the example:
    {gameText}
    now, go ahead and start guessing!
    your result will be viewed at the end :D
    """)
    listOfAnswers = []
    for i in range(21):
        listOfAnswers.append(input(f"Enter Word {i}:"))

    print("your full response:")
    result = merge_text(parse_text(gameText), listOfAnswers)
    print(result)

    print("saving your response.......")
    newSave = open("./assets/playerSave.txt", 'w')
    newSave.write(
        result + "\n \n THIS FILE WAS GENERATED AUTOMATICALLY!!!!!!!!")
    newSave.close()
    print("Done!")


begin_game(text)
