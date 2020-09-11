# Grading rubric for coding assignments

### Correctness (50%)

Your program should work correctly on all inputs. Also, if there are any
specifications about how the program should be written, or how the output
should appear, those specifications should be followed.

* 50% (full points)
  * Program always works correctly and meets the specifications
* 30%
  * Minor details of the program specification are violated, program functions
    incorrectly on some inputs.
* 15%
  * Significant details of specification are violated, or the program often exhibits incorrect behavior.
* 0%
  * Program does not execute

### Readability (30%)

Code follows PEP8 guidelines (use a linter, such as `pylint` or `flake8`).
Variables and functions should have meaningful names. Code should be organized
into functions/methods where appropriate (rather than long passages of ad hoc
code).

* 30% (full points)
  * Code is clean, understandable, well-organized
* 20%
  * Minor issues such as inconsistent indentation, variable naming, general organization
* 10%
  * At least one major issue that makes it difficult to read
* 0%
  * Several major issues that make it difficult to read.

### Documentation (10%)

Your code should be appropriately commented. Not every line should be commented
because that makes your code overly busy.  Think carefully about where comments
are needed. All functions/methods should have docstrings describing the purpose
of the function, the expected arguments, and the return type.

* 10% (full points)
  * Code is well commented.
* 7%
  * One or two places could benefit from comments, or the code is overly
    commented
* 3%
  * Major lack of comments make it difficult to understand code.
* 0%
  * No comments, even though comments are needed.

### Elegance (10%)

There are many ways to write the same functionality into your code, and some of
them are needlessly slow or complicated. For example, if you are repeating the
same code, it should be refactored into a new method/function or a `for` loop.

* 10% (full points)
  * Code appropriately uses `for` loops and methods for repeated code, and
    there is minimal hard-coding.
* 5%
  * Code uses a poorly chosen approach in at least one place, for example, hard
    coding something that could be implemented through a `for` loop
* 0%
  * Many instances where code could have used easier/faster/better approach.
