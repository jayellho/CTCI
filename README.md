# Preface
This code repository is in <b>Python</b> and is intended to assist readers of 'Cracking the Coding Interview' (by Gayle Laakmann) by creating a <b>skeleton directory</b> (by chapter) for their practice, as well as to provide a <b>test harness</b> for easy checking of their solutions. It will also include <b>my code</b> as I follow the book chapter by chapter.

The skeleton directory would include the following:  
1. .py files for each question in the chapter. This will run through the user-defined test cases and output the number of passed test cases.
2. .txt file for user-defined test cases. NOTE: If you need more test cases, feel free to add them into the .txt but just follow the format of the skeleton .txt.

# How to use
1. Ensure you have Python 3 installed.
2. Open a terminal and run `python create_skeleton_dir_by_chapter`.
3. Follow the prompts from the code to create your skeleton directory by chapter.
4. Edit the .py to include your code for each question.
5. Edit the .txt to include your test cases as necessary.
6. Upon completion, test each question by running `python <question number>.py` in a terminal.

# Notes on specific files in this repository
### code_playground.ipynb
For users to try out their code before putting into the different .py files for actual testing.

### create_skeleton_dir_by_chapter.py
This includes code to create the skeleton directory. Makes use of `sample_soln_file.py` below.

### sample_soln_file.py
This is the skeleton code for each .py file that is created using `create_skeleton_dir_by_chapter.py`.

# Notes to self regarding testing
<b>Possible test cases (not exhaustive):</b>  
- Case #1: Variations on the scenario in the question
- Case #2: Inputs not as described
- Case #3: Duplicates
- Case #4: Performance
