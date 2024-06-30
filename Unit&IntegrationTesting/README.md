# Unit Testing and Integration Testing

- Testcase is created by subclassing `unittest.TestCase`.

    1. `assertEqual()` - To check for an expected result.
    2. `assertTrue()` or `assertFalse()` - To verify a condition.
    3. `assertRaises()` - To verify that a specific exception gets raised.

- N/B: All the methods in the testcase class start with `test_`

- The above methods are used instead of the `assert` statement so the test runner can accumulate all test results and produce report.

- The `setUp()` and `tearDown()` methods allow to define instructions that will be executed before and after each test method.

- To run the tests => `unittest.main()` provides a command-line interface to the test script.
- Passing the `-v` option when running the test script will instruct `unittest.main()` to enable a higher level of verbosity(state of being verbose or wordy).

## Running the unittests from CLI

```bash
python3 -m unittest tests/test_something.py

```

### Unittest Command-line options

1. `-v` - for verbosity
2. `-h` - Help (List all the command-line optionss)
3. `-b` or `--buffer` - The standard output and standard error streams are buffered during the test run. Output during a passing test is discarded. Output is echoed normally on test fail or error and is added to the failure messages.
4. `-c` or `--catch` - Control-C during the test run waits for the current test to end and then reports all the results so far. A second Control-C raises the normal KeyboardInterrupt exception.
5. `-f`, `--failfast`
Stop the test run on the first error or failure.
6. `-k`
Only run test methods and classes that match the pattern or substring. This option may be used multiple times, in which case all test cases that match any of the given patterns are included.

Patterns that contain a wildcard character (*) are matched against the test name using fnmatch.fnmatchcase(); otherwise simple case-sensitive substring matching is used.

Patterns are matched against the fully qualified test method name as imported by the test loader.

For example, -k foo matches foo_tests.SomeTest.test_something, bar_tests.SomeTest.test_foo, but not bar_tests.FooTest.test_something.

7. `--locals`
Show local variables in tracebacks.

8. `--durations N`
Show the N slowest test cases (N=0 for all).


## Test Discovery




## Author

- **@waltertaya**
