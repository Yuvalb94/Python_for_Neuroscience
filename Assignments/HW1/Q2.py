def compare_subjects_within_student(subj1_all_students, subj2_all_students):
    """Compare the two subjects with their students and print out the higher-graded subject for each student.

    Single-subject students shouldn't be printed.

    Parameters
    ----------
    subj1_all_students, subj2_all_students
        Data structures which contain the grades of all students in a given subject.

    Notes
    -----
    Choice for the data structure of the function's arguments is up to you.

    Returns
    -------
    A data structure with the name of the student and the corresponding subject.
    """

    result = {}
    for student, grades in subj1_all_students.items():
        # The 'subject' key in each dictionary is not a student name, skip this key.
        if student == 'subject':
            continue
        # Check if current student is in both subjects, if not - continue
        if student not in subj2_all_students:
            continue
        # If the student is in both subjects, compare the grades and store the higher-graded subject for each student in the results dictionary.
        if max(grades) > max(subj2_all_students[student]):
            result[student] = subj1_all_students['subject']
        else:
            result[student] = subj2_all_students['subject']
    return result
