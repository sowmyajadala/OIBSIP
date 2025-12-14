import pyttsx3
import wikipedia

assistant = pyttsx3.init()

SearchBar = input("search here:")

SearchResult = wikipedia.summary(SearchBar,sentences = 2)
print(SearchResult)

assistant.say(SearchResult)

assistant.runAndWait()