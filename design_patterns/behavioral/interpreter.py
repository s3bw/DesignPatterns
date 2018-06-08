"""
Interpreter
===========

(Page. 237)

Intent
------
Given a language, define a representation for its grammar along with an
interpreter that uses the representation to interpret sentences in the
language.

Motivation
----------
If a particular kind of problem occurs often enough, then it might be
worthwhile to express instances of the problem as sentences in a simple
language. Then you can build an interpreter that solves the problem by
interpreting these sentences.

The Interpreter pattern uses a class to represent each grammar rule.
The grammar is represented by fire classes; an abstract call
RegularExpression and its four subclasses LiteralExpression,
AlternationExpression, SequenceExpression and RepetitionExpression.

Applicability
-------------
Use the Interpreter pattern when there is a language to interpret, and
you can represent statements in the language as abstract syntax tress.
The Interpreter pattern works best when
 - The Grammar is simple.
 - Efficiency is not a critical concern.

Consequences
------------
1. It's easy to change and extend the grammar.
2. Implementing the grammar is easy, too.
3. Complex grammars are hard to maintain.
4. Adding new ways to interpret expressions.
"""
