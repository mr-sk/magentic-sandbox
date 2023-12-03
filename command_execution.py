import os
import stat
from magentic import prompt_chain
from subprocess import getoutput

def validate_command(command: str) -> str:
    length = len(command)
    idx = 0
    command_blocks = []
    while idx < length:
        try:
            start = command.index('```', idx) + 3 # skip backticks
        except ValueError:
            break
        end = command.index('\n```', start)

        next_line = command.index('\n', start) + 1 # skip newline
        candidate = command[next_line:end]
        cleansed_lines = []
        for line in candidate.split('\n'):
            if line.startswith('$ '): # Only for people who enter bash commands with a dollar sign
                cleansed_lines.append(line[2:])
            else:
                cleansed_lines.append(line)
        command_blocks.extend(cleansed_lines)
        idx = end + 4 # move past newline and end backticks

    return command_blocks

def verbal_to_command(verbal):
    return (
       """From this point on, you are a bash shell assistant that outputs bash commands
1. Completions of any prompt must be utilizing shell commands only
2. Place commands in a fenced code block using Markdown and three backticks
2. Often, these shell commands will need to get piped | together to accomplish a task
3. Please be considerate of the operating system over which these commands are operating (Ubuntu Linux 22.04)
5. Use the bash comment character to comment any lines of exposition within a fenced code block
6. Complete the users tasks in accordance to their prompt

User prompt:
List the contents of the current working directory in long format
Completion:
To list the contents of the current working directory in long format, we will run the following command
```
ls -l
```

User prompt:
Get the number of lines in test.py
Completion:
To get the number of lines, we will run the `wc` command with the `-l` option.
```
wc -l test.py
```

User prompt:
{verbal}
Completion:
"""
       )


@prompt_chain(
    "{verbal}?",
    functions=[verbal_to_command],
)
def commandify_verbal(verbal: str) -> str:
    ...


output = commandify_verbal("Touch a file called test.txt and echo 'hello llm' into it.")
print(f"{output}")

clean_commands = validate_command(output)
print(f"Clean command: {clean_commands}")

for command in clean_commands:
    stdout = getoutput(command)
    print(f"stdout: {stdout}")

# Assert things are correct
assert "test.txt" in getoutput("ls")
assert "hello llm" in getoutput("cat test.txt")

st = os.stat("test.txt")
oct_perm = oct(st.st_mode)
assert "0664" in oct_perm[-4:]
