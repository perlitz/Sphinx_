import os
import numpy as np


"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


def about_me(your_name: str) -> str:
    """A function about me

    Args:
        your_name: A name of yours

    Returns:
        A sring

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in range(4)])
        [0, 1, 2, 3]


    """
    return "The wise {} loves Python.".format(your_name)


class ExampleClass(object):
    """

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, name: str) -> None:
        """Initializer of ExampleClass

        Args:
            name: The name of the class

        Attributes:
        module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.



        """
        self.name: str = name


    def about_self(self) -> str:
        """
        Return information about an instance created from ExampleClass.

        Yields:
            int: The next number in the range of 0 to `n` - 1.

        Todo:
            * For module TODOs
            * You have to also use ``sphinx.ext.todo`` extension

        Examples:
            Examples should be written in doctest format, and should illustrate how
            to use the function::


                s = "Python syntax highlighting"

                $ python example_google.py



            >>> print([i for i in example_generator(4)])


        """
        return "I am a very smart {} object.".format(self.name)