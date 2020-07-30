## Known bugs and typos

A few bugs have been discovered in the code examples of the book. These
have all been corrected in the source code files available here, but they
are still present in the [published version](https://www.springer.com/gp/book/9783030503550):

### Chapter 3
* In the last code block on page 24, the first line of the interactive session is 'l[0] =2'. But
  the variable 'l' has not been defined, and this line has nothing to do with the rest of the example. 

### Chapter 5
* In the second code block on page 77, the f-string in the print statement includes the
  variable 'p' at the end. But 'p' is not defined, and should be replaced by 'r'
* On page 78, in the code block that starts on page 77, the assert statement uses
  the wrong variable names. 'A0' should be replace by 'P' and 'p' by 'r'.

### Chapter 6
* In the block in the middle of page 84, the variable 'y' is never defined. For the
  loop to work this needs to be initialized to an array having the same length
  as 'x'.
* In the formula at the top of page 86, the bounds for *x* are first defined in the
  formula and then again on the next line. The definition in the formula makes most
  sense, and is consistent with the code.

## Chapter 8
 * The wrong class name is used in the interactive session at the bottom of page 121. To
   be consistent with the code above, 'Account' must be replaced by 'BankAccount'.
   For the session to work one should also include an import of 'BankAccount'.
 * In the same interactive session example, the print statement is missing parentheses.
 * In the 'BankAccountP' example on page 122 there are multiple bugs:
   * The constructor includes the line 'self._last_name = name', which should be 'self._last_name = last_name' to be
     consistent with the argument list.
   * In the method 'print_info', the underscore is missing in front of all the
     instance variables, 'first = self.first_name' should be 'first = self._first_name', etc.
   * In the same method, a local variable is named 'bal', but in the next line the 'balance'
     is used, which is not defined.

The list is probably incomplete. If you find bugs or typos that are not on this
list, please send an email to sundnes@simula.no
