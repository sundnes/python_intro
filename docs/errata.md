## Known bugs and typos

Quite a few bugs have been discovered in the code examples of the book. These
have all been corrected in the source code files available here, but they
are still present in the [published version](https://www.springer.com/gp/book/9783030503550):

### Chapter 3
* In the last code block on page 24, the first line of the interactive session is 'l[0] =2'. But
  the variable 'l' has not been defined, and this line has nothing to do with the rest of the example.

### Chapter 4
* In the code block on page 41, an argument is missing in the call to the function 'amount'. The
  call should read something like 'a0, r = amount(7,r)'.
* There are some minor errors in the interactive session on page 44-45, which illustrates
  the use of default arguments. Specifically, the third call to 'somefunc' is listed
  with the wrong output and an incorrect comment.

### Chapter 5
* In the second code block on page 76, in line 'n = years(P, 2*P, p)', the variable 'p' is
  not defined. It should be replaced by 'r'.
* Similar to the above, in the second code block on page 77, the f-string in the print statement includes the
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
* On page 88, a comment in the code block says '[tmin, tmax,... ]' where it should have
  been '[xmin, xmax,... ]'.
* In the last code block on page 90, in the line 't = np.linspace(0, 8, 201)',
  't' should be replaced by 'x'.
* In the code blocks on page 99, continued from page 98, the prefix 'np.' is missing
  in front of 'zeros', 'asarray' and other NumPy functions.
* In the last code block on page 99, in line 'a[a < 0] = a.max() # if a[i]<10, set a[i]=10', the
   comment does not match the code. The code will replace all entries of 'a' below 0, but the comment
   says below 10.

### Chapter 7
* On page 102, there should be quotes around the word 'Berlin' in the code block in the middle.
* On page 103, the print statement in the second-to-last code block is missing parentheses.
* On page 106, missing parantheses in the print statement in the last code block.
* On page 109, the ':' that appear on the first lines of the first interactive example
  should not be there. Further down in the same example the print statements are missing
  parentheses.
* In the last code block on page 111, there should be quotes around 5 in the line
  's2 = s.replace(s[18],5)' to make the argument a string ('5') rather than an integer.

### Chapter 8
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
 * On page 126, the first line of the second code block, 'from tmp import *', should be
   removed.

### Chapter 9
* In the definition of the Trapezoidal class on page 144, the prefix 'np.' is missing
  in front of the NumPy functions 'zeros' and 'linspace'.
* In the Simpson class on page 144, the print statement is missing parentheses.

The list is probably incomplete. If you find bugs or typos that are not on this
list, please send an email to sundnes@simula.no
