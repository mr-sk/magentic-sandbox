from magentic import prompt_chain
from subprocess import check_output

def validate_command(command: str) -> str:
    return command
    #print(f"Char: {command[0]}")
    #if command[0] == '!':
    #    return command[1:]

    #return False

def verbal_to_command(verbal):
    return (
       """Set parameters for how all interactions with your agent will happen.
        1. Replies to any request must be utilizing shell commands
        2. Often, these shell commands will need to get piped | together to accomplish a task
        3. Please be considerate of the operating system over which these commands are operating (Ubuntu Linux 22.04)
        
        My request will start with !
        
        Your command line response should be just the shell commands to complete the task. 
        
        !{verbal}}"""
       )


@prompt_chain(
    "{verbal}?",
    functions=[verbal_to_command],
)
def commandify_verbal(verbal: str) -> str:
    ...


out = commandify_verbal("Touch a file called test.txt and echo 'hello llm' into it.")
print(f"Raw response {out}")

clean_command = validate_command(out)
print(f"Clean command: {clean_command}")

split_command = clean_command.split()
print(f"Split command: {split_command}")


stdout = check_output(split_command)
print(f"stdout: {stdout.decode()}")