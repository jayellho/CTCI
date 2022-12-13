# Import libraries.
import os
import shutil

# Mapping dictionary for changing numbers to letters
dict_map_no_to_letter = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}


# User input to create the templates.
def inputs_from_user():
    inputs_dict = {}
    inputs_dict["input_chapter_no"] = input("Please input the chapter number from CTCI. E.g.: 10\n")
    input_chapter_title = input("Please input the chapter title from CTCI. E.g.: 'Sorting and Searching'\n")
    input_chapter_title = input_chapter_title.lower().replace(" ", "_")
    inputs_dict["input_chapter_title"] = input_chapter_title
    inputs_dict["input_number_of_qns"] = input("Please input the number of questions for current chapter. E.g.: 10\n")
    return inputs_dict

# Create new folder.

def create_new_folder(inputs_dict):
    new_dir_name = f"{inputs_dict['input_chapter_no']}_{inputs_dict['input_chapter_title']}"
    parent_dir = os.getcwd()
    new_dir_full_path = os.path.join(parent_dir, new_dir_name)

    if not os.path.exists(new_dir_full_path):
        os.makedirs(new_dir_full_path)

    return new_dir_full_path

# Create test_cases.txt skeleton.
def create_test_cases_txt(inputs_dict, new_dir):
    input_number_of_qns = int(inputs_dict["input_number_of_qns"])
    filename = 'test_cases.txt'
    full_file_path = os.path.join(new_dir, filename)
    with open(full_file_path, 'w') as f:
        for i in range(input_number_of_qns):
            input_chapter_no = str(inputs_dict['input_chapter_no']) + "." + str(i+1)
            #cleaned_chapter_no = "".join([dict_map_no_to_letter[i] if i in dict_map_no_to_letter else i for i in input_chapter_no])
            f.write("====\n")
            f.write(f"{input_chapter_no}\n")

            for each_case in range(10):
                f.write(f'# {each_case+1} <description of this test case here if you want>\n')
                f.write(f'[] >>>>> []\n\n')


# Create individual python files for each question.
def create_soln_files(inputs_dict, new_dir, py_filename_to_copy):
    no_of_files_to_create = int(inputs_dict['input_number_of_qns'])

    # Source
    parent_dir = os.getcwd()
    full_path_of_py = os.path.join(parent_dir, py_filename_to_copy)

    # Target
    for i in range(no_of_files_to_create):
        input_chapter_no = str(inputs_dict['input_chapter_no']) + "." + str(i+1)
        #cleaned_chapter_no = "".join([dict_map_no_to_letter[i] if i in dict_map_no_to_letter else i for i in input_chapter_no])
        new_filename = f"{input_chapter_no}.py"
        full_path_of_new_py = os.path.join(new_dir, new_filename)
        if not os.path.exists(full_path_of_new_py):
            shutil.copy(full_path_of_py, full_path_of_new_py)






if __name__ == "__main__":
    inputs_dict = inputs_from_user()
    new_folder = create_new_folder(inputs_dict)
    create_test_cases_txt(inputs_dict, new_folder)
    create_soln_files(inputs_dict, new_folder, "sample_soln_file.py")


