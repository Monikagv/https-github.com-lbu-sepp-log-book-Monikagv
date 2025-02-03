### Linux cheat sheet

* ssh: Connect to another
* pwd: Prints the current working directory.
* ls: Lists files and directories in the current directory.
* cd: Changes the current working directory.
* mkdir: Creates a new directory.
* rmdir: Removes an empty directory.
* touch: Creates an empty file or updates the timestamp of an existing file.
* cp: Copies files or directories to another location.
* mv: Moves or renames files and directories.
* rm: Deletes files or directories.
* cat: Displays the content of files.
* less: Views file content page-by-page with backward/forward navigation.
* more: Views file content page-by-page with forward navigation only.
* head: Displays the first few lines of a file.
* tail: Displays the last few lines of a file.
* grep: Searches for patterns or specific text within files.
* find: Searches for files and directories based on given criteria.
* echo: Outputs text or variable values to the terminal.
* man: Opens the manual page for a command for detailed usage instructions.
* history: Shows a list of previously executed commands.
* clear: Clears all the text from the terminal screen.
* chmod: Changes the access permissions of files or directories.
* chown: Changes the ownership of files or directories.
* ps: Displays a snapshot of current running processes.
* top: Provides a real-time view of system processes and resource usage.
* kill: Sends a signal to terminate or manage a process by its process ID (PID).
* sudo: Executes commands with superuser or administrative privileges.
* nano: Open a simple editor
* vim: open a more advanced text editor
* shred: Destroy a file, so it can't be recovered
* In: create shortcuts or links to files
* whoami: show your current user name

## File Commands
* ls: List files and directories (options: -l for long, -a for all, -h for human-readable sizes).
* cd: Change the current directory.
* pwd: Print the current working directory.
* mkdir: Create a new directory.
* rm: Remove files or directories (use -r for recursive, -f for force)
* cp: Copy files or directories (use -r for directories)
* mv: Move or rename files and directories.
* touch: Create an empty file or update file timestamps.
* cat: Display the contents of a file.
* head: Show the first few lines of a file (use -n to specify the number of lines)
* tail: Show the last few lines of a file (use -n to specify the number of lines)
* ln: Create links between files (use -s for symbolic links)
* find: Search for files and directories (e.g., using -name or -type options)

##  File Permission Commands

* chmod: Change file permissions (use u, g, o, +, -, or =).
* chown: Change file ownership.
* chgrp: Change group ownership.
* umask: Set default file permissions.

## File Compression and Archiving Commands

* tar: Create or extract archive files (options: -c, -x, -f, -v, -z, -j).
* gzip: Compress files (use -d to decompress).
* zip: Create compressed zip archives (use -r to include directories recursively)

## Process Management Commands

* ps: Display running processes (e.g., aux shows all processes).
* top: Monitor system processes in real-time.
* kill: Terminate a process (use -9 for force).
* pkill: Kill processes by name.
* pgrep: List processes by name.
* grep: Search for patterns in text (various options: -i, -v, -r, -l, -n, etc.)

## System Information Commands

* uname: Print system information (use -a for all details).
* whoami: Display the current username.
* df: Show disk space usage (use -h for human-readable sizes).
* du: Estimate file/directory sizes (use -h and -s for total size).
* free: Display memory usage (use -h for human-readable format).
* uptime: Show system uptime.
* lscpu: Display CPU information.
* lspci: List PCI devices.
* lsusb: List USB devices.

## Networking Commands

* ifconfig: Display network interface information.
* ping: Send ICMP echo requests to check connectivity.
* netstat: Display network connections and statistics (use -tuln for listening ports).
* ss: Display network socket information (use -tuln for TCP/UDP sockets).
* ssh: Securely connect to a remote server.
* scp: Securely copy files between hosts.
* wget: Download files from the web.
* curl: Transfer data to or from a server.

##  IO Redirection Commands#

