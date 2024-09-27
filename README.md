# Hermes - Version 1.0

<img src="https://github.com/Pragyanshu-rai/static/blob/master/hermes/hermes_icon.png" alt="Hermes Logo" width="200" height="200">

## Welcome to Hermes

Hermes is a powerful and user-friendly command-line tool designed for searching text patterns across files and directories. Whether you're a developer searching through logs, or anyone needing to find patterns in a large file system, Hermes simplifies the task.

---

### Features:

- **Recursive Search**: Search for patterns recursively in directories.
- **Case-insensitive Search**: Perform case-insensitive searches with ease.
- **Simple CLI Options**: Intuitive and easy-to-use command-line options.

---

### Release 

You can download the latest release of the package [here](https://github.com/Pragyanshu-rai/hermes_cli/releases/tag/v1.0.0) or checkout the release page.

---

### Prerequisite

Ensure you have JRE installed:

```bash
sudo apt install default-jre
```

### Installation

Hermes requires Java Runtime Environment (JRE) 14 or higher. You can install it by downloading the `.deb` package and using `dpkg`.

```bash
sudo dpkg -i hermes_1.0.0_all.deb
```

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
-w, -W: Search for patterns recursively in directories.
-i, -I: Perform case-insensitive pattern matching.
-h, -H: Show this help message and exit.
```

### Example

To search for the pattern 'error' in /path/to/logs recursively and case-insensitively, use:

```bash
hermes -w -i 'error' /path/to/logs
```
---

## License

Hermes is licensed under MIT. For more details, check the license file.

***