import re
import os
from .scoring import get_numeric

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)

def get_similiar_filename(expected_check_script_set, actual_check_script_set, test_set_file_prefix, test_set_file_suffix):
    check_script_set= [None]*len(expected_check_script_set)

    for idx, i_path in enumerate(expected_check_script_set):
        i = os.path.basename(i_path).lower()

        for s_path in actual_check_script_set:
            s = os.path.basename(s_path).lower()

            if i==s:
                check_script_set[idx]= s_path
                break
            else:
                temp_s= s

                if test_set_file_prefix in temp_s:
                    start, end = re.search(test_set_file_prefix.lower(), temp_s).span()
                    # x= re.findall(test_set_file_prefix.lower(), temp_s)

                    temp_s = temp_s[:start] + temp_s[end:]

                    if test_set_file_suffix=='' or test_set_file_suffix in temp_s:
                        start, end = re.search(test_set_file_suffix.lower(), temp_s).span()
                        temp_s = temp_s[:start] + temp_s[end:]

                        # print('Numeric List:',list(map(int, get_numeric(temp_s))))
                        if idx+1 in list(map(int, get_numeric(temp_s))):
                            check_script_set[idx]= s_path
                            break


    return check_script_set