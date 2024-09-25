

def printWelcome():
  welcome_text = f"""
###############################################
#                                             #
#       Welcome to hermes - Version 1.0       #
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
  -h, -H          Show this help message and exit.

Example:
  hermes -w -i 'error' /path/to/logs

Start finding patterns now and streamline your workflow!
"""

  print(welcome_text)


if __name__ == "__main__":
  printWelcome()