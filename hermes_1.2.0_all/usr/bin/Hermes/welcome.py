

def printWelcome():
  welcome_text = f"""
###############################################
#                                             #
#       Welcome to hermes - Version 1.2       #
#                                             #
#     A tool for searching text patterns      #
#   across files and directories with ease.   #
#                                             #
###############################################

              ++=:=========:
              ++=:...:::...*+:
              ++. .++==++  **%-
              ++. *+    .%.  *=
              ++. ++    :#   *=
              ++   -*++++#*   =
              ++ .======--\\\\  =
              ++..=======-:\\\\:=
              ++..========- ##=
              =*..========-..*=
              .=+++++++++++++=.

Usage: hermes [OPTIONS] [FILE_PATH] [PATTERN] 

Options:
    -w, -W          Search for patterns recursively in directories.
    -i, -I          Perform case-insensitive pattern matching.
    -c, -C          Will color code the output.
    -l, -L          Can specify the depth level for the search by passing a number in the argument with this flag set.
    -r, -R          Will run a recursive search down from the give path, this Supersedes depth level flag.
    -p, -P          Will log the performance metric for the search session.
    -h, -H          Show this help message and exit.

Example:
  hermes -w -i /path/to/logs error

Start finding patterns now and streamline your workflow!
"""

  print(welcome_text)


if __name__ == "__main__":
  printWelcome()