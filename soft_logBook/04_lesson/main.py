#!usr/bin/env python3

    import sys

    from student_id_function import get_student_id, get_student_surname, get_student_initials, get_four_random_digitis

    if __name__=='__main__':

       line = input('Enter the line: ')

       email = (f'{get_student_id(line)}'{get_student_initials(line)} {get_student_surname(line)}
       f'{get_four_random_digitis(line)}@pop.ac.uk')

       print(email)