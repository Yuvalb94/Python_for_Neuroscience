"""Exercise 1.2 
Write a function that receives an iterable of full subject names (first name and then last name) and returns a dictionary of nested dictionaries, wherein each key is in the format “sub-i” and each value is a dictionary containing the keys "first_name" and "last_name", as well as the corresponding values.

For example:

subjects = ["Freddie Mercury", "Robert Plant"]

parse_subject_names(subjects)

{'sub-0': {'first_name': 'Freddie', 'last_name': 'Mercury'},

 'sub-1': {'first_name': 'Robert', 'last_name': 'Plant'}}

"""

def split_string(string):
    """
    Splits a string into a list of words.

    Parameters
    ----------
    string : str
        The input string to be split.

    Returns
    -------
    list
        A list of words obtained by splitting the input string.
    """
    # split the string into words using whitespace as the delimiter
    return string.split()


def parse_subjects_names(subjects):
    """
    Parses a list of full subject names into a dictionary of nested dictionaries.

    Parameters
    ----------
    subjects : list
        A list of full subject names (first name and last name).

    Returns
    -------
    dict
        A dictionary where each key is in the format "sub-i" and each value is a
        dictionary containing the keys "first_name" and "last_name", along with
        the corresponding values.
    """
    result = {}
    for i, subject in enumerate(subjects):
        # Split the subject name into first and last names
        first_name, last_name = split_string(subject)
        # Create the nested dictionary for each subject
        result[f'sub-{i}'] = {'first_name': first_name, 'last_name': last_name}
    return result

if __name__ == "__main__":
    # Example usage
    subjects = ["Freddie Mercury", "Robert Plant"]
    parsed_subjects = parse_subjects_names(subjects)

    # print the results as a dictionary
    print("Parsed subjects:")
    # print the parsed subjects
    for key, value in parsed_subjects.items():
        print(f"{key}: {value}")