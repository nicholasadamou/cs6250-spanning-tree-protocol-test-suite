# CS6250 Spanning Tree Protocol Test Suite

*Test your spanning tree protocol algorithm against the official solutions provided by the CS6250 TAs.*

## What does it do?

It will parse the solution for the selected topology you've chosen. It will then compare the solution to your output. If the output matches the solution, it will print acknowledge that your output matches the solution. If the output does not match the solution, it will acknowledge that your output does not match the solution. If chosen to test all cases, it will acknowledge the number of tests that passed versus fail.

## How do I download it?

Clone this repository into your `SpanningTree` directory.

```bash
git clone \
 https://github.com/nicholasadamou/cs6250-spanning-tree-protocol-test-suite \
 test-suite
```

## How do I use it?

From within the `test-suite` directory, run the following command:

```bash
# python3 tester.py {name of topology here}

python3 test_spanning_tree.py SimpleLoopTopo

# If no topology is specified it will default to use all topologies.
# By 'all' I mean each topology provided in the solutions directory.
# These solutions are the official solutions provided by the TAs for
# project 1.

python3 test_spanning_tree.py

# Alternatively, you can test against the student topologies provided.

python3 test_student_spanning_tree.py 4dHyperCubeTopo

# If no topology is specified it will default to use all student topologies.

python3 test_student_spanning_tree.py
```

### What if I am on Windows?

1. Followed the steps [here](https://code.visualstudio.com/docs/remote/wsl) to download WSL and add the WSL extension to VS Code (default Ubuntu distribution worked).
1. Open a WSL terminal from VS Code.
2. Run the git clone command from above in the WSL terminal.
3. Following the steps from above to run `test_spanning_tree.py` or `test_student_spanning_tree.py`.
