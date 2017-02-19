import typing


def iter_sequence(seq: typing.List[typing.Any]):
    while True:
        for i in seq:
            yield i
