# Modify your code here. Feel free to include your own functions but DO NOT change the name of and number of inputs for the 'code_run' function.
def code_run(some_input):
    print("code_run ran!")
    some_output = []
    return some_output



# Do not touch code within this========================
## Import libraries.
import ast
import os

## Functions
def check_against_test_cases(path_to_test_cases_file):
    passed_cases_per_qn = 0
    total_cases_per_qn = 0
    current_py_wo_py = os.path.basename(__file__)[:-3]
    with open(path_to_test_cases_file) as f:
            file_content = f.readlines()
            for indx, line in enumerate(file_content):
                
                # stop loop just before last item in loop.
                if indx == len(file_content)-1:
                    break

                # identify new qn.
                if '====' in line:
                    qn_no = file_content[indx+1].strip() # strip to remove line breaks
                    
                elif '#' in line and qn_no == current_py_wo_py:
                    print(f"qn_no = {qn_no}")
                    # get test case no.
                    test_case_no = line.split(" ")[1]
                    
                    # get test case input.
                    test_case_input = file_content[indx+1].split(">>>>>")[0].strip()
                    cleaned_test_case_input = ast.literal_eval(test_case_input)
                    
                    # get test case output
                    test_case_expected_output = file_content[indx+1].split(">>>>>")[1].strip()
                    cleaned_test_case_expected_output = ast.literal_eval(test_case_expected_output)
                    
                    # run user code and compare to test case expected output.
                    actual_output = code_run(cleaned_test_case_input) # LOOK HERE. THIS IS WHERE USER CODE IS RUN.
                    total_cases_per_qn += 1
                    if actual_output == cleaned_test_case_expected_output:
                        print(f"Test case {test_case_no} passed!")
                        passed_cases_per_qn += 1
                    else:
                        print(f"Test case {test_case_no} failed! Please amend your code.")
                        print(f"Your output is: {actual_output}")
                        print(f"The actual output should be: {cleaned_test_case_expected_output}")
            
            return [passed_cases_per_qn, total_cases_per_qn, current_py_wo_py]

if __name__ == "__main__":

    results = check_against_test_cases('test_cases.txt')
    print(f"OVERALL RESULTS FOR QN {results[2]}: {results[0]}/{results[1]} test cases passed.")
# Do not touch code within this========================
