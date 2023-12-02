Examples on how to use this project, which is leveraging Magentic to provide decators that utilize openAI API's ChatGPT. 

To setup:

    git clone git@github.com:mr-sk/magentic.git
    cd magentic
    python3 -m venv venv
    source venv/bin/activate

    // add your open AI key to the environment
    emacs ~/.bashrc
    export OPENAI_API_KEY=”<yourkey>”
    source ~/.bashrc

Todo

* In `command_execution.py` when it attemps to execute the command, it just "creates directories" for each "command" it is suppose to be executing. The split() command ([list]) looks correct, but the subprocess.check_output(command) totally bombs. Need to fix this. 

Summary

* Really just messin around with Magentic, there's a few examples of calling the LLM as a decator. It's a cool concept. 