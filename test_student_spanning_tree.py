#!/usr/bin/python3

import os
import sys

def read_file(file_path):
    lines = []

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()

    return lines


def parse_student_topologies():
    topologies = []

    for file in os.listdir('student_topologies'):
        file_name = file.split('.')[0]

        if file.endswith('.py'):
            topologies.append(file_name)

    return topologies


def clean_up(topologies):
    for file in os.listdir('.'):
        file_name = file.split('-')[0]

        if file_name in topologies and file.endswith('.log'):
            os.system(f'rm {file}')


def run_spanning_tree_test(topology):
    did_test_pass = False

    hash = os.urandom(16).hex()

    os.system(f'cp student_topologies/{topology}.py {topology}.py')
    os.system(f'python3 ../run.py ../{topology} {topology}-{hash}.log')

    output = read_file(f'{topology}-{hash}.log')
    expected = read_file(f'solutions/student_solutions/{topology}.log')

    if output == expected:
        did_test_pass = True

        print(f'{topology} passed')
    else:
        did_test_pass = False

        print(f'{topology} failed')

    os.system(f'rm {topology}-{hash}.log')
    os.system(f'rm {topology}.py')

    return did_test_pass


program = sys.argv[0]

topology = sys.argv[1] if len(sys.argv) == 2 else "ALL"
number_of_tests_passed = 0
number_of_tests_failed = 0

topologies = parse_student_topologies()

clean_up(topologies)

if topology != "ALL" and topology not in topologies:
    print("Topology not found")
    print("Defaulting to all topologies")

    topology = "ALL"

if topology == "ALL":
    for topology in topologies:
        did_test_pass = run_spanning_tree_test(topology)

        if did_test_pass:
            number_of_tests_passed += 1
        else:
            number_of_tests_failed += 1

    print()

    print(f'{number_of_tests_passed} tests passed')
    print(f'{number_of_tests_failed} tests failed')

    number_of_tests = len(topologies)

    print(f'{number_of_tests_passed}/{number_of_tests} tests passed')

    exit()

run_spanning_tree_test(topology)