* cmd < file: Use a file as input for a command.
* cmd > file: Redirect standard output (stdout) of a command to a file.
* cmd 2> file: Redirect error output (stderr) of a command to a file.
* cmd 2>&1: Redirect stderr to the same destination as stdout.
* cmd1 <(cmd2): Use the output of one command as input for another.
* cmd > /dev/null: Discard the stdout of a command.
* cmd &> file: Redirect all output (stdout and stderr) to a file.
* cmd 1>&2: Redirect stdout to the same destination as stderr.
* cmd >> file: Append stdout to a file.

##  Environment Variable Commands

* export: Set an environment variable (e.g., export VAR=value).
* echo: Display the value of an environment variable (e.g., echo $VAR).
* env: List all environment variables or set one for a specific command.
* unset: Remove an environment variable.
* export -p: List all exported environment variables.
* printenv: Print the values of environment variables.

##  User Management Commands

* who: Show users currently logged in.
* sudo adduser: Create a new user account.
* finger: Display information about logged-in users (or a specific user).
* sudo deluser: Remove a user from a group.
* last: Show recent login history.
* sudo userdel -r: Delete a user account along with its home directory.
* sudo passwd -l: Lock a user's password to prevent login.
* su -: Switch to another user account (with that user’s environment).
* sudo usermod -a -G: Add an existing user to a group.

# Shortcuts Commands

## Bash Shortcuts: 
Bash (Bourne Again SHell) is one of the most commonly used command-line interpreters (shells) on 
Linux and Unix systems. It allows you to execute commands, run scripts, and perform various system tasks.

* Ctrl+A: Move to the beginning of the line.
* Ctrl+E: Move to the end of the line.
* Ctrl+B: Move back one character.
* Ctrl+F: Move forward one character.
* Alt+B: Move back one word.
* Alt+F: Move forward one word.
* Ctrl+U: Cut from the cursor to the beginning of the line.
* Ctrl+K: Cut from the cursor to the end of the line.
* Ctrl+W: Cut the word before the cursor.
* Ctrl+Y: Paste the last cut text.
* Ctrl+R: Reverse search command history.
* Ctrl+P: Go to the previous command in history.
* Ctrl+N: Go to the next command in history.
* Ctrl+L: Clear the screen.
* Ctrl+C: Terminate the current command.
* Ctrl+G: Exit history search mode.

## Nano Shortcuts
* Nano is a simple, user-friendly text editor that runs in the terminal. It’s designed to be easy to use for 
beginners while still offering the essential features needed for editing text files.

* Ctrl+O: Save the file.
* Ctrl+X: Exit Nano.
* Ctrl+R: Read a file into the current buffer.
* Ctrl+J: Justify the current paragraph.
* Ctrl+Y: Scroll up one page.
* Ctrl+V: Scroll down one page.
* Alt+\: Go to a specific line number.
* Alt+,: Go to the beginning of the current line.
* Alt+.: Go to the end of the current line.
* Ctrl+K: Cut from the cursor to the end of the line.
* Ctrl+U: Paste the last cut text.
* Ctrl+6: Mark text for copying or cutting.
* Alt+6: Copy the marked text.
* Ctrl+W: Search for a string.
* Alt+W: Search and replace a string.
* Alt+R: Repeat the last search.

## VI Shortcuts
* vi is one of the oldest and most widely available text editors on Unix-like systems. It operates in different modes
(such as command mode and insert mode) and is known for its efficiency and powerful editing capabilities once you learn its commands.

* cw: Change the current word (delete to the end of the word and enter insert mode).
* dd: Delete the current line.
* x: Delete the character under the cursor.
* R: Enter replace mode (overwrite until Esc is pressed).
* o: Insert a new line below and enter insert mode.
* u: Undo the last change.
* s: Substitute the character under the cursor.
* dw: Delete from the cursor to the beginning of the next word.
* D: Delete from the cursor to the end of the line.
* 4dw: Delete the next four words.
* A: Enter insert mode at the end of the line.
* S: Delete the entire line and enter insert mode.
* r: Replace the character under the cursor.
* i: Enter insert mode before the cursor.
* 3dd: Delete the current line and the two lines below it.
* ESC: Exit from insert or command mode.
* U: Restore the current line to its original state.
* ~: Toggle the case of the character under the cursor.
* a: Enter insert mode after the cursor.
* C: Delete from the cursor to the end of the line and enter insert mode.

