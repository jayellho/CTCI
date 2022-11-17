# Import libraries.
import os
import shutil

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
    with open(full_file_path, 'ws') as f:
        for i in range(input_number_of_qns):
            f.write("====\n")
            f.write(f"{inputs_dict['input_chapter_no']}.{i+1}\n")
            f.write("1\n")
            f.write("\n")
            f.write("2\n")
            f.write("\n")
            f.write("3\n")
            f.write("\n")


# Create individual python files for each question.
def create_soln_files(inputs_dict, new_dir, py_file_to_copy):



if __name__ == "__main__":
    inputs_dict = inputs_from_user()
    new_folder = create_new_folder(inputs_dict)
    create_test_cases_txt(inputs_dict, new_folder)
    create_soln_files(inputs_dict, new_folder, py_file_to_copy)
    print(new_folder)


