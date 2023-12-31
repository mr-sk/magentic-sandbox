from magentic import prompt, StreamedStr
from time import time

commands = ['watch', 'pop', 'screen']

@prompt("Summarize the man page for the following commands: {command}. Limit to 500 words.")
def get_man_summary(command: str) -> StreamedStr:
    ...

start_time = time()
for command in commands:
    summary = str(get_man_summary(command))
    print(f"{time() - start_time:.2f}s : {command} - {len(summary)} chars, {summary[:100]}...")

print('\n\n\n')

start_time = time()
streamed_str =  [get_man_summary(command) for command in commands]
for command, streamed_str in zip(commands, streamed_str):
    summary = str(streamed_str)
    print(f"{time() - start_time:.2f}s : {command} - {len(summary)} chars, {summary[:100]}...")

# Results
#
# 10.25s : watch - 2579 chars, The watch command in UNIX systems continuously runs a command and displays its output in real-time o...
# 20.90s : pop - 2340 chars, The "pop" command is not a specific command in the Unix/Linux system. It could be interpreted as sev...
# 33.51s : screen - 3054 chars, The `screen` command is a full-screen window manager that multiplexes a physical terminal between se...
 


# 10.76s : watch - 2921 chars, The man page for the 'watch' command is a concise document that provides information on how to use t...
# 13.87s : pop - 3353 chars, Command: pop

# The pop command is a system command used for retrieving email messages from a mail ser...
# 13.97s : screen - 2938 chars, The man page for the "screen" command provides comprehensive information about the usage, functional..