from magentic import prompt

@prompt('Add more elite hacker to: {phrase} but keep it to one sentence')
def hackerize(phrase: str) -> str:
    ...

print(hackerize("Hello World!"))