## Vim Shortcuts
* Vim stands for “Vi Improved” and is an enhanced version of the vi editor. It retains the core modal editing features 
* of vi but adds many improvements and additional functionalities, making it a popular choice among programmers and 
* system administrators.

* i: Enter insert mode at the cursor.
* x: Delete the character under the cursor.
* dd: Delete the current line.
* yy: Copy the current line.
* u: Undo the last change.
* Ctrl+R: Redo the last undone change.
* :w: Save the file.
* :q: Quit Vim.
* :q!: Quit Vim without saving.
* :wq or :x: Save and quit Vim.
* :s/old/new/g: Replace all occurrences of “old” with “new.”
* :set nu or :set number: Display line numbers.
* v: Enter visual mode to select text.
* y: Copy the selected text.
* d: Delete the selected text.
* p: Paste the copied or deleted text.

### Java

Java is a high-level, class-based, object-oriented programming language that is designed to have a few implementation 
dependencies as possible. Java was designed by James Gosling at Sun Microsystems. It was released in May 1995 as a core
component of Sun's Java platform. It is a general-purpose programing language intended to let programmers write once,
run anywhere (WORA-write once, run anywhere, was a slogan to illustrate the cross-platform benefits in 1995), making 
that compiled Java code can run on all platforms that support Java without the need to recompile. Java applications are 
typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of teh underlying computer architecture.
The syntax of Java is similar to C and C++, but has fewer low-level facilities than either of them. The Java runtime 
provides dynamic capabilities (such as reflection and runtime code modification) that are typically not available in 
traditional compiled languages.

Java is:
 -High-level: Java abstracts many low-level tasks (e.g., memory management) so you can focus on the application logic rather than system details
 -Object-Oriented: Encourages modular design and code reuse via classes, objects, and interfaces
 -Platform-Independent: Java code si compiled into bytecode and runs on the Java Virtual Machine (JVM), making it "write
once, run anywhere"
 -Robust and Secure: Automatic memory management (garbage collection) and a strict typed system help prevent common 
programming errors.

Key Features and Concepts:
 - JVM(Java Virtual Machine) executes Java bytecode, allowing Java programs to run on any machine with a compatible 
   JVM implementation.
 - Java Development Kit(JDK). A software development kit that includes teh Java compiler (javac) and essential tools 
   to create, compile, and run Java programs.
 - Garbage Collection, Java automatically manages memory, freeing up objects that are no longer in use, reducing the 
   risk of memory leaks.
 - Rich Standard Library, Java offers a vast collection of libraries (collectively known as the Java Standard Library)
   for tasks like data structures, networking, I\O, GUI development, and more.
 - Object-oriented Programming (OOP)
   -Classes and objects: Basic building blocks for creating and organising code.
   - Inheritance: Allows you to create specialised classes by extending functionality of existing classes.
   - Polymorphism: Lets you work with objects in different classes in a unified way.
   - Encapsulation: Protects data by restricting direct access to the internals of a class.
 
Java is one of the most popular programming languages. Java programs can run on different platforms, including mobile, 
desktop, and other portable systems. You can use Java to build apps, games, banking applications, web app, and much more.



### C++

* Introduction:

C++ is a very popular, high-level, object-oriented, general-purpose programming languages that is made to create applications
and system programming. It was made by Bjarne Stroustrup at Bell Labs in 1983 as a continuation of C programming language.
It focuses on procedural, functional, and generic programming styles, which help develop operating systems, or creating 
applications but nowadays mainly used in game development. It is used to write efficient codes for larger applications,e.g.:
games, software, and graphical user interfaces.

* Key features of C++ programming languages
Writing a program should follow a program structure, which starts with the #include statement that should be added to the
header.