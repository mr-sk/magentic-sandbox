This sandbox leverages magentic (https://github.com/jackmpcollins/magentic) which provides openAI chatgpt based interaction
via @prompt decorators. 

The prompt used is provided here: https://github.com/mr-sk/magentic-sandbox/blob/main/command_execution.py#L38

The point is to take natural language commands and turn into commands the script can execute. 

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

    (venv) sk@brokebox:~/Research/magentic$ python3 command_execution.py Touch a file name github-test.txt with Testing 1,2,3 as the first and only line in the file
    GPT Output: To create a file named 'github-test.txt' with the content 'Testing 1,2,3', you can use the following command:

     ```
     echo 'Testing 1,2,3' > github-test.txt
     ```

    This command will create a file named 'github-test.txt' and write the text 'Testing 1,2,3' as the first and only line in the file.
    Clean Command: ["echo 'Testing 1,2,3' > github-test.txt"]
    stdout: 
    Run Output for: None
    
Lets check if it worked:

    (venv) sk@brokebox:~/Research/magentic$ ls
    abcd.txt              github-test.txt   streaming.py  venv
    command_execution.py  README.md         test.py
    function_chain.py     requirements.txt  test.txt
    (venv) sk@brokebox:~/Research/magentic$ cat github-test.txt 
    Testing 1,2,3

Todo
* [ ] Have the commands execute in subdirectory on the local fs

* [ ] Where the assertions are executed, could instead have the llm generate the asserts to validate the command and then we (in some environment) assert them. Additionally, then feed the error back into the llm and prompt it to fix. 

* [*FIXED*] In `command_execution.py` when it attemps to execute the command, it just "creates directories" for each "command" it is suppose to be executing. The split() command ([list]) looks correct, but the subprocess.check_output(command) totally bombs. Need to fix this.

Summary

* Really just messin around with Magentic, there's a few examples of calling the LLM as a decorator. It's a cool concept.
