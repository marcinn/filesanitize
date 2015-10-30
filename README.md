## filesanitize

[![Build Status](https://travis-ci.org/marcinn/filesanitize.svg?branch=master)](http://travis-ci.org/marcinn/filesanitize)

A small library for sanitizing filenames in Python 2.6/2.7 by removing accents,
special chars and decoding unidode.

### Usage


Sanitize a path:


```
> import filesanitize
> filesanitize.safe_path('/path/to/Str@ng#F!l3name.txt')
u'/path/to/StrngFl3name.txt'
```

Sanitize a filename only:

```
> import filesanitize
> filesanitize.safe_filename('Str@ng#F!l3name.txt')
u'StrngFl3name.txt'
```


### License

BSD (see LICENSE.md)


