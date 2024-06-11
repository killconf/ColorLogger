# ColorLogger

ColorLogger is a Python module that logs messages in color to stdout and/or a log file.

## Features

- Supports logging messages in different colors to stdout.
- Optionally logs messages to a file.
- Supports different logging levels: DEBUG, INFO, WARNING, ERROR, and NONE.

## Usage

Import the `ColorLogger` class from the `colorlog` module:

```python
from colorlog import ColorLogger
```
Create a ColorLogger instance
```
logger = ColorLogger(log_name='yourlog.log', log_dir='\\path\\to\\dir', level='DEBUG', log_to_file=True)
```
The `ColorLogger` class is initialized with the following parameters:

- `log_name` (str): The name of the log file. Defaults to 'logger.log'.
- `log_dir` (str): The directory to save the log file. If not provided, the current working directory is used.
- `level` (str): The logging level. One of 'DEBUG', 'INFO', 'SUCCESS', 'WARNING', 'ERROR', or 'NONE'. Defaults to 'INFO'.
- `log_to_file` (bool): Whether to save the log to a file. Defaults to False.

If `log_to_file` is set to True and a valid `log_dir` is provided or determined, a log file will be created in that directory. If the `log_name` does not include a file extension, '.log' will be used.

Once you have created an instance of `ColorLogger`, you can use it to log messages...

```python
logger.debug('Your debug message')
logger.info('Your info message')
logger.success('Your success message')
logger.warning('Your warning message')
logger.error('Your error message')
```
## License

MIT License

Copyright (c) 2024 killconf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.