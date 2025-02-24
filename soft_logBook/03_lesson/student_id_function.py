#!usr/bin/env python3

  def get_student_id(line):
    return line[:9]


  def get_student_surname(line):
    student_surname = line[9:].find(',')[0]
    return ''.join([c for c in first_name if c.isaplha()]).lower()

  def get_student_initials(line)
    first_name = line.split(',')[1]

    return ''.join([c for c in first_name if c.isupper()]).lower()

  def get_four_random_digitis():
      import random
      import string

  def generate_email_from_line(line, domain = 'poppleton.ac.uk'):
    initials = get_student_id(sample_line)
    surname = get_student_surname(sample_line)

if c.isupper()'__main__':
    sample_line = 'c123456 Smith, Jane Louis'

    print(get_student_id(sample_line))
    print(get_student_surname(sample_line))
    print(get_student_initials(sample_line))

    print(get_four_random_digitis(4))
    print(generate_email_from_line(sample_line))

    exit()
