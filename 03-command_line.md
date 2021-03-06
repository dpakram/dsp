# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 

##Command Line Cheat Sheet

* pwd outputs the name of the current working directory
* ls lists all files and directories in the working directory
* cd switches you into the directory you specify
* mkdir creates a new directory in the working directory
* touch creates a new file inside the working directory

###Modify the behavior of commands:
* ls –a lists all contents of a directory, including hidden files and directories
* ls –l lists all contents in long format
* ls –t order files and directories by the time they were last modified
* ls –alt multiple options at once 

###Copy, move, and remove files and directories:
* cp copies files
* mv moves and renames files
* rm removes files
* rm –r removes directories

Wildcards
- * selects all

Redirection reroutes standard input, standard output, and standard error

###Common redirection commands are:
- > redirects standard output of a command line to a file, overwriting previous content
- >> redirects standard output of a command to a file, appending new content to old content
- < redirects standard input to a command
- | redirects standard output of a command to another command

###These can be combined with redirection commands:
- sort sorts lines of text alphabetically
- uniq filters duplicate, adjacent lines of text
- grep searches for a text pattern and outputs it
- sed  searches for a text pattern, modifies it, and outputs it

Environment refers to the preferences and settings of the current user.

The nano editor is a command line text editor used to configure the environment.

~/.bash_profile is where environment settings are stored. You can edit this file with nano

Environment variables are variables that can be used across commands and programs and 
hold information about the environment 
- export VAIRABLE=”Value” sets and exports an environment variable.
- USER is the name of the current user
- PS1 is the command prompt
- HOME is the home directory. It is usually not customized
- PATH  returns a colon separated list of file paths. IT is customized in advanced cases.
- Env returns a list of environment variables. 


---

###Q2.  List Files in Unix   

What do the following commands do:  
> > - `ls`  lists all files and directories in the working directory
- `ls -a`  lists all contents of a directory, including hidden files and directories
- `ls -l`  lists all contents in long format
- `ls -lh`  print sizes in human readable format
- `ls -lah`  a combination of ls -lh and ls -a
- `ls -t`  order files and directories by the time they were last modified
- `ls -Glp`  a combination of ls -G (Displays the long format listing, but exclude the owner name), ls -l (Displays the long format listing.) and ls-p (Displays directories with /)


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > - 'ls -r' Displays files in reverse order.
- 'ls -t' displays newest file first
- 'ls -1' displays each entry on a line
- 'ls -m' Displays the names as a comma-separated list.
- 'ls -u' Displays files by the file access time.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is a command used to execute commands based on arguments from standard input. It can be combined with with other commands. For example xargs can be used in combination with find in order to do something with the list of files returned by find. Recursively find all Python files and count the number of lines
'find . -name '*.py' | xargs wc -l'

 

