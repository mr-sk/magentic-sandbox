from typing import Literal
from magentic import prompt, FunctionCall

def activate_lock(code: int) -> str:
    if code == 1234:
        print('unlocked')
    else:
        print('locked')
    
@prompt('Enter the code to unlock the door - hint for the code is, the first four consecutive integers',
        functions=[activate_lock])
def unlock_door() -> FunctionCall[int]:
    ...

out = unlock_door()
print(out)
out()

