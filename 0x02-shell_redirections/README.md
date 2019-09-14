This is the README.md for the 0x02-shell_redirections folder. It contains some requirements, each file in this directory and which script they contain.

File name : Script description


0-hello_world : Prints "Hello, World" followed by a new line to the standard output.

1-confused_smiley : Displays a confused smiley-> "(Ôo)' 

2-hellofile : Displays content of "/etc/passwd".

3-twofiles : Displays the content of "/etc/passwd" and "/etc/hosts".

4-lastlines : Displays the last 10 lines of "/etc/passwd".

5-firstlines : Displays the first 10 lines of "/etc/passwd".

6-third_line : Displays third line of "iacta". Can't use sed.

7-file : Creates a file named exactly->  \*\\'"Holberton School"\'\\*$?\*\*\*\*\*:)  <- contains the test "Holberton School" ending by a new line.

8-cwd_state : Writes into the file "ls_cwd_content" the result of the command "ls -la". (Creates it else, overwrites it)

9-duplicate_last_line : Duplicates the last line of the file iacta.

10-no_more_js : Deletes all regular files with a .js extension. Not directories. In current and sub.

11-directories : Counts all number of directories and sub-directories in current directory. (Doesn't include current or parent).

12-newest_files : Displays the 10 newest files in the current directory. One file per line and from newest to oldest.

13-unique : Input a list of words but only output words that appear once. Words should be sorted and every line has one word.

14-findthatword : Display all lines containing "root" from /etc/passwd.

15-countthatword : Display number of lines containing "bin" from /etc/passwd.

16-whatsnext : Display lines containing "root" and 3 lines after from /etc/passwd.

17-hidethisword : Display all lines that don't contain "bin" from /etc/passwd.

18-letteronly : Display all lines, that start with a letter, from "/etc/ssh/ssh_config".

19-AZ : Replacae all A with Z and c with e from the input.

20-hiago : Removes all letters c and C from input.

21-reverse : Reverses input.

22-users_and_homes : Displays all users and their home directories. Sorted by Users.


Other general requirements include:
- Either vi, vim, or emacs
- Each file should be exactly 2 lines long
- All files should end with new line
- First line for each file should be: #!/bin/bash