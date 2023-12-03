import argparse
import os
import stat
from magentic import prompt_chain
from pathlib2 import Path
from subprocess import getoutput

def generate_assertions(verbal: str) -> str:
    gpt_prompt = """From this point on, you are a bash shell assistant that outputs python commands
1. Completions of any prompt must be utilizing python & shell commands only in an assert() statement
2. Place commands in a fenced code block using Markdown and three backticks
2. Often, these shell commands will need to get piped | together to accomplish a task
3. Please be considerate of the operating system over which these commands are operating (Ubuntu Linux 22.04)
5. Use the bash comment character to comment any lines of exposition within a fenced code block
6. Complete the prompt by creating python assertions

User prompt:
echo 'Testing 1,2,3' > github-test.txt
Completion:
```
assert(os.path.exists('github-test.txt'))
assert('Testing 1,2,3' in Path('github-test.txt').read_text())
```

User prompt:
echo 'Testing 1,2,3' > github-test.txt
Completion:
```
assert(os.path.exists('github-test.txt'))
assert('Testing 1,2,3' in Path('github-test.txt').read_text())
```

User prompt:
{verbal}
Completion:
"""

def generate_code_execution_prompt(verbal: str) -> str:
    return """From this point on, you are a bash shell assistant that outputs bash commands
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

def run_command(command: str) -> str:
    for command in clean_commands:
        stdout = getoutput(command)
        print(f"stdout: {stdout}")

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

def verbal_to_command(verbal: str) -> str:
    return verbal


@prompt_chain(
    "{verbal}?",
    functions=[verbal_to_command],
)
def commandify_verbal(verbal: str) -> str:
    ...

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GPT Text-to-Command - CLI [sk#innercircle]")
    parser.add_argument("prompts", nargs="+", help="One or more prompts")
    args = parser.parse_args()

    # Get args.prompts into a string
    prompt_string = " ".join(args.prompts)

    complete_prompt_string = generate_code_execution_prompt(prompt_string)
    print(f"Complete Prompt: {complete_prompt_string}")

    gpt_output = commandify_verbal(complete_prompt_string)
    print(f"GPT Output: {gpt_output}")

    clean_commands = validate_command(gpt_output)
    print(f"Clean Command: {clean_commands}")

    run_output = run_command(clean_commands)
    print(f"Run Output for: {run_output}")

    # Validate output
    complete_assertion_string = generate_assertions(clean_commands)
    gtp_assertion_output = commandify_verbal(complete_assertion_string)
    print(f"GPT Output: {gtp_assertion_output}")
