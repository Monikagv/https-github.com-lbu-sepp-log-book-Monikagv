#!usr/bin/env python3

import sys

from student_id_function import (get_student_id, get_student_surname, get_student_initials, get_four_random_digitis
                                 generate_email_from_line)

if __name__=='__main__':

    test_lines = [
        'c1235566 Jones, Jane Louise',
        'c1234550 Smit-Jones, Frank',
        "c9876553 O'Reilly, James Edward",
        'c6879484 de Silva, Mario',
    ]

    for line in test_lines:
        print(f'{line}-->{generate_email_from_line(line)}')

       line = input('Enter the line: ')

       email = (f'{get_student_id(line)}{get_student_initials(line)}{get_student_surname(line)}
       f'{get_four_random_digitis(line)}@pop.ac.uk')

       print(email)

       exit()

