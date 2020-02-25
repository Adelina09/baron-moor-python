#!/usr/bin/env python3

import abc

class Movement(abc.ABC):

    @abc.abstractmethod
    def nort(n):
        pass

    @abc.abstractmethod
    def south(s):
        pass

    @abc.abstractmethod
    def west(w):
        pass

    @abc.abstractmethod
    def east(e):
        pass

    



