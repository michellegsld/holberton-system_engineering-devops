This is the README.md for the 0x01-shell_permissions folder. It contains some requirements, each file in this directory and which script they contain.

Each file within this directory : description of script it contains

0-iam_betty : Changes user ID to "betty".

1-who_am_i : Prints the effective userif of the current user.

2-groups : Prints all the groups the current user is part of.

3-new_owner : Changes owner of "hello" file to the user "betty".

4-empty : Creates an empty file called "hello".

5-execute : Adds execute permission to the owner of "hello".

6-multiple_permissions : Adds execute permission to owner and group owner and the read permission to other users, to "hello".

7-everybody : Adds execution permission to owner, group owner, and the other users to "hello".

8-James_Bond : Sets permission of "hello", where the owner and group owners have no permission at all while other users has all.

9-John_Doe : Sets mode of "hello" to -rwxr-x-wx.

10-mirror_permissions : Sets mode of "hello" to the same as another file's, "olleh".

11-directories_permissions : Adds execute permission to all subdirectories of the current directory for the owner, group owner and all other users. Regular files won't be changed.

12-directory_permissions : In current directory, creates a directory called "dir_holberton" with permissions 751.

13-change_group : Changes group owner to "holberton" of the file "hello".

14-change_owner_and_group : Changes owner to "betty" and group owner to "holberton" for all files and directories in working directory.

15-symbolic_link_permissions : Changes owner to "betty" and group owner to "holberton" of the file "__hello".

16-if_only : Changes owner, to "betty" of the file "hello", but only if it's owned by another certain user, "guillaume".

100-Star_Wars : Plays StarWars IV.

101-man_holberton : Creates a man page.

Other general requirements include:
- Either vi, vim, or emacs
- Each file should be exactly 2 lines long
- All files should end with new line
- First line for each file should be: #!/bin/bash
