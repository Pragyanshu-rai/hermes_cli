# Hermes - Version 1.2

<img src="https://github.com/Pragyanshu-rai/static/blob/master/hermes/hermes_icon.png" alt="Hermes Logo" width="200" height="200">

## Welcome to Hermes

Hermes is a powerful and user-friendly command-line tool designed for searching text patterns across files and directories. Whether you're a developer searching through logs, or anyone needing to find patterns in a large file system, Hermes simplifies the task.

---

### Features:

- **Recursive Search**: Search for patterns recursively in directories.
- **Case-insensitive Search**: Perform case-insensitive searches with ease.
- **Level Limit Search**: Search for patterns up to the required depth.
- **Performance Metric**: Get a real-time performance log for the search session.

---


### Release 

You can download the latest release of the package [here](https://github.com/Pragyanshu-rai/hermes_cli/releases/tag/v1.2.0) or checkout the release page.

---

### Prerequisite

Ensure you have JRE installed:

```bash
sudo apt install default-jre
```

### Installation

Hermes requires Java Runtime Environment (JRE) 14 or higher. You can install it by downloading the `.deb` package and using `dpkg`.

```bash
sudo dpkg -i hermes_1.2.0_all.deb
```

*Here 'hermes_1.2.0_all.deb' denotes the version of the package you wish to install.*

### Validate Install

Run
```bash
which hermes
```
to check if the package has been installed on your system.

### Uninstalling

Run 
```bash
sudo dpkg -r hermes
```
to uninstall the package.

---

### Usage

The basic usage of the Hermes tool is as follows:
``` bash
hermes [OPTIONS] [FILE_PATH] [PATTERN]
```

### Options
```bash
  -w, -W          Search for patterns recursively in directories.
  -i, -I          Perform case-insensitive pattern matching.
  -c, -C          Will color code the output.
  -l, -L          Can specify the depth level for the search by passing a number in the argument with this flag set.
  -r, -R          Will run a recursive search down from the give path, this Supersedes depth level flag.
  -p, -P          Will log the performance metric for the search session.
  -h, -H          Show this help message and exit.
```

### Example

To search for the pattern 'error' in /path/to/logs recursively and case-insensitively, use:

```bash
hermes -w -i /path/to/logs error
```
---

## License

Hermes is licensed under MIT. For more details, check the license file.

***
