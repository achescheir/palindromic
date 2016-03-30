#Palindrome Testing

###Console
If run with no arguments asks for input and replies whether of not it was a
palindrome. If it was not a palindrome it then searches the line to find
palindromes in sub-sentences of the line.

###From File
If run with a filename as an argument it echoes each line and replies if it is a
palindrome or not.

###is_palindrome arguments
is_palindrome() can be run in recursive or non-recursive mode, depending on the
recurse argument.
By default the function is not case sensitive all non-alphabetical characters
are removed. Although the only current options are no manipulation of the input
or full removal of non-alphabetical characters and case insensitive, it would
not be too hard to add more options. If no manipulation is used this function
should work on any indexable data type.
