'Full Stack End to End ML Pipeline'

Process:
1. Create a github repository - Here the name given is End-End-ML-Pipeline
2. Create a folder in the system under the same name
3. Open a terminal at that folder or open the vscode at the folder and open a new terminal and then create a virtual environment
4. Use the following command 
    pip3 install virtualenv
    virtualenv venv             # Here venv is name of the virtual environment
    source venv/bin/activate
5. Create a readme file and then add the required information as per need
6. Now use the github commands to initialise the repository and push the files
    git init
    git status
    git add .
    git commit -m 'Message for commit'
    git branch -M master
    if first time configure the git with your username and email_id
    git config --global user.name '<user_name>'
    git config --global user.email <email id>
    git remove -v        # To check the links that can be added
    git remote add origin https://github.com/gowtham12591/End-End-ML-Pipeline
    git push -u origin master    # This will push the files to the repo
6. Now create a .gitignore file using add files option the repository and click commit changes
7. We can use 'git pull' command to pull the .gitignore file to our local system
8. Create 'setup.py' and 'requirements.txt' file inside the folder
    - With the help of setup.py file we can package our entire ML application and we can also deploy in 'pypy' - Place where our python libraries are packaged and used
    - To utilize the find_packages create a folder named src and inside that create a file '__init__.py'
    - So whenever the find_packages is called this will automatically check for this source file '__init__.py' and initialize it - This is for pypy package
    - Entire working will be saved under this folder 'src'
9. Now use the command 'pip3 install -r requirements.txt' trigger the setup.py file and install the required files and dependencies
10. Finally push the entire file to the repository using git add, git commit and git push commands. 
   