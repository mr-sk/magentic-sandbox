Examples on how to use this project, which is leveraging Magentic to provide decorator that utilize openAI API's ChatGPT.

To setup:

    git clone git@github.com:mr-sk/magentic.git
    cd magentic
    python3 -m venv venv
    source venv/bin/activate

    // add your open AI key to the environment
    emacs ~/.bashrc
    export OPENAI_API_KEY=”<yourkey>”
    source ~/.bashrc

To Run:

    // Easy
    python3 command_execution

`ls` the directory and rm the test.txt as needed. 


Todo
* [ ] Have the commands execute in subdirectory on the local fs

* [ ] Where the assertions are executed, could instead have the llm generate the asserts to validate the command and then we (in some environment) assert them. Additionally, then feed the error back into the llm and prompt it to fix. 

* [*FIXED*] In `command_execution.py` when it attemps to execute the command, it just "creates directories" for each "command" it is suppose to be executing. The split() command ([list]) looks correct, but the subprocess.check_output(command) totally bombs. Need to fix this.

Summary

* Really just messin around with Magentic, there's a few examples of calling the LLM as a decorator. It's a cool concept.
