import requests
import json
from bs4 import BeautifulSoup
import sys
import argparse

language_in = ''
language_trans = ''
translation = ''

languages = ['Arabic', 'German', 'English', 'Spanish', 'French',
             'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
             'Romanian', 'Russian', 'Turkish']

# -- A variable used for outputting the translations in output function --
user_chosen_lang = ''


# -- Main input function that grabs the users selection and calls a request function
# for processing and output --
def main_input():
    user_language = int(input("Type the number of your language: " + '\n'))
    user_translate = int(input("Type the number of language you want to translate to or '0' to translate to all "
                               "languages:" + '\n'))
    print("Type the word you want to translate: ")
    word_to_translate = str(input())

    if user_translate == 0 or user_translate == "all":
        translate_all_to_terminal(user_language, user_translate, word_to_translate)
    else:
        global user_chosen_lang
        user_chosen_lang = languages[user_translate - 1]

        request_translation(languages[user_language - 1].lower(), languages[user_translate - 1].lower(),
                            word_to_translate.lower())


# -- Method that requests translation to website, and prints all output to a text file.
def translate_all_to_terminal(user_lang, user_trans, word_to):
    translate_url = ''
    translate_file = open(str(word_to).lower() + ".txt", "a", encoding="utf-8")

    for x in languages:
        if x == languages[user_lang-1]:
            continue
        user_agent = 'Mozilla/5.0'
        translate_url = 'https://context.reverso.net/translation/' + str(languages[user_lang-1].lower()) \
                        + '-' + str(x.lower()) + '/' + \
                        str(word_to)
        #print(translate_url)
        r = requests.get(translate_url, headers={'User-Agent': user_agent})
        if not r:
            if r.status_code == 404:
                print(f"Sorry, unable to find {word_to}")
                sys.exit(1)
            else:
                print("Something wrong with your internet connection")
                sys.exit(1)
        soup = BeautifulSoup(r.content, 'html.parser')
        translated_words = [word.text.strip() for word in soup.select('div#translations-content > a')]
        # print(translated_words[0])
        translated_examples = []
        for example in soup.select('section#examples-content > div[class="example"]'):
            translated_examples.append([sentence.text.strip() for sentence in example.select('span.text')])

        translate_file.write(str(x) + " Translations:" + '\n')
        translate_file.write(str(translated_words[0]) + '\n')
        translate_file.write('\n')
        translate_file.write(str(x) + " Example:" + '\n')
        translate_file.write(str(translated_examples[0][0]) + '\n')
        translate_file.write(str(translated_examples[0][1]) + '\n')
        translate_file.write('\n')

    translate_file.close()
    read_file = open(str(word_to).lower() + ".txt", "r", encoding="utf-8")
    for line in read_file:
        print(line.strip('\n'))
    read_file.close()


# ------ ======== -------- ======== -------- =======


# -- Method that requests the translation to the website, and calls an output function. --
def request_translation(user_lang, user_trans, word_to):
    translate_url = ''
    translate_file = open(str(word_to).lower() + ".txt", 'a', encoding='utf-8')
    user_agent = 'Mozilla/5.0'
    translate_url = 'https://context.reverso.net/translation/' + str(user_lang) + '-' + str(user_trans) + '/' + str(word_to)

    # -- Grab the request from the website and print the status code --
    r = requests.get(translate_url, headers={'User-Agent': user_agent})
    if not r:
        if r.status_code == 404:
            print(f"Sorry, unable to find {word_to}")
            sys.exit(1)
        else:
            print("Something wrong with your internet connection")
            sys.exit(1)


    soup = BeautifulSoup(r.content, 'html.parser')
    translated_words = [word.text.strip() for word in soup.select('div#translations-content > a')]
    translated_examples = []
    for example in soup.select('section#examples-content > div[class="example"]'):
        translated_examples.append([sentence.text.strip() for sentence in example.select('span.text')])

    # --- Write translation words to file ---
    # translate_file.write("Context Examples:" + '\n')
    # translate_file.write('\n')
    translate_file.write(str(user_trans).title() + " Translations:" + '\n')
    num_words = len(translated_words)
    if num_words < 5:
        for i in range(len(translated_words)):
            translate_file.write(translated_words[i] + '\n')
    else:
        for i in range(5):
            translate_file.write(translated_words[i] + '\n')

    # --- Write translation examples to file. ---
    translate_file.write('\n')
    translate_file.write(str(user_trans).title() + " Examples:" + '\n')
    num_examples = len(translated_examples)
    if num_examples < 5:
        for i in range(len(translated_examples)):
            for j in range(len(translated_examples[i])):
                if j == 0:
                    translate_file.write(str(translated_examples[i][j]) + ":" + '\n')
                else:
                    translate_file.write(str(translated_examples[i][j]) + '\n')
            translate_file.write('\n')
    else:
        for i in range(5):
            for j in range(len(translated_examples[i])):
                if j == 0:
                    translate_file.write(translated_examples[i][j] + ":" + '\n')
                else:
                    translate_file.write(translated_examples[i][j] + '\n')

            translate_file.write('\n')
    translate_file.close()

    read_file = open(str(word_to).lower() + ".txt", 'r', encoding='utf-8')
    for lines in read_file:
        print(lines.strip('\n'))

    read_file.close()
    # output_results(translated_words, translated_examples)


def output_results(words, examples):
    print()
    print("Context examples: ")
    print()
    print(user_chosen_lang + " Translations:")

    # print(words)
    num_words = len(words)
    if num_words < 5:
        for i in range(len(words)):
            print(words[i])
    else:
        for i in range(5):
            print(words[i])

    # print(translated_words)
    print()
    print(user_chosen_lang + " Examples:")

    num_examples = len(examples)
    if num_examples < 5:
        for i in range(len(examples)):
            for j in range(len(examples[i])):
                if j == 0:
                    print(examples[i][j] + ":")
                else:
                    print(examples[i][j] + '\n')
    else:
        for i in range(5):
            for j in range(len(examples[i])):
                if j == 0:
                    print(examples[i][j])
                else:
                    print(examples[i][j] + '\n')


# print("""Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:""")

# --== Begin program by calling the main function for user input --==
parser = argparse.ArgumentParser(description="Hello, welcome to the translator: \
Translator supports: ")

args = sys.argv
if len(args) < 4:
    print("You need three fields to fill, your language, language to translate to, and what word you want translated.")
    sys.exit(1)
else:
    if str(args[1]).title() not in languages:
        print(f"Sorry, the program doesn't support {str(args[1]).title()}")
        sys.exit(1)
    elif str(args[2]).title() not in languages and str(args[2]).lower() != "all":
        print(f"Sorry, this program doesn't support {str(args[2]).title()}")
        sys.exit(1)
    else:
        language_in = str(args[1]).lower()
        language_trans = str(args[2]).lower()
        translation = str(args[3]).lower()

if str(args[2] == "all"):
    set_int = 0
    for i in range(len(languages)):
        if languages[i] == language_in.title():
            set_int = i
    # print("set " + str(set_int))
    translate_all_to_terminal(set_int+1, language_trans, translation)
else:
    request_translation(language_in, language_trans, translation)

# print("Hello, welcome to the translator. Translator supports:")
# for x in range(len(languages)):
#     print(str(x + 1) + "." + " " + languages[x])

# main_input()


# print(f'You chose "{user_in}" as a language to translate "{word_to_translate}"')