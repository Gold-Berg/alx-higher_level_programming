#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError("Cannot dynamically create new instance attributes")
        super().__setattr__(attr, value)
