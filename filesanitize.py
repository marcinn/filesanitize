# coding: utf-8

"""
Common usage sanitizers
"""

import string
import unicodedata
import os

try:
    import translitcodec
except ImportError:
    pass

try:
    from django.utils.text import force_unicode
except ImportError:
    def force_unicode(x, encoding='utf-8'):
        if not isinstance(x, unicode):
            return x.decode(encoding)
        return x


DEFAULT_SAFE_FILENAME_CHARS = '-_.()%s%s' % (string.ascii_letters,
        string.digits)


def safe_filename(name, allowed_chars=None):
    """
    simple filename sanitizer

    >>> safe_filename(u'some str@ng3 File 12,0)a nAm#.txt')
    u'some_strng3_File_120)a_nAm.txt'

    >>> safe_filename(u'registered\xae sign.txt')
    u'registered_sign.txt'
    """

    allowed_chars = allowed_chars or DEFAULT_SAFE_FILENAME_CHARS

    try:
        name = force_unicode(name).encode('translit/one/ascii')
    except (UnicodeDecodeError, UnicodeEncodeError, TypeError, LookupError):
        name = force_unicode(name).encode('ascii', 'ignore')
    name = name.replace(' ','_')
    name = ''.join(c for c in name if c in allowed_chars)
    fn, ext = os.path.splitext(name)
    if not fn:
        raise ValueError('Cannot sanitize filename')
    return force_unicode(name)


def safe_path(path):
    """
    sanitize path

    >>> safe_path(u'/os//some #(dir/$0m3F  ile')
    u'/os/some_(dir/0m3F__ile'
    """
    path = os.path.normpath(path)
    return safe_filename(path, DEFAULT_SAFE_FILENAME_CHARS+os.path.sep)


def remove_accents(s):
    s = s.replace(u'ł', u'l').replace(u'Ł',u'L')
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

