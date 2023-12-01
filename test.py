from magentic import prompt

@prompt('Add more elite hacker to: {phrase} but keep it to one sentences')
def hackerize(phrase: str) -> str:
    ...

print(hackerize("Hello World!"))

