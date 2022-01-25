"""
CP1404/CP5632 Practical
Wikipedia API & Python Library
"""
import wikipedia


def main():
    """
    Program that takes the Search term or page title from user and displays the title, summary and URL
    when searching for that keyword on the wiki.
    """
    search_phrase = input("Search phrase or page title: ").strip()
    while search_phrase != "":
        try:
            summary = wikipedia.summary("search_phrase")
            print("Summary: {}".format(summary))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)

        page = wikipedia.page(search_phrase)
        print("Title: {}".format(page.title))
        print("Url: {}".format(page.url))
        print()
        search_phrase = input("Search phrase or page title: ").strip()


main()
